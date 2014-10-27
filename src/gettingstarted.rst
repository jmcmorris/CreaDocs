
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


Locating the Crea Files
-----------------------

To find the Crea source code:

 * Open Steam and go to your library.
 * Right click on Crea and click on the "Properties" option.
 * Click on the "Local Files" tab.
 * Click "Browse Local Files..." button from that page.


Getting a Text Editor
---------------------

Now that you've found the source code, you'll want to use a text editor while modding. We recommend using `Sublime Text <http://www.sublimetext.com/>`_. It's full-featured and is free to use for non-commercial use.

Once that's installed, we'll setup the syntax highlighting for .ce files. To do this:
 * Navigate to mods/core/body/player.ce and open that file in Sublime Text.
 * With player.ce open, at the toolbar up top, click View => Syntax => Open all files with current extension as... => Python => Python.

Syntax highlighting should now be enabled for all .ce files. Next we want to add the Python code base to Sublime Text as a project:
 * Click Project => Add folder to project... and select Crea/mods
 * Now all of the directories and files will be conveniently accessible from the panel to the left.

`If you need more help using Sublime Text view the documentation provided here. <https://www.sublimetext.com/docs/2/>`_

