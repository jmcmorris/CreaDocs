
Bags and Chest
--------------

Before reading it is recommended to have already gone through the guides above, as things that were explained in them will not be explained here.

Bags and chest are not all that difficult. They just require a few new lines of code. There will be two examples here, the bag and the large gold
chest.

The bag will be first.
1.png

The first new variable we see is on line 7.
::

    requiresResearch = False

This makes it so once the player gets the item in their inventory they gain knowledge of it and don't have to research it. This is most often done
for rare items that it might be unreasonable to require player's to waste some researching.

On line 10  it sets the bag with the ability to carry items.
::

    bag.hasInventory(capacity=20, carryable=True)

The capacity tells the game how many slots the bag has.
The carryable tells the game that the player is able to put the bag in the pouch slot in their inventory menu.

On to the large gold chest
2.png

On lines 1 and 2 we have some new groups, or classes.
::

    from core.template.item import Material, StorageContainer
    from siege.util import PixelRect

The StorageContainer is called since there is some special logic involved with placing down chest in the world generation and populating it with
items with a player opens it for the first time.
The PixelRect is used since pixel perfect collision doesn't work alone for placing down a chest, since it gets larger when it opens.

Line 7 and 8 tells the game what is required to open the chest if it is locked.
::

    keyRequired = 'gold_key',
    lockpick = 'gold_lockpick',

For the gold chest it tells the game that the player either needs to have a gold key or a gold lockpick.

Line 16 sets the area needed for the chest to be placed down.
::

    area = PixelRect(0, 12, 32, 16)

Then on line 19 it tells the game to create a marker on the map.
::

    chest.hasMapMarker(markerType='chest')

The marker type is set to chest for this, as defined in the parentheses.

That concludes the item guide! Hopefully it helped. Now go make some items!

