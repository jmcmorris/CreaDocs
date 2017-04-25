
.. _creating-monsters:

Creating Monsters
=================

Creating new monsters is much more involved than most other content and consequently knowing the :ref:`basics of creating content <basic-items>` will go a long ways.
Getting started we'll want to create a new folder inside of the mods/mymod/monster/ directory and in that new subfolder create a new .ce file so it looks like mods/mymod/monster/gold_slime/gold_slime.ce.
Even though monsters are more complex they still have their own :ref:`content template <content-template>` to help simplify the creation.

The ``Monster`` template has several parameters which you can see below.

.. py:function:: Monster(name, *, tuning=None, isPersistent=False, weight=0, isParagon=False, layer=Layer.Active, placementType=MonsterPlacementType.OnGround, biomes=[], spawnOffset=Vector())

    Sets up the content entity data of a Monster. The majority of this data can come from the provided tuning data.

    :param str name: The name of the monster. This should be the key used for :ref:`localizations <creating-localizations>`.
    :param AttrDict tuning: The tuning data for the monster.
    :param bool isPersistent: Whether the monster should persist between play sessions.
    :param int weight: The frequency this monster should appear in biomes relative to other monsters weights.
    :param bool isParagon: Whether this monster is considered a paragon and should be treated as such.
    :param Layer layer: The layer this monster should be placed on when created.
    :param MonsterPlacementType placementType: Where the monster should be placed - ground, air, water, etc.
    :param biomes: A list of the biomes the monster can spawn in.
    :type biomes: list of str
    :param Vector spawnOffset: The offset of the monster relative to the spawner it spawns from.
    :param bool hostile: Whether the monster should be treated as a monster or an animal.
    :param kwargs: Keyword argument list that will be passed to the main template class.

The content file contains the standard components such as ``hasPhysics`` and ``animations``.
In addition, we have to provide information and logic for the monster's attacks as well as the rest of the monster's AI.

Monster Attacks
---------------

New monster attacks can be added by through the template's ``Monster.attack()``.
This sets up a ``core.template.monster.MonsterAttack`` with the provided parameters.
Afterwards ``MonsterAttack.customize`` class decorator can be used to finish creating the attack.
The parameters provided to ``Monster.attack()`` are set as class attributes on the customized class.
Most of these are to change default class ``core.monster.MonsterMeleeAttack`` attributes that most attacks derive from.
With this customized class you can override any functions that ``core.monster.MonsterMeleeAttack`` has to provide your own custom logic.
In the example below the ``BasicOrtomiAttack`` overrides ``core.monster.MonsterMeleeAttack.perform()`` and ``handleTimeStep()``.

.. note::

   Whenever using callbacks for delayed events be sure to ensure the monster is still alive using ``core.monster.MonsterMeleeAttack.shouldStopAttack()``.

.. code-block:: python

    basicAttack = monster.attack(
        hitFrames = attack.indices(3, 4, 5, 6),
        power = MonsterTuning.ORTOMI.MELEE_POWER,
        powerLevel = MonsterTuning.ORTOMI.MELEE_POWER_LEVEL,
        detectionArea = Rect(0, -3, 32, 24),
        cooldownTime = 700,
        recoverTime = 900,
        sound = "mods/core/audio/sfx/monster/ortomi_bite.ogg",
        soundDelay = 300
    )


    @basicAttack.customize
    class BasicOrtomiAttack(MonsterMeleeAttack):
        def perform(self, monster):
            MonsterMeleeAttack.perform(self, monster)
            self.jumped = False

        def handleTimeStep(self, physics, frameTime):
            isFinished = MonsterMeleeAttack.handleTimeStep(self, physics, frameTime)
            if not self.jumped and self.monster.entity.animation.getPlayTime() >= 600:
                direction = -1 if self.monster.entity.render.getFlipX() else 1
                force = Vector(5.0 * direction, -1.5)
                physics.applyForce(force)
                self.jumped = True
            return isFinished


Below are the full details of the ``core.monster.MonsterMeleeAttack`` class.

.. py:class:: MonsterMeleeAttack

    .. attribute:: hitFrames = []

    .. attribute:: power

        Power of the attack. Defaults to 0.

    .. attribute:: powerLevel

        Amount of power to add multiplied by the monster's level. Defaults to 0.

    .. attribute:: statusEffect

        The status effect to apply to any hit targets. Defaults to None.

    .. attribute:: attackType

        Defaults to AttackType.Melee.

    .. attribute:: damageType

        Defaults to DamageType.Physical.

    .. attribute:: detectionArea

        The area around the monster that this attack is considered to be in range. Defaults to Rect().

    .. attribute:: cooldownTime

        Amount of time (ms) elapsed after for this attack to be performed again. Defaults to 0.

    .. attribute:: recoverTime

        Amount of time (ms) the monster requires to recover after performing the attack. Defaults to 0.

    .. attribute:: animation

        Defaults to "attack".

    .. attribute:: sound

        Sound to play when performing the attack. Defaults to "".

    .. attribute:: soundDelay

        Amount of time (ms) to delay playing the sound. Defaults to 0.

    .. attribute:: isPhysical

        Defaults to True.


    .. method:: getPower(level)

        Calculates the final power of the attack.

        :param int level: The current level of the monster performing the attack.
        :returns: The power of the attack.
        :rtype: int

    .. method:: update(frameTime)

        Called every frame to update the attack. This is typically used to update timers and the likes.

        :param int frameTime: The amount of time (ms) elapsed since the last update.


    .. method:: shouldPerform(monster)

        Determines whether or not this attack should be performed. Default logic checks to see if any enemies are within range.

        :param BaseMonster monster: The instance of the monster that would be performing the attack.
        :returns: Whether this attack should be performed or not.
        :rtype: bool


    .. method:: inRange(monster)

        Checks if there are any enemies within the defined range of this attack.

        :param BaseMonster monster: The instance of the monster that would be performing the attack.
        :returns: Whether enemies are within range or not.
        :rtype: bool

    .. method:: perform(monster, animation='')

        Called when the attack is being performed by the monster.

        :param BaseMonster monster: The instance of the monster that would be performing the attack.
        :param str animation: The name of the animation that should be played for this attack.


    .. method:: updateAttackTime(physics, frameTime)

        Updates the amount of time the attack has been being performed and will play the attack's sound effect after the specified sound delay.

        :param PhysicsComponent physics: The physics of the monster entity performing the attack.
        :param int frameTime: The amount of time (ms) elapsed since the last update.


    .. method:: handleTimeStep(physics, frameTime)

        Called every physics step at a fixed time and determining when the attack is complete.

        :param PhysicsComponent physics: The physics of the monster entity performing the attack.
        :param int frameTime: The amount of time (ms) elapsed since the last update.
        :returns: Whether the attack animation is complete or not.
        :rtype: bool

    .. method:: handleIsAlive(entity, wasAlive, isAlive)

        Used to watch is the monster's alive state changes. If so then it disconnects the timestep listener allowing the attack to discontinue.

        :param Entity entity: The entity of the monster.
        :param bool wasAlive: Whether the monster was alive before the state changed or not.
        :param bool isAlive: Whether the monster is currently alive or not.

    .. method:: checkHit()

        Attempts to hit any enemies within the attack range.

        :returns: The enemies that were hit by the attack.
        :rtype: list of Entity


    .. method:: handleRecoverTimeStep(physics, frameTime)

        Responsible for updating the recovery timer while the monster is recovering from performing this attack. It automatically stops once the recovery timer has expired.

        :param PhysicsComponent physics: The physics of the monster entity performing the attack.
        :param int frameTime: The amount of time (ms) elapsed since the last update.

    .. method:: shouldStopAttack()

        Determines if this attack should be discontinued based off of the monsters current state. This should be called immediately for any callbacks. Especially for those that have some side-effect such as creating an entity.

        :returns: Whether the monster should stop the attack or not.
        :rtype: bool

    .. method:: onFinish()

        Called when the attack has finished being performed.

    .. method:: cleanup()

        Called when the attack has fully concluded including recovery.



Monster Core
------------

All of the logic that drives the monster behavior lives within the monster core.
This monster core is a python instance that derives from ``core.monster.BaseMonster`` which is stored inside of the :ref:`MonsterComponent` at ``entity.monster.core``.
There is a great deal of default base logic that can help simplify the creation of more basic monsters.
Even with more simple monsters you will often want to change its behavior some.

The monsters' logic is driven by a state machine. At any given moment a monster can only be doing one thing.
While in one state that state can determine that the monster should switch to another state.
Such as when the monster is roaming about and spots a player it can switch from the roaming state to the hostile state.
When changing to a state through :py:meth:`BaseMonster.changeState` that state's initializer is called. Afterwards, every frame the state updater is called while updating the monster until the monster changes state once more.

Both state initializers and handlers are split between daytime and nighttime.
The current state initializers can be found in :py:attr:`BaseMonster.initializers` and the handlers can be found in :py:attr:`BaseMonster.handlers`.
When the time of day changes the current set of initializers and handlers are swapped out for the others.
These are all in :py:attr:`BaseMonster.dayInitializers`, :py:attr:`BaseMonster.dayHandlers`, :py:attr:`BaseMonster.nightInitializers` and :py:attr:`BaseMonster.nightHandlers`.
After creation the initializers and handlers can be changed by using :py:meth:`BaseMonster.updateInitializer` and :py:meth:`BaseMonster.updateHandler` respectively.

All initializers and handlers are expected to have the following signatures.

.. py:func:: stateInitializer(monster)

    :param BaseMonster monster: The instance of the monster that is changing state.


.. py:func:: stateHandler(monster, frameTime)

    :param BaseMonster monster: The instance of the monster that is in this current state.
    :param int frameTime: The amount of time (ms) elapsed since the last update.


.. py:class:: BaseMonster


    .. method:: __init__(entity, dayInitializers=None, dayHandlers=None, nightInitializers=None, nightHandlers=None)


    .. method:: setup()

        Called after the monster has been fully initialized and added to the world. Allows for additional setup after creation.

    .. method:: changeState(state)

        Called when the monster's state is being changed. State changes are disallowed when the monster is in MonsterState.Death.

    .. method:: update(frameTime)

        Called every frame updating the monster. This includes updating the monster's actions checking to see if they should be performed.

        :param int frameTime: The amount of time (ms) elapsed since the last update.

    .. method:: updateInitializer(state, callback)

        Changes the provided state's initializer to the provided callback. This changes occurs for both day and night initializers.

        :param MonsterState state: The state to change the initializer for.
        :param callback: The initializer callback using the signature specified with :py:func:`stateInitializer`.

    .. method:: updateHandler(state, callback)

        Changes the provided state's handler to the provided callback. This changes occurs for both day and night handlers.

        :param MonsterState state: The state to change the handler for.
        :param callback: The handler callback using the signature specified with :py:func:`stateHandler`.

    .. method:: attachToSpawner(spawner)

        Attaches the monster to the specified spawner. This results in the monster becoming hostile towards any players that attack the spawner.

        :param Entity spawner: The entity of the spawner to attach the monster to.


    .. method:: guardPoint(point)

        Changes the monster's roaming state to patrol the specified area not straying too far from it.

        :param Vector point: The position the monster should guard.


    .. method:: guardSpawner(spawner)

        Changes the monster's roaming state to patrol around the spawner and not stray too far from it.

        :param Entity spawner: The spawner the monster should guard.


    .. method:: performAction(action)

        Sets the provided action as the action the monster is currently performing and changes the monster's state to ``MonsterState.Action``.

        :param action: The action the monster should perform.


    .. method:: attemptAction()

        All available actions are checked to see if any should be performed. If any are found then the action is performed.

    .. method:: surveyArea()

        Checks the nearby area using ``detectionArea`` to see if there are any enemies nearby that the monster should become hostile towards. If an enemy is found the the monster's state is changed to ``MonsterState.Hostile``.

    .. method:: getLifePercentage()

        Retrieves the percentage of health the monster is at.

        :returns: The health percentage ranging from 0-100.
        :rtype: int

    .. method:: addAffix(affixKey)

        Adds the affix belonging to the given key to the monster.

        :param str affixKey: The key that the desired affix is registered under.

    .. method:: playAnimation(name, animation=None)

        Plays the specified animation on the monster.

        :param str name: The name of the animation to play.
        :param AnimationComponent animation: The animation component belonging to the monster. If not provided then it will be automatically retrieved.

    .. method:: idle(animation=None)

        Plays the 'idle' animation on the monster if it has it.

        :param AnimationComponent animation: The animation component belonging to the monster. If not provided then it will be automatically retrieved.

    .. method:: move(animation=None)

        Plays the 'move' animation on the monster if it has it.

        :param AnimationComponent animation: The animation component belonging to the monster. If not provided then it will be automatically retrieved.

    .. method:: jump(animation=None)

        Plays the 'jump' animation on the monster if it has it.

        :param AnimationComponent animation: The animation component belonging to the monster. If not provided then it will be automatically retrieved.

    .. method:: fall(animation=None)

        Plays the 'fall' animation on the monster if it has it.

        :param AnimationComponent animation: The animation component belonging to the monster. If not provided then it will be automatically retrieved.

    .. method:: land(animation=None)

        Plays the 'land' animation on the monster if it has it.

        :param AnimationComponent animation: The animation component belonging to the monster. If not provided then it will be automatically retrieved.

    .. method:: death(animation=None)

        Plays the 'death' animation on the monster if it has it.

        :param AnimationComponent animation: The animation component belonging to the monster. If not provided then it will be automatically retrieved.


Paragons
--------

Paragons are elite versions of monsters that are given extra abilities and prove to be a greater challenge.
Paragon monsters derive from ``core.monster.ParagonMonster`` which itself inherits from ``core.monster.BaseMonster``.
Paragon monsters are automatically given the extra abilities known as affixes.
Unlike other monsters though, Paragon monsters persist between play sessions keeping their stats and affixes.

New affixes can be registered to the monster system via :py:meth:`MonsterSystem.registerAffix` which should be done during :ref:`mod registration <mod-registration>`.
Whenever an affix is being added to a monster a new instance of that affix is created.
The affix's constructor is responsible for hooking up the affix to the monster in whichever way it needs.
Some affixes act as a new attack while some simply use a game timer.
The affix constructor is expected to have the following signature.

.. py:func:: affix(entity, monster)

    :param Entity entity: The entity representing the monster that this affix is being added to.
    :param BaseMonster monster: The instance of the monster that this affix is being added to.

Animals
-------

Animals are basically monsters with a few behavioral tweaks.
Namely the creature is made to be passive and not have any attacks.
Additionally 'hostile = False' should be provided to the Monster template.
Animals are treated differently by the conflict system in that they spawn more often during the day and in less hostile areas.


Monster Example
---------------

Below is a full example of a monster's content file.

.. code-block:: python

    from core.monster import BaseMonster, MonsterMeleeAttack

    from core.template.animation import Frame, Frames
    from core.template.monster import Monster
    from core.tuning.monster import MonsterTuning

    from siege.util import PixelVector, Rect, Vector


    monster = Monster(name="Ortomi", tuning=MonsterTuning.ORTOMI)

    monster.hasPhysics(
        body = Rect(-7, -17, 13, 35),
        friction = Vector(0.1, 0),
        groundFriction = Vector(0.1, 0)
    )

    lick = monster.getSpriteFrames(
        frames = [
            Frame(122, 226),
            Frame(122, 170),
            Frame(122, 114),
            Frame(122, 58),
            Frame(122, 2),
            Frame(2, 226),
            Frame(2, 170),
            Frame(2, 114),
            Frame(2, 58),
            Frame(2, 2),
        ],
        size = PixelVector(120, 56),
        origin = PixelVector(29, 40)
    )

    run = monster.getSpriteFrames(
        frames = [
            Frame(242, 225),
            Frame(242, 182),
            Frame(242, 139),
            Frame(242, 96),
            Frame(242, 53),
        ],
        size = PixelVector(40, 43),
        origin = PixelVector(25, 26)
    )

    death = monster.getSpriteFrames(Frame(282, 135, size=(39, 41), origin=(29, 24)))

    jump = monster.getSpriteFrames(
        frames = [
            Frame(282, 53),
            Frame(267, 268),
        ],
        size = PixelVector(39, 41),
        origin = PixelVector(29, 21)
    )

    attack = monster.getSpriteFrames(
        frames = [
            Frame(242, 2),
            Frame(214, 282),
            Frame(161, 282),
            Frame(108, 282),
            Frame(55, 282),
            Frame(2, 282),
        ],
        size = PixelVector(53, 51),
        origin = PixelVector(30, 34)
    )

    idle = monster.getSpriteFrames(Frame(282, 94, size=(39, 41), origin=(29, 24)))

    monster.animations(
        start = 'idle',
        idle = Frames(idle()),
        move = Frames(run(), time=100),
        jump = Frames(jump(), time=100),
        fall = Frames(jump(2), time=100),
        attack = (
            Frames(attack(1), time=150),
            Frames(attack(2), time=300),
            Frames(attack(3, 4, 5, 6), time=100)
        ),
        lick = (
            Frames(lick(1, 2), time=300),
            Frames(lick(3, 4, 5, 6, 7, 8, 4), time=100),
            Frames(lick(9, 10, 9), time=60),
        ),
        death = Frames(idle() + death() + idle() + death(), time=200),
        disableLooping = ['idle', 'attack', 'jump', 'death', 'lick']
    )


    lickAttack = monster.attack(
        hitFrames = lick.indices(3, 4, 5, 6, 7, 8),
        power = MonsterTuning.ORTOMI.LICK_POWER,
        powerLevel = MonsterTuning.ORTOMI.LICK_POWER_LEVEL,
        detectionArea = Rect(0, -14, 50, 40),
        recoverTime = 850,
        cooldownTime = 1600,
        sound = "mods/core/audio/sfx/monster/ortomi_lick.ogg",
    )

    basicAttack = monster.attack(
        hitFrames = attack.indices(3, 4, 5, 6),
        power = MonsterTuning.ORTOMI.MELEE_POWER,
        powerLevel = MonsterTuning.ORTOMI.MELEE_POWER_LEVEL,
        detectionArea = Rect(0, -3, 32, 24),
        cooldownTime = 700,
        recoverTime = 900,
        sound = "mods/core/audio/sfx/monster/ortomi_bite.ogg",
        soundDelay = 300
    )


    @lickAttack.customize
    class LickAttack(MonsterMeleeAttack):
        def perform(self, monster, animation='lick'):
            MonsterMeleeAttack.perform(self, monster, animation)


    @basicAttack.customize
    class BasicOrtomiAttack(MonsterMeleeAttack):
        def perform(self, monster):
            MonsterMeleeAttack.perform(self, monster)
            self.jumped = False

        def handleTimeStep(self, physics, frameTime):
            isFinished = MonsterMeleeAttack.handleTimeStep(self, physics, frameTime)
            if not self.jumped and self.monster.entity.animation.getPlayTime() >= 600:
                direction = -1 if self.monster.entity.render.getFlipX() else 1
                force = Vector(5.0 * direction, -1.5)
                physics.applyForce(force)
                self.jumped = True
            return isFinished


    @monster.customize
    class OrtomiMonster(BaseMonster):
        def __init__(self, entity, component):
            BaseMonster.__init__(self, entity)
            self.actions.append(BasicOrtomiAttack())
            self.actions.append(LickAttack())

        def update(self, frameTime):
            BaseMonster.update(self, frameTime)

        @staticmethod
        def create(entity, component):
            return OrtomiMonster(entity, component)
