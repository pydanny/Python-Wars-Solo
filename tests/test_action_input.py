"""Exercise action selection through the real interactive game loop."""

import contextlib
import io
import unittest
from unittest.mock import patch

import go
import stuff


class ActionInputTests(unittest.TestCase):
    def play(self, answers, *, ammo=5, shields=100.0, charge=100):
        universe = stuff.Universe()
        cruiser = stuff.Cruiser("Pythonista")
        cruiser.missile.ammo = ammo
        cruiser.shields = shields
        cruiser.spinal_mount.capacitor = charge
        responses = iter(answers)
        prompts = []

        def answer(prompt):
            prompts.append(prompt)
            try:
                return next(responses)
            except StopIteration:
                self.fail("The game requested unexpected additional input")

        output = io.StringIO()
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(stuff, "Universe", return_value=universe))
            stack.enter_context(patch.object(stuff, "Cruiser", return_value=cruiser))
            stack.enter_context(patch("builtins.input", side_effect=answer))
            stack.enter_context(patch.object(go.random, "randrange", return_value=0))
            stack.enter_context(contextlib.redirect_stdout(output))
            go.main()

        return cruiser, prompts, output.getvalue()

    def test_unknown_action_does_not_advance_turn_or_change_ship(self):
        cruiser, prompts, output = self.play(
            ["1", "a", "typo", "exit"], shields=50.0, charge=10
        )
        self.assertEqual(cruiser.shields, 50.0)
        self.assertEqual(cruiser.spinal_mount.capacitor, 10)
        self.assertEqual(cruiser.missile.ammo, 5)
        self.assertEqual(prompts[-2:], ["What is your action? "] * 2)
        self.assertNotIn("Turn 2", output)

    def test_empty_action_reprompts_without_enemy_attack(self):
        cruiser, prompts, output = self.play(["1", "a", "", "exit"])
        self.assertEqual(cruiser.shields, 100.0)
        self.assertEqual(prompts[-2:], ["What is your action? "] * 2)
        self.assertNotIn("Turn 2", output)

    def test_unavailable_missiles_do_not_advance_turn(self):
        cruiser, prompts, output = self.play(
            ["1", "a", "m", "exit"], ammo=0, shields=50.0, charge=10
        )
        self.assertEqual(cruiser.shields, 50.0)
        self.assertEqual(cruiser.spinal_mount.capacitor, 10)
        self.assertEqual(cruiser.missile.ammo, 0)
        self.assertEqual(prompts[-2:], ["What is your action? "] * 2)
        self.assertNotIn("Turn 2", output)

    def test_valid_action_after_typo_keeps_selected_target(self):
        cruiser, prompts, output = self.play(["1", "a", "typo", "S", "exit"])
        self.assertEqual(cruiser.spinal_mount.capacitor, 10)
        self.assertEqual(cruiser.shields, 90.0)
        self.assertEqual(prompts.count("Who is your target? "), 2)
        self.assertEqual(output.count("Turn 2"), 1)
        self.assertNotIn("Turn 3", output)

    def test_spinal_mount_still_consumes_one_turn(self):
        cruiser, _, output = self.play(["1", "a", "s", "exit"])
        self.assertEqual(cruiser.spinal_mount.capacitor, 10)
        self.assertEqual(cruiser.shields, 90.0)
        self.assertIn("Turn 2", output)

    def test_available_missile_still_consumes_one_turn(self):
        cruiser, _, output = self.play(["1", "a", "m", "exit"])
        self.assertEqual(cruiser.missile.ammo, 4)
        self.assertEqual(cruiser.shields, 90.0)
        self.assertIn("Turn 2", output)

    def test_damage_control_still_consumes_one_turn(self):
        cruiser, _, output = self.play(
            ["1", "a", "d", "exit"], shields=50.0, charge=10
        )
        self.assertEqual(cruiser.shields, 52.0)
        self.assertEqual(cruiser.spinal_mount.capacitor, 30)
        self.assertIn("Turn 2", output)

    def test_exit_at_action_menu_does_not_advance_turn(self):
        cruiser, _, output = self.play(["1", "a", "EXIT"], shields=50.0, charge=10)
        self.assertEqual(cruiser.shields, 50.0)
        self.assertEqual(cruiser.spinal_mount.capacitor, 10)
        self.assertNotIn("Turn 2", output)


if __name__ == "__main__":
    unittest.main()
