
Items
=====

Modding items in Crea is easy! In this guide we will break down all of the different components used to make different types of items.

Basic Sword
-----------

Let's kicks things off with a very simple sword. We are going to be using the bone sword as our example. To get to the bone sword file we need to find our steam apps folder which contains Crea. This can be easily done by right click on Crea in Steam and clicking on properties. Then select the tab Local Files, and after that just click on the Browse Local Files button. Now that we are in the Crea folder we just need to click on the folders mods/core/item/weapon/sword and then just click on the bone_sword.ce file.

1.png

* First off we have the files that we import in on line 1.

from core.template.item import Material, Sword, StatAttribute

 * core.template.item is the file directory. This shows what file we are importing from. After import we have the groups of code that we want to use
 for this sword. These groups are called classes.

* We name the sword on line 4. name = "BoneSword".

	name = "BoneSword",

 * We don't put any spaces in the name here because the name that people will actually see is in the en.local file.

* On line 5 there is the power of the sword. The bone sword has a power of 36.

	power = 36,

 * The power of the weapon is part of the algorithm that that is used to calculate how much damage is dealt when something is hit.

* Line 6 has the items craft level. This means that the craft talent needs to be only level 1 to make the bone sword.

	level = 1,

* Line 7 dictates the base amount of crafting TP the player will gain when making the bone sword.

	experience = 15,

 * The base amount means that the player will gain that amount if their crafting level is the same level as the item's crafting level.
 * If the player's crafting level is higher than the item's crafting level then the amount of talent points gain will be less.
 * If the player's crafting level is lower than the item's crafting level then the amount of talent points gain will be more.

* On line 8 we have the price of the item.

	price = 25,

 * The price of the item is how much an NPC will sell it for, and the player is able to sell it to an NPC for 1/5 of that price.
 * This means that while the player can buy the bone sword from an NPC for 25 auri, the player will sell it to an NPC for 5 auri.

* Next on line 9 we have materials which dictates what items are needed to craft the item.

	materials = [
        Material('lumber', quantity=5),
        Material('bone', quantity=2),
        Material('vine', quantity=6),
    ],

 * This uses the class materials that we imported on the first line.
 * Lets look at the first material used for the bone sword.
  * Material tells the game to call the class that we imported.
  * 'lumber' tells the game what item to use.
  * quantity=5 tells the game that 5 lumber are needed to craft the item.

* Now onto line 14 we have the potentialRange.

	potentialRange = (0, 2),

 * The potentialRange tells the game how many potentials an item can have.
 * The bone sword has a potentialRange of (0, 2) this means that is can have either 0 potentials, 1 potential, or 2 potentials.

* On line 15 we tell the game what potentials the item can have.

	potentials = [
        StatAttribute('ATK', valueRange=(2, 4), weight=5),
        StatAttribute('HP', valueRange=(3, 6), weight=2)
    ]

 * A potential is an added stat that the item can randomly acquire.
 * The bone sword only has two different potentials. Let's use the first one as the example.
  * StatAttribute tells the game to call the class we imported on line 1.
  * 'ATK' is the potential that will be added on if it is chosen.
  * The valuseRange=(2, 4) is how much potential 'ATK' the bone sword can have.
  * The weight=5 is the likely hood of the item being chosen as a potential.
   * weight works by taking all the weight values and adding them together and randomly drawing one.

* It is important to follow the syntax that is in place, otherwise the game will not be able to read the file.
 * Everything is case sensitive.
 * Commas must be used to tell the game that it is moving on from one thought to the next.
 * The parentheses and brackets must be used.
 * Indentation is important. If something is indented it means it piece of code that falls under the line that is not indented above it.

After all of this is done to the .ce file there is just the matter of visuals. Lets go back to the sword folder.
Every sword needs to have three .png files. 

bone_sword.png for the animations
2.png

bone_sword_icon.png for what is shown in the inventory.
3.png

bone_sword_mask.png to provide extra range for the item to hit the enemies.
4.png

 It is important to have them named as such otherwise the game will not know that they are associated with the bone_sword.ce file.
 This is everything needed to make a basic weapon.


Advanced Armor
---------------

Before reading it is recommended to have already gone through the basic sword guide, as things that were explained in it will not be explained here.

Making more advanced armor and weapons are almost the same. The example item that is going to be used will be the beast helm. To get to the
beast_helm.ce file just go to mods/core/item/armor/head and open the file.

1.png

* After seeing the file there are a few differences in how it is formated compared to the bone sword. Since it is more complicated it is split
up into different sections in order for it to be easier to read.

* On lines 1 through 3 we are importing the classes we want to use. Each file we want to import a class from needs a different line.

from core.template.template import Hide, Substitute
from core.template.item import Item, Material, RollAttribute, StatAttribute
from siege.util import Vector

* The first new variable we come to is on line 7. The unique variable just means that this item will get it's own id when the game saves, so
when the player loads the game again the item will have the same stats and potentials.

	unique = True,

* The next new variables we come across are on line 12 and 13. The category and subcategory are used to define what the item falls under for when
the player tries to look up the item in the game while crafting.

	category = "Armor",
    subcategory = "Head",

 * The beast helm will be under the category "Armor" and it will be under the subcategory "Head".

* Then on line 16 it defines what crafting surface is required to craft the item.

	serviceRequired = "Workstation",

 * The serviceRequired = "Workstation" tells the game that in order for the player to craft a beat helm the player needs to be next to a workstation.

* On line 17 it tells the game that in order to craft the item it needs to upgrade from another item.

	upgradeFrom = 'light_hood_plus',

 * For the beast helm it tells the game that a light hood plus is needed to craft it.
 * When an item upgrades from another item it keeps all of attributes and stats on the item and adds the new ones to it.

* On line 28 we have the slot variable. This is where we tell the game where the piece of gear can be equipped to.

	slot = "head",

 * The beast helm is equipped onto the players head space in the game.

* The levelRequired variable on line 29 tells that game what combat level the character needs to be in order to put on the gear.

	levelRequired = 8,

 * The beast helm has a level requirement of 8.

* On line 30 through 32 it tells the game where to put the items graphics over the character.

	visuals = [
        Substitute('helmet', origin=Vector(1, 1)),
        Hide('hair_top')
    ],

 * Line 31 calls the class Substitute from line 1, and it tells the game to put the beast helm on the character head.
 * On line 32 the Hide class tells the game to put the helmet over the characters hair.

*Lastly on line 34 through 36 we assign attributes that the item will always have.

	attributes = [
        RollAttribute(valueRange=(3, 5)),
        StatAttribute('DEF', valueRange=(1, 2)),
    ],

 * Line 35 calls the class RollAttribute. This is a special attribute, we have all of our special attributes in the file
 core.template.item.
 * Line 36 will always give the item the StatAttribute as opposed to the potentials which is random. 

 That completed the beast_helm.ce file. Now it just needs the beast_helm.png file and the beast_helm_icon.png file and the item is done.


Furniture
---------

*Antlers*

Before reading it is recommended to have already gone through the guides above, as things that were explained in them will not be explained here.

There will be multiple examples in this section, since different items perform different roles. The first example will be antlers.
1.png

* First notice that on line 1 we import Axis.

from core.template.item import Axis, Item, Material

* On line 5 we have useTime, this tells the game how much time it takes for the player to use the item in the game.

	useTime=20,

* All the way at the bottom on line 21 we tell the game that the antlers can be placed on backwalls.

antlers.placeable(backwall_axis=Axis())

 * The backwall_axis portion is the part that tells the game where to look to see if there is support for the item.

*Small Table*

The next example will be a small table.
2.png

* On lines 1 through 4 we import some more groups. Support and Direction are the two new ones.

from core.template.item import Axis, Item, Material, Support

from siege.component import Direction
from siege.util import Vector

* On line 8 we have stack, this tells the game how many of the item can be held in a single inventory slot.

	stack = 99,

  * The player will be able to hold up to 99 small tables in a single space of their bag.

* On line 23 it tells the game that the small table can be placed on the floor and can support things on top of it.

small_table.placeable(floor_axis=Axis(support_top=Support()))

 * The floor_axis section tells the game that the table needs blocks under it.
 * The Axis(support_top=Support()) tells the game that the item will support other items on top of it.

* On lines 25 through 30 we have some code to manage the support.

small_table.hasPhysics(
    immovable = True,
    collision = Direction.TOP,
    passthrough = Direction.TOP,
    gravity = Vector()
)

 * Line 26 tells the game that once the table is placed down the blocks that are supporting it can't be removed. This is done to
 prevent a cascade of items breaking, since a player can place things on top of the table.
 * Line 27 tells the game that things can collide with the top of the table. This means player will be able to jump on top of it.
 * Line 28 tells the game that if players want to they can pass through the top of the table.

*Door*

The next example will be the door. This starts to get a little more complicated, since the player can interact with it in the game.
3.png
4.png

* Lines 1 through 6 import all the groups that we will be using. The three new ones are Frame, Frames, and game.

from core.template.animation import Frame, Frames
from core.template.item import Axis, Item, Material

from siege import game
from siege.component import Direction
from siege.util import Vector

 * The frames are needed since the item will change what it looks like when the player interacts with it.
 *The game import is needed since it will need to know what state the item is in, so it knows what to do when the player interacts
 with it.

* Line 26 makes it so the supporting blocks can be destroyed, causing the item to break and be picked up.

	allowSupportRemoval = True,

* On line 32 the collision is set to every direction. When the door has physics nothing will be able to pass through it.

	collision = Direction.ALL,

* Lines 37 through 48 set up the door so it can be changed between being open and closed

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

 * Line 37 it is telling the game that the player is able to interact with the item.
 * Line 38 it is setting up all of the code below that will be part of it. The three variables, or arguments inside the parentheses 
 are what the code is going to determine where each individual door is in the world, and letting the player interact with it.
 * Lines 39 and 40 are just comment lines, that are there to tell people what the code is for. Any line with a # in front of it
 will become a comment line, and have no effect to the code.
 * Line 41 tells the game that if the door is closed, then it has physics and things can't pass through it.
 * Line 42 checks to see if the door is closed.
  * If the door is closed it will go ahead with lines 43 and 44. Line 43 tells the game to play the open animation and resets the
  physics. On line 44 it tells the game to play the opening door sound effect and to broadcast it to nearby players.
 * If the door was open it will skip lines 43 and 44 and perform lines 46 and 47, which will close the door.
 * Line 48 will change the door between being active and not active.

* Lines 50 and 51 are going into the png file and assigning which image is closed and which one is open.

closed = door.getSpriteFrames(Frame(39, 2, size=(14, 48)))
opened = door.getSpriteFrames(Frame(2, 2, size=(35, 48)))

 * For the opened frame it tells the code to start at the vector 2x, 2y on the png file. Then it tells the game to use from the 
 start all the way to 35x, 48y.

* Lines 53 through 57 are setting up the animations.

door.animations(
    start = 'closed',
    closed = Frames(closed()),
    opened = Frames(opened())
)

 * On line 54 it tells the game to always place doors down as being closed.
  * Then on lines 55 and 56 it is assigning what frame is considered opened and what one is closed.

I know that was a lot, but hopefully now you can make some basic interactable objects.


Bags and Chest
--------------

Before reading it is recommended to have already gone through the guides above, as things that were explained in them will not be explained here.

Bags and chest are not all that difficult. They just require a few new lines of code. There will be two examples here, the bag and the large gold
chest.

The bag will be first.
1.png

* The first new variable we see is on line 7.

  requiresResearch = False

 * This makes it so once the player gets the item in their inventory they gain knowledge of it and don't have to research it. This is most often done
 for rare items that it might be unreasonable to require player's to waste some researching.

* On line 10  it sets the bag with the ability to carry items.

bag.hasInventory(capacity=20, carryable=True)

 * The capacity tells the game how many slots the bag has.
 * The carryable tells the game that the player is able to put the bag in the pouch slot in their inventory menu.

On to the large gold chest
2.png

* On lines 1 and 2 we have some new groups, or classes.

from core.template.item import Material, StorageContainer
from siege.util import PixelRect

 * The StorageContainer is called since there is some special logic involved with placing down chest in the world generation and populating it with
 items with a player opens it for the first time.
 * The PixelRect is used since pixel perfect collision doesn't work alone for placing down a chest, since it gets larger when it opens.

* Line 7 and 8 tells the game what is required to open the chest if it is locked.

    keyRequired = 'gold_key',
    lockpick = 'gold_lockpick',

 * For the gold chest it tells the game that the player either needs to have a gold key or a gold lockpick.

* Line 16 sets the area needed for the chest to be placed down.

  area = PixelRect(0, 12, 32, 16)

* Then on line 19 it tells the game to create a marker on the map.

chest.hasMapMarker(markerType='chest')

 * The marker type is set to chest for this, as defined in the parentheses.

 That concludes the item guide! Hopefully it helped. Now go make some items!


