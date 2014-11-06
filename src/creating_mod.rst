
Creating a Mod
==============

Modding in Crea is all done in `Python <https://www.python.org/>`_; however,
you don't have to know Python to create simple content such as items or new
character customizations. When modding in Crea there are several file types to 
be aware of.

* *.ce*   - Content Entity file which represents a type of content such as a single monster or item (Python file treated specially by the game)
* *.py*   - Python file used for systems
* *.png*  - Image file used by the game
* *.scml* - `Spriter <http://www.brashmonkey.com/spriter.htm>`_ character file used for modular sprites


Possibilities
-------------

"Is it possible to mod ____?" - The answer is almost always yes. Here is a list
of some of the things you can mod.

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

Now that you've found the source code, you'll want to use a text editor while
modding. We recommend using `Sublime Text <http://www.sublimetext.com/>`_. It's
full-featured and is free to use for non-commercial use.

Once that's installed, we'll setup the syntax highlighting for .ce files. To do
this:

* Navigate to mods/core/body/player.ce and open that file in Sublime Text.
* With player.ce open, at the toolbar up top, click View => Syntax => Open all
  files with current extension as... => Python => Python.

Syntax highlighting should now be enabled for all .ce files. Next we want to add
the Python code base to Sublime Text as a project:

* Click Project => Add folder to project... and select Crea/mods
* Now all of the directories and files will be conveniently accessible from the
  panel to the left.

`If you need more help using Sublime Text view the documentation provided here. <https://www.sublimetext.com/docs/2/>`_


Directory Structure
-------------------

You know where the files are, and your text editor is all setup. Let's take a
look at the basic structure of a mod. Files can be placed however you want
inside a mod. However, there are a few files that are needed or are treated
specially.

* Crea/

  * mods/

    * your_mod/

      * __init__.py
      * info
      * preview.png
      * registration.py
      * coremod/

**Crea/**
    This is the root directory for Crea.

**mods/**
    This directory is where all mods are stored. Note that the core game
    directory is also located here. Feel free to use it as reference!

**your_mod/**
    Create a directory that suits the mod you're going to be creating. Be sure
    to follow the naming convention of all lower-case letter and underscores
    instead of spaces.

**info**
    The info file contains mod information that Steam Workshop uses. This file
    must be in the `JSON Format <http://www.json.org/>`_.

    * title: This field is a string that contains the title of your mod. Note
      that this will be displayed on the Workshop page as is.
    * author: This string should contain the name you want to display on the
      Steam Workshop page.
    * description: String field that describes briefly what your mod provides.
    * version: This is a float that Steam checks to make sure that any players
      subscribed to your mod have the latest version. Make sure to increment
      this value whenever you make changes.

**preview.png**
    This image file provides a preview screenshot of what your mod adds and
    provides. The Steam Workshop page that is generated for your mod will use
    this image.

**registration.py**
    The game engine looks for this file specifically. Packages listed here will
    have their ```register``` method called and let the game engine know that
    these packages need to be used.

    For most basic mods, this registration.py will look like this::
        
        def register():
            pass

**coremod/**
    Allows for modification of python code in the core package. Code placed here
    can inherit and overload the existing code base. 


Behavior of .ce Files
---------------------

Content Entity files (.ce) represent a piece of content within the game such as a
monster or item. It's actually a Python file that is treated differently by the game.

* .ce files are loaded automatically on game startup.  
* Imported functions can be called, but as a general rule, don't contain code.

  * The exception to this rule is customizing (or decorating for those of you that know Python).


Behavior of .py Files
---------------------

You'll want to encapsulate functions and game logic for your .ce files into .py
files. Python files (.py) are only run when called on. Keeping logic separated
is good for performance because it'll only be loaded when called.


Publishing your mod
-------------------

#. Make sure that everything in the info file is correct. The values you set in
   this file will be displayed on your mod's Steam Workshop page.
#. Make sure that you have an image file named preview.png. This image will be
   used as the main image for the mod's Steam Workshop page as well as in Crea's
   Community Hub.

   * Keep the image in a square resolution to avoid cropping.
   * You will be able to add more images to your page once the mod is uploaded.

#. Launch the game and click the wrench icon in the top right hand corner of the
   main menu. From here, you'll see a list of all mods you have installed. If
   your mod isn't there, go back and install it.
#. Next click "publish/update mod". You'll be taken to a screen listing all mods
   that are ready to be uploaded.
#. Click the mod you want to upload, and select the tags you want it to be
   listed under.
#. Hit "continue", and you'll be taken to a page with two buttons. 

   * The first is "Read & Agree". Clicking this button will take you to a page
     where you can sign the Steam Terms of Service for creating a workshop item.
   * After you finish this, close the popup.
   * Note that you will be asked to click this button everytime you upload a
     mod. If you've already signed the Terms of Service, just close the window.

#. Clicking "publish" will then attempt to upload your mod to the Steam Workshop. 
   It will immediately become public.
#. Uninstall your mod and subscribe to freshly uploaded Steam Workshop version
   and test it! 
   * If something isn't working as you intended, head to the mod's workshop page
     and hide the mod. You can do this by clicking "Change visibility" and set
     it to hidden from the "Owner Controls" in the right side bar.
   * Note that updating the mod will automatically set your mod to visible again.
#. Add more screenshots and fill any other information you'd like to display
   from the "Owner Controls".
