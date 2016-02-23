
Gear
====


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
