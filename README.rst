=============
README
=============

The nit and gritty behind Python Wars Solo 1

Usage
=====

::

    $ pip install python-wars-solo
    $ pythonwarsolo

Introduction
============

Python Wars Solo is the result of a few hours effort roughly duplicating a text-based Star Trek game I wrote back in 1980-1981.  You fought up to 9 Klingons in your Enterprise.  Beating one was a piece of cake.  Three was a fun challenge.  Five was tough.  Seven was done only a few times.  Nine was never done.  The game was simple, fast, easy to learn, and tons of fun.

Now I don't remember much about the mechanics of the code I wrote back in High School.  So when I started writing Python Wars Solo I decided not to worry about it.  I would code how I felt like coding, and just create a game.

There were a few false starts.  I kept trying to add tons of complexity to the code, or lots of neat features.  Lots of time was wasted and not much was done.  The technical term for what I was doing is 'Scope Creep'.  Then someone advised that I just make it really simple and get it done.

And I did.  I got it done.

To avoid potential yet likely silly copyright/trademark issues, I renamed the ship the '*Pythonista*'.  The enemies are the evil '*Zargons*'.

Flashpoint in GitHub History
=============================

In 2011, at the first and last inaugural PyCodeConf, GitHub founder Chris Wanstrath (@defunkt), introduced me by asking me in front of various Python luminaries (Raymond Hettiger, Travis Oliphant, David Beasley, Jesse Noller, the young Kenneth Reitz) details about this... er... game.

Definitely my most memorable introduction ever.

Updated for Python 3!
======================

Thanks to @Scribilicious Python Wars Solo war is now Python 3 compatible. In fact, it no longer works for Python 2.7.


Details
=======

 * Command the Battle Cruiser Pythonista!
 * Fight the good fight against the evil Zargons
 * Use your ship's spinal mounted beam cannon to slice and dice the enemy to pieces!
 * Launch missiles to destroy Zargons in single shots
 * Fight up to 9 enemies!
 * Old school text based game
 * Easy to learn
 * Addictive

Future Version Thoughts
========================

Originally I thought of expanding this out to become a game with graphics and maybe a campaign. Then I went onto other things. But here was my original list of things to add:

 * Keep basic mechanics
 * Add 2-D map
 * Incorporate PyGame
 * Since all components are objects on ship objects which exist in the space object, current version could easily be expanded:
 * Let players build their own ships and use introspection to generate menus
 * Damage the ship in ways so that parts get broken
