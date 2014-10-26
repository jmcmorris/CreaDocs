
Getting Started
===============

Modding in Crea is all done in `Python <https://www.python.org/>`_; however, you don't have to know Python to create simple content such as items or new character customizations. When modding in Crea there are several file types to be aware of.
 * *.ce*   - Content Entity file which represents a type of content such as a single monster or item (Python file treated specially by the game)
 * *.py*   - Python file used for systems
 * *.png*  - Image file used by the game
 * *.scml* - `Spriter <http://www.brashmonkey.com/spriter.htm>`_ character file used for modular sprites


Possibilities
-------------

"Is it possible to mod ____?" - The answer is almost always yes. Here is a list of some of the things you can mod.

**Content**
 * Character Customizations
 * Items (Materials, Equipment, Weapons, Blocks)
 * Monsters and Bosses
 * NPCS
 * Character Races
 * Biomes and Plants
 * Talents and Skills

**Systems**
 * Crafting
 * Research
 * World Generation
 * Conflict
 * Combat
 * Talent


Directory Structure
-------------------

Typically files can be placed however you want inside a mod; however, there are a few files that are needed or are treated specially.

 * mymod
  * info
  * preview.png
  * registration.py
  * coremod/

info
    Contains mod information such as title, description, and version number. (`JSON Format <http://www.json.org/>`_)

registration.py
    Game engine will call the ```register``` method when registering all mod packages.

coremod/
    Allows for modification of python code in the core package
