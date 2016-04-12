
.. _engine-overview:

Engine Overview
===============

Understanding Crea's engine is not necessary for simple mods but can prove to be instrumental for more advanced mods.
There are several elements at work in the engine however the most fundamental aspect of it is that it's a component-based engine.

A component-based engine means that there is a single :mod:`Entity` that is composed of many :mod:`Component`.
Such as a Broadsword is an Entity that consists of a :mod:`ItemComponent`, :mod:`WeaponComponent` and :mod:`EquipmentComponent`.
Generally any combination of components can be added to a single Entity.

While components usually contain data and sometimes logic, each :mod:`Subsystem` is responsible for a single type of component and keeping them together.
Such as the :mod:`CraftSystem` is responsible for creating each :mod:`CraftComponent` for every item and tracks all of these components for easy access.

.. code-block:: python

    game.craft.getComponents()

All Subsystems are registered with :mod:`Game` and are accessable at anytime using its name as attribute.

Subsystems are directly associated with one or more components but a normal system is standalone. A system is used to track grouped logic and data
over many frames. Just like Subsystems, Systems are updated every frame and can be easily accessed at anytime.

.. _entity-creation:

Entity Creation
---------------

Every :mod:`Entity` type is represented by a .ce (Crea Entity) file. When Crea loads it finds all .ce files and creates a stamp for each one which is used in the future anytime a new entity needs to be created. Such as a Oil Slime entity stamp is created so that anytime a new Oil Slime is spawned it is based off of this stamp. Along with the stamp is a vanilla :ref:`content-entity` for each type which makes it easy to query information about an entity without having to create a new one.

The :mod:`EntityManager` is responsible for creating an maintaining all entities. Use :py:func:`EntityManager.create` to create new entities.

.. code-block:: python

    oilSlimeEntity = game.entity.create('oil_slime')
    # When an entity is no longer needed it can be destroyed directly
    oilSlimeEntity.destroy()

.. note::

    Remember to fully setup the entity with a position and realm!

.. code-block:: python

    from siege.world import World
    from siege.world.realm import Layer

    world = World.get()
    player = world.getPlayer()
    oilSlimeEntity = game.entity.create('oil_slime')
    # Set the Oil Slime directly above the player
    oilSlimeEntity.setInitialPosition(player.entity.getPosition() + Vector(0, -30))
    world.move(oilSlimeEntity, player.entity.realm, Layer.Active)

.. _content-entity:

Content Entities
----------------

A Content Entity is a vanilla entity that was created directly from its stamp and is unmodified making it easy to query information about an entity type.
Every Content Entity has a id set to 0 since they are not unique. It is possible to query any entity if it is a content entity with :py:func:`Entity.isContentEntity`.

.. code-block:: python

    entity.isContentEntity()

A Content Entity can be retrieved at anytime through :py:attr:`Content.entity`.

.. code-block:: python

    lumberContent = game.content.get('lumber')  # Get lumber content
    lumberContent.entity.item.sellPrice  # Get lumber sell price through its Content Entity

.. note::

    You should only ever query information from Content Entities!


.. _creating-components:

Creating Components
-------------------

It is entirely possible to create a new Component type and use it in your own entities. Start with creating a .py file in mods/mymod/component/. Here is an example
which is thoroughly commented. See the documentation for :mod:`Component` and :mod:`ComponentDefinition` for full details on the classes including all functions that can be overridden.

.. code-block:: python
    :linenos:

    from siege import game
    from siege.component import Component, ComponentDefinition, ComponentFactory


    class Example(ComponentDefinition):
        def __init__(self):
            ComponentDefinition.__init__(self)
            # Any amount of attributes containing data can be used here
            self.data = {}
            # Freeze this so that no more attributes can be set on it help prevent any errors
            self.freeze()

        def getType(self):
            '''Return the type of component this definition is associated with.'''
            return ExampleComponent.TYPE


    class ExampleComponent(Component):
        TYPE = "example"  # The type of the component
        CID = 0  # The Content ID which is automatically assigned during registration
        VERSION = 1  # The current version of this component. This should be incremented when the data in read()/write() changes.

        def __init__(self, definition):
            Component.__init__(self)
            # Transfer over any data we need from the definition (Example instance)
            self.data = definition.data
            self.freeze()

        def getData(self, key):
            # Any number of methods can be defined and used in a Component
            return self.data[key]

        @staticmethod
        def factory(entity, componentType, definition):
            # A Component can exist without its own Subsystem. It is then registered to a generic 'BasicSystem'.
            # When this is the case Component assumes the responsibility of creating itself and assigning itself to the entity.

            if entity.isContentEntity():
                # Set component to None here so that the BasicSystem does not manage the component for a Content Entity
                entity.add(ExampleComponent(definition))
                component = None
            else:
                component = ExampleComponent(definition)
                entity.add(component)
            return component

        @staticmethod
        def register():
            # Request a unique CID which is used internally for several things such as in multiplayer
            ExampleComponent.CID = game.entity.requestCid(ExampleComponent.TYPE, Example)
            # Next register the component with the engine and provide a factory from which components will be created
            # NOTE: This is only needed if the Component does not have a corresponding Subsystem. If it does then the Subsystem registration takes this responsibility.
            game.registerComponent(ExampleComponent.TYPE, ComponentFactory.create(ExampleComponent.factory))


You'll notice on line 5 the :py:class:`Example` class derives from :mod:`ComponentDefinition`.
This is the stamp part that is used in .ce files to hold the data until an actual :py:class:`ExampleComponent` is created through :py:attr:`ExampleComponent.factory`.
The interface for a ComponentDefinition should be kept simple since it is directly used the most.

Using an example from core, we have mods/core/component/imbue.py for the :py:class:`ImbueComponent` which is responsible for tracking the results for imbuable items.
You will notice :py:class:`ImbueComponent` only contains static data so it does not need :py:func:`ImbueComponent.pack`, :py:func:`ImbueComponent.unpack`, :py:func:`ImbueComponent.read`, or :py:func:`ImbueComponent.write`.
For more examples be sure to check out the mods/core/component/ directory.

.. code-block:: python
    :linenos:

    from core.tuning import RemnaType

    from siege import game
    from siege.component import Component, ComponentDefinition, ComponentFactory


    class Imbue(ComponentDefinition):
        def __init__(self):
            ComponentDefinition.__init__(self)
            self.remnaType = RemnaType.All
            self.results = {}
            self.freeze()

        def getType(self):
            return ImbueComponent.TYPE


    class ImbueComponent(Component):
        TYPE = "imbue"
        CID = 0
        VERSION = 1

        def __init__(self, definition):
            Component.__init__(self)
            self.remnaType = definition.remnaType
            self.results = definition.results
            self.freeze()

        def isCompatible(self, entity):
            remna = entity.remna
            return bool(self.remnaType & remna.element) and remna.tier in self.results

        def getContent(self, tier):
            return game.content.get(self.results[tier])

        @staticmethod
        def factory(entity, componentType, definition):
            if entity.isContentEntity():
                entity.add(ImbueComponent(definition))
                # Set component to None here so that the BasicSystem does not manage the component for a Content Entity
                component = None
            else:
                component = ImbueComponent(definition)
                entity.add(component)
            return component

        @staticmethod
        def register():
            ImbueComponent.CID = game.entity.requestCid(ImbueComponent.TYPE, Imbue)
            game.registerComponent(ImbueComponent.TYPE, ComponentFactory.create(ImbueComponent.factory))


.. _creating-subsystems:

Creating Subsystems
-------------------

For some new components you will also want to create a new class:`Subsystem` to manage the component. Below is an example subsystem with comments.
See the documentation for :mod:`SubSystem` for full details on the class including all functions that can be overridden.

.. code-block:: python

    from mymod.component.example import ExampleComponent

    from siege import game
    from siege.subsystem import Subsystem


    class ExampleSystem(Subsystem):
        NAME = "example"

        def getName(self):
            return self.NAME

        def __init__(self):
            Subsystem.__init__(self)
            self.components = []
            # Freeze the subsystem to prevent additional attributes being accidentally added
            self.freeze()

        def create(self, entity, type, definition):
            # When providing a subsystem for a component it becomes responsible for creating new components
            # This means that the component does not need a factory method
            component = ExampleComponent(definition)
            self.components.append(component)
            entity.add(component)

        def add(self, entity):
            # Add an entity that already has the component created
            if entity.has(ExampleComponent.CID):
                self.components.append(entity.example)

        def remove(self, entity):
            # Remove an entity/component from being tracked by this subsystem
            try:
                del self.components[self.components.index(entity.example)]
            except (AttributeError, ValueError):
                pass

        @staticmethod
        def register():
            # Register the subsystem with Game
            game.registerSubsystem(ExampleSystem(), ExampleSystem.NAME, ExampleComponent.TYPE)


For more examples see mods/core/system/ and look for classes that inherent from :mod:`Subsystem`.

.. _creating-systems:

Creating Systems
----------------

Sometimes you will need a system to manage data and perform logic every frame but not be responsible for a :mod:`Component`.
This is possible by registering a simple system with :mod:`Game`. Below is an example system.

.. code-block:: python

    from siege import game


    class ExampleSystem(object):
        NAME = "example"

        def getName(self):
            '''This is a required method.'''
            return self.NAME

        def __init__(self):
            pass

        def update(self, frameTime):
            '''Called every frame.
            :param frameTime: The amount of time (ms) passed since the last frame.
            '''
            pass

        @staticmethod
        def register(world):
            '''Registers this System to Game making it accessable through game.example.'''
            game.registerSystem(ExampleSystem.NAME, ExampleSystem())

        @staticmethod
        def unregister(world):
            '''Unregisters this System from Game.'''
            if game.hasSystem(ExampleSystem.NAME):
                game.unregisterSystem(ExampleSystem.NAME)

For more examples see mods/core/system/ and look for classes that are registered using :py:func:`Game.registerSystem`.
