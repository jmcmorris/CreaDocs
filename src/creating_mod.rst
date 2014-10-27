
Creating a Mod
==============

Open up the Crea/mods directory. Here, you'll find the core directory, as well as any other mods you've installed. The game engine checks here for any content that needs to be run. The base game located in core/ is actually, technically a mod of the game so feel free to use it as a reference point!


Directory Structure
-------------------

Files can be placed however you want inside a mod. However, there are a few files that are needed or are treated specially.
 * Crea/

   * mods/

     * your_mod/

       * info
       * preview.png
       * registration.py
       * coremod/

info
    The info file contains mod information such as title, description, and version number. This file must be in the `JSON Format <http://www.json.org/>`_.

preview.png
    preview.png does what it says. It provides a preview screenshot of what your mod adds and provides.

registration.py
    The game engine looks for this file specifically. It will call the ```register``` method when registering all mod packages.

coremod/
    Allows for modification of python code in the core package. Code placed here can inherit and overload the existing code base. 


Behavior of .ce Files
---------------------

Content Entity files (.ce) represent a piece of content within the game such as a monster or item like a sword or a piece of furntiure. It's actually a Python file that is treated differently by the game.

 * .ce files are loaded automatically on game startup.  
 * Imported functions can be called, but as a general rule, don't contain code.

   * The exception to this rule is customizing (or decorating for those of you that know Python).


Behavior of .py Files
---------------------

You'll want to encapsulate functions and logic for your .ce files in .py files. Python files (.py) are only run when called. Keeping logic separated is good for performance because it'll only be loaded when called.
