
.. _creating-mods:

Creating Mods
=============

.. _mod-template:

Mod Template
------------

You can use this premade mod template anytime you wish to create a new mod.
It contains the info file, registration.py and a basic folder layout. Feel free
to delete any unused folders and registration.py if unused.

.. note::

    Be sure to update the info file!

Remember that any folders with .py files need to have a __init__.py to make it a `Python package <https://docs.python.org/2/tutorial/modules.html#packages>`_ and importable.

:download:`Download Mod Template <_static/crea_mod_template.zip>`


.. _mod-publishing:

Mod Publishing
--------------

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
   * If something isn't working as you intended, head to the mod's workshop page and hide the mod. You can do this by clicking "Change visibility" and set it to hidden from the "Owner Controls" in the right side bar.
   * Note that updating the mod will automatically set your mod to visible again.
#. Add more screenshots and fill any other information you'd like to display
   from the "Owner Controls".
