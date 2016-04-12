
.. _core-loading:

Core Loading
============

Sometimes you will wish to change logic in the core game code. This is possible through core loading.

To use core loading you must mirror the directory path starting with mods/mymod/coremod/.
Such as to overload something in mods/core/combat.py you will want to place your code in mods/mymod/coremod/combat.py.
Core loading can be used to modify both functions and classes.

The same function can be loaded multiple times from either the same mod or from multiple mods and the final function chains all of the loads.

.. note::

    Be sure to import the loads that you need!

.. code-block:: python

    from coremod import overload, preload, postload, overloader, preloader, postloader, overloadmethod, postloadmethod, postloadmethod

.. _core-overloading:

Core Overloading
-----------

To completely overwrite a function you can use 'overload' core loading.

.. code-block:: python

    @overload
    def calculateDamage(strength, defense, attackerLevel, target, power, attackType):
        '''Every hit is critical 9999 damage!'''
        return 9999

It is important to ensure the function name and parameters are the same as the core.
However, it is possible to provide a separate name for the function using 'overloader'.

.. code-block:: python

    @overloader('calculateDamage')
    def myCalculateDamage(strength, defense, attackerLevel, target, power, attackType):
        '''Every hit is critical 9999 damage!'''
        return 9999

Overloading a class method is possible by using 'overloadmethod'.

.. code-block:: python

    class ExampleClass(object):
        @overloadmethod
        def test(self, foo):
            pass

.. _core-preloading:

Preloading
----------

Preloading is very similar to overloading except that the original code is still executed **after**.

.. code-block:: python

    @preload
    def handlePlayerDeath(entity, clock):
        '''Drop all items on death.'''
        position = entity.getPosition()
        droppedSystem = entity.realm.dropped
        for index, bag in enumerate(entity.inventory.getBags()):
            if bag:
                for index, item in enumerate(bag.items):
                    if item:
                        droppedSystem.create(item, position, Vector(0, -6))
            bag.clear()

Similar to overloading it is important to have the function name correct but it can be different using 'preloader' the same way 'overloader' was used in the example above.
To preload a class method use 'preloadmethod'.

.. _core-postloading:

Postloading
-----------

Postloading is the same as preloading except the original code is executed **before**.

.. code-block:: python

    @postload
    def dropMonsterLoot(entity, remna, loot, canDropKey):
        '''Drop a candycane from all monsters.'''
        entity.realm.dropped(Item('candycane'), entity.getPosition(), Vector(0, -6))

Just like 'preloader' and 'preloadmethod' there are 'postloader' and 'postloadmethod' decorators.
