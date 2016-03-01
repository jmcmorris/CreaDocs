
.. _basic-items:

Basic Items
===========

In this section, we'll take a look at some source code from very simple items
already in the game to get you on the right track.

Let's head over to the Crea directory (and if you don't know how to navigate
there, take a minute to look over 
:ref:`where it's located and how it's structured <locating-crea>`), and then
into mods/core/item/material.

Take a look through. The first thing you might notice is that every item is 
composed of at least two files, an image file (.png) and some source code 
(.ce). This is because Items in Crea are considered content entities. Content
entity files are designated with the file extension (.ce). The Crea game engine
looks for these files when the game is launched and then looks for an image
file to match them with. This is important to know when modding Crea.


Hide
----

We'll start off by taking a look hide.ce:

.. code-block:: python
   :linenos:

    from core.template.item import Item, ScrapTier

    Item(
        name = "Hide",
        classification = "Trophy",
        stack = 99,
        price = 40,
        scraps = ScrapTier.One
    )

10 lines of code and a sprite! That's all it takes to mod an item into Crea!
Let's break down what's actually going on here.

The start of .ce files and .py files always hold imports. An import takes
source code from a different location and *imports* that source code into the
current file. In this case, we are importing the pre-built template for Items
and the enum for ScrapTier.

Item is a Python class. You won't need to know much Python to do basic modding.
What you need to know at this point is that parenthases '()' following a class
name initializes an instance of that class, so what we are saying at line 3 is
that we are initializing an instance of an Item.

The following lines up to the closing parenthases ')' are parameters defining this
specific Item instance. Here we have an Item with the name Hide and an Item
classification of Trophy. We can stack 99 of them in one item slot in our bag,
It has a price of 40 Auri when sold, and gives the lowest number of scraps
when scrapped.
