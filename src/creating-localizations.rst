
.. _creating-localizations:

Creating Localizations
======================

Localization Setup
------------------

Creating new localizations in Crea is easy. For a pure localization mod all you need is a locale file in mods/mymod/locale/. See :ref:`Mod Template <mod-template>`.

The locale file you do create should use the correct `language code <http://www.science.co.il/Language/Locale-codes.asp>`_ such as for Japanese the file would be ja.locale.

Localization File
-----------------

The locale file holds all of the game's text. While the file is huge there are only a few elements truly at play.

**Name**
    The name of the locale that will show in the UI when selecting the language.

**font()**
    There are a few fonts that display text outside of the UI. The default fonts do not support all languages so it may be necessary to change these.
    The first paramater is the font key and the second is the actual path.

**locale()**
    This provides a localization for a given keyword such as in the example below you'll see "OilClot" is localized to "Oil Clot" in English.
    Items can have a suffix "Desc" or "Flavor" appended to its keyword to provide the description or flavor text.

**associate()**
    Some items need to share the description or flavor text of other items and associate makes that easy.
    Again, the keyword is first then second is the keyword to copy the description/flavor from and lastly is the localization for the keyword.


.. code-block:: python

    # -*- coding: utf-8 -*-

    name = "English"

    font("text", "mods/core/ui/fonts/Bitter/Bitter-Regular.ttf")
    font("nameplate", "mods/core/ui/fonts/Ubuntu/Ubuntu-B.ttf")
    font("number", "mods/core/ui/fonts/Ubuntu/Ubuntu-B.ttf")

    locale("OilClot", "Oil Clot")
    locale("OilClotDesc", "A large dollop of oil. Useful for crafting.")
    locale("OilClotFlavor", "Oil slimes are reviled creatures, but their oil provides the basis of many everyday items.")
    associate("RefinedOilClot", "OilClot", "Refined Oil Clot")
    associate("PremiumOilClot", "OilClot", "Premium Oil Clot")
    associate("PurifiedOilClot", "OilClot", "Purified Oil Clot")
    associate("ParagonOilClot", "OilClot", "Paragon Oil Clot")
