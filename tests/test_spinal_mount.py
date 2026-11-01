import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import go
import stuff


class SpinalMountTests(unittest.TestCase):
    def setUp(self):
        self.player = stuff.Cruiser('Pythonista')
        self.enemy = stuff.Frigate('Bunny', 'bunny', 80)
        self.weapon = self.player.spinal_mount

    def fire_without_hits(self):
        # Zero attack and defense rolls keep the target alive without
        # replacing the real ship, weapon, or damage/recharge behavior.
        with patch.object(stuff.random, 'randrange', return_value=0):
            with redirect_stdout(io.StringIO()):
                return self.weapon.action(self.player, self.enemy)

    def test_partial_charge_spends_only_energy_of_fired_lasers(self):
        self.weapon.capacitor = 10
        self.assertTrue(self.fire_without_hits())
        self.assertEqual(self.weapon.capacitor, 1)
        self.assertEqual(self.enemy.shields, 30)

    def test_empty_weapon_does_not_spend_energy(self):
        self.weapon.capacitor = 0
        self.assertTrue(self.fire_without_hits())
        self.assertEqual(self.weapon.capacitor, 0)
        self.assertEqual(self.enemy.shields, 30)

    def test_fully_charged_sequence_keeps_existing_cost(self):
        self.assertTrue(self.fire_without_hits())
        self.assertEqual(self.weapon.capacitor, 0)
        self.player.recharge()
        self.assertEqual(self.weapon.capacitor, 10)

    def test_exact_charge_spends_no_more_than_available(self):
        self.weapon.capacitor = 9
        self.assertTrue(self.fire_without_hits())
        self.assertEqual(self.weapon.capacitor, 0)

    def test_destroyed_target_stops_sequence_and_preserves_unused_charge(self):
        # A successful first attack and three 10-point hits destroy a
        # normal frigate after the third laser, which costs 9 energy.
        with patch.object(stuff.random, 'randrange', side_effect=[19, 0, 9, 9, 9]):
            with redirect_stdout(io.StringIO()):
                survived = self.weapon.action(self.player, self.enemy)
        self.assertFalse(survived)
        self.assertFalse(self.enemy.alive)
        self.assertEqual(self.weapon.capacitor, 91)

    def test_game_recharges_after_consecutive_firing_turns(self):
        output = io.StringIO()
        commands = ['1', 'a', 's', 'a', 's', 'a', 'exit']
        with patch('builtins.input', side_effect=commands):
            with patch.object(stuff.random, 'randrange', return_value=0):
                with redirect_stdout(output):
                    go.main()
        self.assertIn('Capacitor at 100 %', output.getvalue())
        self.assertIn('Capacitor at 10 %', output.getvalue())
        self.assertIn('Capacitor at 11 %', output.getvalue())


if __name__ == '__main__':
    unittest.main()
