
Basic Items
===========

Modding items in Crea is easy! In this guide we will break down all of the different components used to make different types of items.


Furniture
---------

**Antlers**

There will be multiple examples in this section, since different items perform different roles. The first example will be antlers.
1.png

First notice that on line 1 we import Axis.
::

    from core.template.item import Axis, Item, Material

On line 5 we have useTime, this tells the game how much time it takes for the player to use the item in the game.
::

    useTime=20,

All the way at the bottom on line 21 we tell the game that the antlers can be placed on backwalls.
::

    antlers.placeable(backwall_axis=Axis())

The backwall_axis portion is the part that tells the game where to look to see if there is support for the item.


**Small Table**

The next example will be a small table.
2.png

On lines 1 through 4 we import some more groups. Support and Direction are the two new ones.
::

    from core.template.item import Axis, Item, Material, Support

    from siege.component import Direction
    from siege.util import Vector

On line 8 we have stack, this tells the game how many of the item can be held in a single inventory slot.
::

	stack = 99,

The player will be able to hold up to 99 small tables in a single space of their bag.

On line 23 it tells the game that the small table can be placed on the floor and can support things on top of it.
::

    small_table.placeable(floor_axis=Axis(support_top=Support()))

The floor_axis section tells the game that the table needs blocks under it.
The Axis(support_top=Support()) tells the game that the item will support other items on top of it.

On lines 25 through 30 we have some code to manage the support.
::

    small_table.hasPhysics(
        immovable = True,
        collision = Direction.TOP,
        passthrough = Direction.TOP,
        gravity = Vector()
    )

Line 26 tells the game that once the table is placed down the blocks that are supporting it can't be removed. This is done to
prevent a cascade of items breaking, since a player can place things on top of the table.
Line 27 tells the game that things can collide with the top of the table. This means player will be able to jump on top of it.
Line 28 tells the game that if players want to they can pass through the top of the table.


**Door**

The next example will be the door. This starts to get a little more complicated, since the player can interact with it in the game.
3.png
4.png

Lines 1 through 6 import all the groups that we will be using. The three new ones are Frame, Frames, and game.
::

    from core.template.animation import Frame, Frames
    from core.template.item import Axis, Item, Material

    from siege import game
    from siege.component import Direction
    from siege.util import Vector

The frames are needed since the item will change what it looks like when the player interacts with it.
The game import is needed since it will need to know what state the item is in, so it knows what to do when the player interacts
with it.

Line 26 makes it so the supporting blocks can be destroyed, causing the item to break and be picked up.
::

    allowSupportRemoval = True,

On line 32 the collision is set to every direction. When the door has physics nothing will be able to pass through it.
::

    collision = Direction.ALL,

Lines 37 through 48 set up the door so it can be changed between being open and closed
::

    @door.events('interact')
    def interactDoor(player, entity, position):
        #Toggle between being open and closed
        #We can check which animation is currently being played to know the state
        isActive = entity.physics.active
        if isActive:
            entity.animation.play("opened", forceRestart=True)
            game.audio.playAt("mods/core/audio/sfx/misc/door_open.ogg", entity.realm.uid, entity.getPosition(), broadcast=True)
        else:
            entity.animation.play("closed", forceRestart=True)
            game.audio.playAt("mods/core/audio/sfx/misc/door_close.ogg", entity.realm.uid, entity.getPosition(), broadcast=True)
        entity.physics.active = not isActive

Line 37 it is telling the game that the player is able to interact with the item.
Line 38 it is setting up all of the code below that will be part of it. The three variables, or arguments inside the parentheses 
are what the code is going to determine where each individual door is in the world, and letting the player interact with it.
Lines 39 and 40 are just comment lines, that are there to tell people what the code is for. Any line with a # in front of it
will become a comment line, and have no effect to the code.
Line 41 tells the game that if the door is closed, then it has physics and things can't pass through it.
Line 42 checks to see if the door is closed.
If the door is closed it will go ahead with lines 43 and 44. Line 43 tells the game to play the open animation and resets the
physics. On line 44 it tells the game to play the opening door sound effect and to broadcast it to nearby players.
If the door was open it will skip lines 43 and 44 and perform lines 46 and 47, which will close the door.
Line 48 will change the door between being active and not active.

Lines 50 and 51 are going into the png file and assigning which image is closed and which one is open.
::

    closed = door.getSpriteFrames(Frame(39, 2, size=(14, 48)))
    opened = door.getSpriteFrames(Frame(2, 2, size=(35, 48)))

For the opened frame it tells the code to start at the vector 2x, 2y on the png file. Then it tells the game to use from the 
start all the way to 35x, 48y.

Lines 53 through 57 are setting up the animations.
::

    door.animations(
        start = 'closed',
        closed = Frames(closed()),
        opened = Frames(opened())
    )

On line 54 it tells the game to always place doors down as being closed.
Then on lines 55 and 56 it is assigning what frame is considered opened and what one is closed.

I know that was a lot, but hopefully now you can make some basic interactable objects.


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
