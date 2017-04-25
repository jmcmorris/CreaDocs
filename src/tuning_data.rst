
.. _tuning-data:

Tuning Data
===========

There is a great deal of data that drives Crea such as monster stats and the power of skills.
All of this data is stored in tuning files in the mods/core/tuning/ directory.
This helps make locating and changing values much easier.


.. _status-effect-tuning:

Status Effect Tuning
--------------------

All of the data pertaining to monsters are located in ``core.tuning.effect``.
Most status effect data only contains the name, icon and description.

.. code-block:: python

    POISON = AttrDict(
        NAME = "Poison",
        ICON = "mods/core/effect/poison.png",
        DESC = "PoisonDesc",
    )


.. _monster-tuning:

Monster Tuning
--------------

All of the data pertaining to monsters are located in ``core.tuning.monster``.
This includes a great deal of data including stats, attack powers, and loot.

.. code-block:: python

    OIL_SLIME = AttrDict(
        STATS=AttrDict(
            HP=30,
            SP=30,
            ATK=5,
            DEF=5,
            INT=5,
            MIND=5,
            AGI=5,
            LUCK=5,
        ),
        LEVEL_STATS=[
            AttrDict(level=1, HP=5, SP=2, ATK=1, DEF=3, INT=1, MIND=3, AGI=1, LUCK=0),
            AttrDict(level=6, HP=15, SP=2, ATK=2, DEF=3, INT=2, MIND=3, AGI=2, LUCK=0),
            AttrDict(level=11, HP=18, SP=3, ATK=3, DEF=4, INT=3, MIND=4, AGI=3, LUCK=0),
            AttrDict(level=16, HP=20, SP=3, ATK=4, DEF=5, INT=4, MIND=5, AGI=4, LUCK=0),
            AttrDict(level=21, HP=25, SP=4, ATK=4, DEF=6, INT=4, MIND=6, AGI=4, LUCK=0),
            AttrDict(level=26, HP=25, SP=4, ATK=5, DEF=7, INT=5, MIND=7, AGI=5, LUCK=0),
            AttrDict(level=31, HP=30, SP=5, ATK=5, DEF=8, INT=5, MIND=8, AGI=5, LUCK=0),
            AttrDict(level=36, HP=30, SP=5, ATK=6, DEF=9, INT=6, MIND=9, AGI=5, LUCK=0),
            AttrDict(level=41, HP=35, SP=6, ATK=6, DEF=10, INT=6, MIND=10, AGI=6, LUCK=0),
            AttrDict(level=46, HP=35, SP=6, ATK=7, DEF=10, INT=7, MIND=10, AGI=6, LUCK=0)
        ],
        MELEE_POWER=60,
        MELEE_POWER_LEVEL=2,
        BLOB_POWER=55,
        BLOB_POWER_LEVEL=2,
        BLOB_ATTACK_TYPE = AttackType.Ranged,
        MIN_LEVEL=1,
        WEIGHT = 100,
        EXPERIENCE_YIELD = 25,
        REMNA = RemnaType.Earth,
        BIOMES = ["Plains", "Desert", "Underground"],
        GROWL_SOUND = "mods/core/audio/sfx/monster/oil_slime_growl_[1-7].ogg",
        NIGHT_DETECTION_AREA = Rect(20, -14, 100, 40),
        ATTACK_RANGE = 40,
        LOOT = [
            ImbuableLoot("oil_clot", dropRates={1: 66, 2: 34}),
            ImbuableLoot("bone", dropRates={0: 65, 1: 35})
        ],
    )


.. _skill-tuning:

Skill Tuning
------------

All of the data pertaining to skills are located in ``core.tuning.skill``.
This contains data such as the skill name, cooldown times, TP cost to level and so on.
Below is an example of the tuning data for the Focus skill.

.. code-block:: python

    FOCUS = AttrDict(
        NAME = "Focus",
        DESCRIPTION = "FocusDesc",
        ICON = "mods/core/talent/arms/focus_skill_icon.png",
        UNLOCK_LEVELS = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46],
        LEVEL_COSTS = [350, 375, 375, 375, 400, 400, 400, 400, 450, 450],
        CAST_TIME = 800,
        CRITICAL_MODIFIERS = [100, 120, 120, 150, 150, 150, 200, 200, 200, 250],
        COOLDOWNS = [seconds(20), seconds(20), seconds(17), seconds(17), seconds(17), seconds(14), seconds(14), seconds(14), seconds(11), seconds(11)],
        SP_COSTS = [40, 35, 35, 35, 30, 30, 30, 25, 25, 25],
        TP_AMOUNT = 12,
        TP_CHANCE = 30,
        SOUND = "mods/core/audio/sfx/talent/arms/focus.ogg",
    )

The following bits of data are required for all skills:

NAME
    The name locale key of the skill to be :ref:`localized <creating-localizations>`.

DESCRIPTION
    The description locale key of the skill to be :ref:`localized <creating-localizations>`.

ICON
    The path to the icon that is used to represent the skill in the UI6.

UNLOCK_LEVELS
    The required level the associated talent must be in order to level up the skill.

LEVEL_COSTS
    The talent point (TP) cost to level up the skill for each level.
