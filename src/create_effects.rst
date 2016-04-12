
.. _status-effects:

Status Effects
==============

Status effects can be applied to any entity that has a :mod:`EffectsComponent` - all players and monsters have one.
Status effects can have custom logic behind them enabling a wide range of options.

Applying Effects
----------------

Applying a status effect is fairly simple and is done using :mod:`EffectsComponent.add`.

.. code-block:: python

    entity.effects.add(EffectTuning.BURN, level=1, duration=seconds(1), source=player.entity)


Removing Effects
----------------

Even simpler than adding, removing a status effect is done using :mod:`EffectsComponent.remove`.

.. code-block:: python

    entity.effects.remove(EffectTuning.BURN)


Creating Effects
----------------

New status effects can be added by creating a new .py file in the effect folder.

Below you can find an example with details.

.. note::

    Tons of additional examples can be found in mods/core/effect/ including registration in mods/core/effect/registration.py and mods/core/effect/__init__.py.

.. code-block:: python

    from core.effect.base import EffectBase
    from core.tuning.effect import EffectTuning
    from siege import game


    class ExampleEffect(EffectBase):
        TUNING = EffectTuning.EXAMPLE_EFFECT

        def __init__(self, owner, level, duration, source):
            '''Constructor is called when the status effect is being added to an entity.
            'self' object will live at least until it has been removed.
            :param owner: The Entity that has this status effect being applied to.
            :param level: The level of this status effect.
            :param duration: The duration (ms) this status effect will live for.
            :param source: The source that caused this status effect to be applied to owner.
            '''

            super(ExampleEffect, self).__init__(owner)

        def onRemove(self, owner):
            '''Called when this status effect is being removed.
            This is optional can be completely left out.

            :param owner: The Entity that this status effect was on.
            '''
            pass

        def read(self, stream):
            '''Called when loading the entity with this status effect.
            This is optional can be completely left out.

            :param stream: The DataStream that should be read from.
            '''
            pass

        def write(self, stream):
            '''Called when saving the entity with this status effect. Used to save any necessary data along with the entity.
            This is optional can be completely left out.

            :param stream: The DataStream that should be written to.
            '''
            pass

        @staticmethod
        def register():
            '''Registers this status effect with the EffectsSystem.'''
            game.effects.register(ExampleEffect.TUNING.NAME, ExampleEffect)
