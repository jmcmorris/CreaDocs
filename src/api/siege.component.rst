.. _siege.component:

siege.component
==================

AxisType
-----------------------------------
.. class:: AxisType

   

   .. data:: AXIS_BACKWALL = siege.component.AxisType.AXIS_BACKWALL

   .. data:: AXIS_CEILING = siege.component.AxisType.AXIS_CEILING

   .. data:: AXIS_FLOOR = siege.component.AxisType.AXIS_FLOOR

   .. data:: AXIS_LEFT = siege.component.AxisType.AXIS_LEFT

   .. data:: AXIS_NONE = siege.component.AxisType.AXIS_NONE

   .. data:: AXIS_RIGHT = siege.component.AxisType.AXIS_RIGHT

   .. data:: AXIS_WALL = siege.component.AxisType.AXIS_WALL

CombatStatus
-----------------------------------
.. class:: CombatStatus

   

   .. data:: Attacking = siege.component.CombatStatus.Attacking

   .. data:: Casting = siege.component.CombatStatus.Casting

   .. data:: Dead = siege.component.CombatStatus.Dead

   .. data:: Defending = siege.component.CombatStatus.Defending

   .. data:: Dodging = siege.component.CombatStatus.Dodging

   .. data:: Idle = siege.component.CombatStatus.Idle

   .. data:: Using = siege.component.CombatStatus.Using

CombatTeam
-----------------------------------
.. class:: CombatTeam

   

   .. data:: ALPHA = siege.component.CombatTeam.ALPHA

   .. data:: DELTA = siege.component.CombatTeam.DELTA

   .. data:: GAMMA = siege.component.CombatTeam.GAMMA

   .. data:: NONE = siege.component.CombatTeam.NONE

   .. data:: OMEGA = siege.component.CombatTeam.OMEGA

   .. data:: ZETA = siege.component.CombatTeam.ZETA

Direction
-----------------------------------
.. class:: Direction

   

   .. data:: ALL = siege.component.Direction.ALL

   .. data:: BOTTOM = siege.component.Direction.BOTTOM

   .. data:: HORIZONTAL = siege.component.Direction.HORIZONTAL

   .. data:: LEFT = siege.component.Direction.LEFT

   .. data:: NONE = siege.component.Direction.NONE

   .. data:: RIGHT = siege.component.Direction.RIGHT

   .. data:: TOP = siege.component.Direction.TOP

   .. data:: VERTICAL = siege.component.Direction.VERTICAL

FoliagePriority
-----------------------------------
.. class:: FoliagePriority

   

   .. data:: High = siege.component.FoliagePriority.High

   .. data:: Low = siege.component.FoliagePriority.Low

   .. data:: Medium = siege.component.FoliagePriority.Medium

   .. data:: VeryHigh = siege.component.FoliagePriority.VeryHigh

   .. data:: VeryLow = siege.component.FoliagePriority.VeryLow

FoliageType
-----------------------------------
.. class:: FoliageType

   

   .. data:: Overlay = siege.component.FoliageType.Overlay

   .. data:: Tile = siege.component.FoliageType.Tile

GrowDepth
-----------------------------------
.. class:: GrowDepth

   

   .. data:: Any = siege.component.GrowDepth.Any

   .. data:: Surface = siege.component.GrowDepth.Surface

   .. data:: Underground = siege.component.GrowDepth.Underground

GrowthType
-----------------------------------
.. class:: GrowthType

   

   .. data:: Grass = siege.component.GrowthType.Grass

   .. data:: Plant = siege.component.GrowthType.Plant

   .. data:: Vine = siege.component.GrowthType.Vine

MapMode
-----------------------------------
.. class:: MapMode

   

   .. data:: Fullscreen = siege.component.MapMode.Fullscreen

   .. data:: Hidden = siege.component.MapMode.Hidden

   .. data:: Minimap = siege.component.MapMode.Minimap

   .. data:: Overlay = siege.component.MapMode.Overlay

MonsterPlacementType
-----------------------------------
.. class:: MonsterPlacementType

   

   .. data:: Custom = siege.component.MonsterPlacementType.Custom

   .. data:: InAir = siege.component.MonsterPlacementType.InAir

   .. data:: InGround = siege.component.MonsterPlacementType.InGround

   .. data:: InWater = siege.component.MonsterPlacementType.InWater

   .. data:: OnGround = siege.component.MonsterPlacementType.OnGround

PlayerMode
-----------------------------------
.. class:: PlayerMode

   

   .. data:: Aggressive = siege.component.PlayerMode.Aggressive

   .. data:: Passive = siege.component.PlayerMode.Passive

Slope
-----------------------------------
.. class:: Slope

   

   .. data:: LEFT = siege.component.Slope.LEFT

   .. data:: NONE = siege.component.Slope.NONE

   .. data:: RIGHT = siege.component.Slope.RIGHT

SupportType
-----------------------------------
.. class:: SupportType

   

   .. data:: SUPPORT_BOTTOM = siege.component.SupportType.SUPPORT_BOTTOM

   .. data:: SUPPORT_LEFT = siege.component.SupportType.SUPPORT_LEFT

   .. data:: SUPPORT_RIGHT = siege.component.SupportType.SUPPORT_RIGHT

   .. data:: SUPPORT_TOP = siege.component.SupportType.SUPPORT_TOP

ActiveEffect
-----------------------------------
.. class:: ActiveEffect

   

   .. attribute:: effect

      

   .. attribute:: level

      

   .. attribute:: name

      

   .. attribute:: sourceContent

      

   .. attribute:: sourceId

      

   .. attribute:: timer

       |      (:class:`Timer`)


ActiveEffectMap
-----------------------------------
.. class:: ActiveEffectMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

AnimationDetails
-----------------------------------
.. class:: AnimationDetails

   

   .. attribute:: animating

      

   .. attribute:: currentAnimation

      

   .. attribute:: forced

      

   .. attribute:: frameScale

      

   .. attribute:: frameTime

      

   .. attribute:: group

      

   .. attribute:: hold

      

   .. attribute:: index

      

   .. attribute:: isVisible

      

   .. attribute:: playTime

      

AnimationDetailsMap
-----------------------------------
.. class:: AnimationDetailsMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

BodyCustomization
-----------------------------------
.. class:: BodyCustomization

   

   .. method:: __init__( group, mapping[, supportsColor=True[, isOptional=False]])

      

      :param group: 

      :type group: str

      :param mapping: 

      :type mapping: str

      :param supportsColor: 

      :type supportsColor: bool

      :param isOptional: 

      :type isOptional: bool

   .. attribute:: colors

      

   .. attribute:: group

      

   .. attribute:: isOptional

      

   .. attribute:: mapping

      

   .. attribute:: supportsColor

      

Component
-----------------------------------
.. class:: Component

   

   .. method:: clean( )

      Resets the dirty flag. Override when additional data needs to be cleaned.


   .. method:: create( entity)

      Called whenever a new entity with this component has finished being created.


      :param entity:  The newly created entity.


      :type entity: :class:`Entity`

   .. method:: destroy( )

      Called whenever the entity this component belongs to is being destroyed.


   .. method:: dirty( )

      Marks this :class:`Component` as dirty. This should be called anytime data synced in :py:func:`pack` is changed.


   .. method:: freeze( )

      Freezes this component disallowing any further attributes to be added.


   .. method:: fullDirty( )

      Called whenever this :class:`Component` should be marked as fully dirty.Override when data is conditionally synced in :py:func:`pack`.


   .. method:: getCid( )

      Retrieves the unique :class:`Component` ID given to this component type.


      :rtype: int


   .. method:: getParent( )

      Returns the parent :class:`Entity` this component belongs to.


      :returns: The parent entity.


      :rtype: Entity


   .. method:: getType( )

      Retrieves the type of this component.


      :rtype: str


   .. method:: getVersion( )

      Retrieves the current version for this component.


      :rtype: int


   .. method:: isDirty( )

      Returns if this :class:`Component` has been marked as dirty since the last multiplayer data sync.


      :returns: Whether this :class:`Component` is dirty or not.


      :rtype: bool


   .. method:: pack( stream)

      Called whenever this component needs to be synced over the network.


      :param stream:  The stream that the :class:`Component` data should be written to.


      :type stream: :class:`DataStream`

   .. method:: read( stream, version)

      Called whenever this component is being read from the network.


      :param stream:  The stream that the :class:`Component` data should be read from.


      :type stream: :class:`DataStream`

      :param version:  The version of the :class:`Component` that the data was saved with.


      :type version: int

   .. method:: readEntities( stream, version)

      Called when loading a player. Override for components that stores entities and read the entities from the stream.This ensures that the entities exist before attempting to access them elsewhere.


      :param stream:  The stream that the :class:`Component` data should be read from.


      :type stream: :class:`DataStream`

      :param version:  The version of the :class:`Component` that the data was saved with.


      :type version: int

   .. method:: unpack( stream)

      Called whenever this component is being read from the network.


      :param stream:  The stream that the :class:`Component` data should be read from.


      :type stream: :class:`DataStream`

   .. method:: update( frameTime)

      Called every frame allowing the component to update itself.


      :param frameTime:  The amount of time (ms) elapsed since the last frame.


      :type frameTime: int

   .. method:: validate( )

      Returns if this :class:`Component` data is valid - used for testing.


      :returns: Whether this :class:`Component` is valid or not.


      :rtype: bool


   .. method:: write( stream)

      Called whenever this component is being written to disk (saving).


      :param stream:  The stream that the :class:`Component` data should be written to.


      :type stream: :class:`DataStream`

   .. method:: writeEntities( stream)

      Called when saving a player. Override for components that stores entities and write the entities to the stream.


      :param stream:  The stream that the :class:`Component` data should be read from.


      :type stream: :class:`DataStream`

AnimationComponent
-----------------------------------
.. class:: AnimationComponent

   

   .. method:: backupAnimations( )

      

      :rtype: :class:`AnimationDetailsMap`

   .. method:: clearQueue( [group=''])

      

      :param group: 

      :type group: str

   .. method:: getAnimationLength( [group=''])

      

      :param group: 

      :type group: str

      :rtype: int

   .. method:: getAnimationName( [group=''])

      

      :param group: 

      :type group: str

      :rtype: str

   .. method:: getFrame( [group=''])

      

      :param group: 

      :type group: str

      :rtype: int

   .. method:: getFrameTime( [group=''])

      

      :param group: 

      :type group: str

      :rtype: int

   .. method:: getPlayTime( [group=''])

      

      :param group: 

      :type group: str

      :rtype: int

   .. method:: has( name[, group=''])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

      :rtype: bool

   .. method:: hide( [group=''[, bypassLock=False]])

      

      :param group: 

      :type group: str

      :param bypassLock: 

      :type bypassLock: bool

   .. method:: hold( [group=''])

      

      :param group: 

      :type group: str

   .. method:: isLocked( )

      

      :rtype: bool

   .. method:: isPlaying( name[, group=''])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

      :rtype: bool

   .. method:: isPlayingGroup( [group=''])

      

      :param group: 

      :type group: str

      :rtype: bool

   .. method:: lock( )

      

   .. method:: pause( [group=''[, bypassLock=False]])

      

      :param group: 

      :type group: str

      :param bypassLock: 

      :type bypassLock: bool

   .. method:: play( [name=''[, group=''[, forceRestart=False[, bypassLock=False]]]])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

      :param forceRestart: 

      :type forceRestart: bool

      :param bypassLock: 

      :type bypassLock: bool

   .. method:: queue( name[, group=''])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

   .. method:: restoreAnimations( arg2)

      

      :param arg2: 

      :type arg2: :class:`AnimationDetailsMap`

   .. method:: scale( totalDelay[, group=''[, downOnly=True]])

      

      :param totalDelay: 

      :type totalDelay: int

      :param group: 

      :type group: str

      :param downOnly: 

      :type downOnly: bool

   .. method:: stop( [group=''[, bypassLock=False]])

      

      :param group: 

      :type group: str

      :param bypassLock: 

      :type bypassLock: bool

   .. method:: unlock( )

      

   .. method:: wasForced( [group=''])

      

      :param group: 

      :type group: str

      :rtype: bool

   .. method:: wasPlaying( name[, group=''])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

      :rtype: bool

   .. attribute:: defaultAnimation

      

   .. attribute:: onFinished

      

AttachmentComponent
-----------------------------------
.. class:: AttachmentComponent

   

   .. method:: attach( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`Entity`

   .. method:: attach( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: :class:`Vector`

   .. method:: detach( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: detach( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: getAttached( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`Entity`

   .. method:: hasAttached( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: hasAttached( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :rtype: bool

BagComponent
-----------------------------------
.. class:: BagComponent

   

   .. attribute:: canCarry

      

   .. attribute:: capacity

      

BodyComponent
-----------------------------------
.. class:: BodyComponent

   

   .. attribute:: colors

      

   .. attribute:: components

      

   .. attribute:: customizations

      

   .. attribute:: identifier

      

   .. attribute:: initialize

      

   .. attribute:: substitutions

      

CombatComponent
-----------------------------------
.. class:: CombatComponent

   

   .. method:: __init__( definition)

      

      :param definition: 

      :type definition: :class:`Combat`

   .. method:: adjustExperience( amount)

      

      :param amount: 

      :type amount: int

   .. method:: clearCooldown( cooldown)

      

      :param cooldown: 

      :type cooldown: str

      :rtype: bool

   .. method:: finishAttack( attackId)

      

      :param attackId: 

      :type attackId: int

   .. method:: getExperienceToLevel( [level=0])

      

      :param level: 

      :type level: int

      :rtype: int

   .. method:: getLevelCap( )

      

      :rtype: int

   .. method:: hasAlreadyHit( attackId, entity)

      

      :param attackId: 

      :type attackId: int

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: hasCooldown( cooldown)

      

      :param cooldown: 

      :type cooldown: :class:`Cooldown`

      :rtype: bool

   .. method:: hasCooldownTolerant( cooldown)

      

      :param cooldown: 

      :type cooldown: :class:`Cooldown`

      :rtype: bool

   .. method:: hit( attackId, entity)

      

      :param attackId: 

      :type attackId: int

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: isMaxLevel( )

      

      :rtype: bool

   .. method:: setAlive( alive)

      

      :param alive: 

      :type alive: bool

   .. method:: setCanRecover( canRecover)

      

      :param canRecover: 

      :type canRecover: bool

   .. method:: setCooldown( cooldown)

      

      :param cooldown: 

      :type cooldown: :class:`Cooldown`

   .. method:: setFatigued( fatigued)

      

      :param fatigued: 

      :type fatigued: bool

   .. method:: setInvincible( invincible)

      

      :param invincible: 

      :type invincible: bool

   .. method:: setLevel( level)

      

      :param level: 

      :type level: int

   .. method:: setTargetable( targetable)

      

      :param targetable: 

      :type targetable: bool

   .. method:: startAttack( )

      

      :rtype: int

   .. method:: update( frameTime)

      

      :param frameTime: 

      :type frameTime: int

   .. attribute:: blockStaminaCost

      

   .. attribute:: blockThreshold

      

   .. attribute:: canRecover

      

   .. attribute:: cooldowns

      

   .. attribute:: experience

      

   .. attribute:: experienceYield

      

   .. attribute:: isAlive

      

   .. attribute:: isFatigued

      

   .. attribute:: isHitStunned

      

   .. attribute:: isInvincible

      

   .. attribute:: isTargetable

      

   .. attribute:: knockback

      

   .. attribute:: knockbackModifier

      

   .. attribute:: level

      

   .. attribute:: levels

      

   .. attribute:: magicalReduction

      

   .. attribute:: numberOffset

      

   .. attribute:: onDamageSound

      

   .. attribute:: onDeathSound

      

   .. attribute:: onExpiredCooldown

      

   .. attribute:: onHit

      

   .. attribute:: onSetCooldown

      

   .. attribute:: onStatusChange

      

   .. attribute:: physicalReduction

      

   .. attribute:: status

      

   .. attribute:: team

      

   .. attribute:: timeSinceCombat

      

CraftComponent
-----------------------------------
.. class:: CraftComponent

   

   .. method:: usesMaterial( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. attribute:: category

      

   .. attribute:: experience

      

   .. attribute:: isResearchable

      

   .. attribute:: level

      

   .. attribute:: materials

      

   .. attribute:: onCraft

      

   .. attribute:: requiresDiscoveryMaterials

      

   .. attribute:: results

      

   .. attribute:: servicesRequired

      

   .. attribute:: subcategory

      

CustomizationComponent
-----------------------------------
.. class:: CustomizationComponent

   

   .. attribute:: bodies

      

   .. attribute:: group

      

   .. attribute:: substitutions

      

   .. attribute:: supportsColor

      

DroppedComponent
-----------------------------------
.. class:: DroppedComponent

   

   .. attribute:: expired

      

   .. attribute:: ignorePlayer

      

   .. attribute:: quantity

      

EffectsComponent
-----------------------------------
.. class:: EffectsComponent

   

   .. method:: add( effect, level, duration[, source=None])

      

      :param effect: 

      :type effect: str

      :param level: 

      :type level: int

      :param duration: 

      :type duration: int

      :param source: 

      :type source: :class:`Entity`

   .. method:: get( effect)

      

      :param effect: 

      :type effect: str

      :rtype: :class:`ActiveEffect`

   .. method:: getEffects( )

      

      :rtype: :class:`ActiveEffectMap`

   .. method:: has( effect)

      

      :param effect: 

      :type effect: str

      :rtype: bool

   .. method:: level( effect, level, duration)

      

      :param effect: 

      :type effect: str

      :param level: 

      :type level: int

      :param duration: 

      :type duration: int

      :rtype: int

   .. method:: remove( effect[, duration=0])

      

      :param effect: 

      :type effect: str

      :param duration: 

      :type duration: int

   .. method:: removeAll( )

      

   .. attribute:: onAddEffect

      

   .. attribute:: onRemoveEffect

      

   .. attribute:: onUpdateEffect

      

EquipmentComponent
-----------------------------------
.. class:: EquipmentComponent

   

   .. method:: addAttribute( attribute)

      

      :param attribute: 

      :type attribute: object

   .. method:: getAttributes( )

      

      :rtype: :class:`EquipmentAttributes`

   .. method:: getContentAttributes( )

      

      :rtype: list

   .. method:: getModifiedName( )

      

      :rtype: str

   .. method:: getPotentialRange( )

      

      :rtype: :class:`RangeUint`

   .. method:: getSlots( )

      

      :rtype: :class:`StringList`

   .. method:: getSubstitutions( )

      

      :rtype: :class:`SubstitutionMap`

   .. method:: hasAttribute( type)

      

      :param type: 

      :type type: str

      :rtype: bool

   .. method:: hasSlot( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: isAttached( )

      

      :rtype: bool

   .. method:: removeAttribute( attribute)

      

      :param attribute: 

      :type attribute: object

   .. attribute:: levelRequired

      

   .. attribute:: potentials

      

   .. attribute:: quality

      

EventComponent
-----------------------------------
.. class:: EventComponent

   

   .. method:: __getitem__( name)

      

      :param name: 

      :type name: str

      :rtype: :class:`GameEvent`

   .. method:: has( name)

      

      :param name: 

      :type name: str

      :rtype: bool

   .. method:: reset( )

      

FoliageComponent
-----------------------------------
.. class:: FoliageComponent

   

   .. method:: getCompatibleTiles( )

      

      :rtype: :class:`StringList`

   .. method:: getOnPhysicsEntityContact( )

      

      :rtype: object

   .. method:: getTimeToUpdate( )

      

      :rtype: int

   .. attribute:: foliageType

      

   .. attribute:: growthType

      

   .. attribute:: id

      

   .. attribute:: particlePath

      

   .. attribute:: priority

      

GearComponent
-----------------------------------
.. class:: GearComponent

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Component`

      :rtype: bool

   .. method:: __getattr__( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: add( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: int

      :rtype: int

   .. method:: canEquip( item[, slotName=''])

      

      :param item: 

      :type item: :class:`InventoryItem`

      :param slotName: 

      :type slotName: str

      :rtype: bool

   .. method:: consume( slotName[, quantity=1])

      

      :param slotName: 

      :type slotName: str

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: disable( slot)

      

      :param slot: 

      :type slot: str

   .. method:: disableAll( category)

      

      :param category: 

      :type category: str

   .. method:: enable( slot)

      

      :param slot: 

      :type slot: str

   .. method:: enableAll( category)

      

      :param category: 

      :type category: str

   .. method:: equip( item[, slotName=''])

      

      :param item: 

      :type item: :class:`InventoryItem`

      :param slotName: 

      :type slotName: str

      :rtype: :class:`InventoryItem`

   .. method:: get( slot)

      

      :param slot: 

      :type slot: str

      :rtype: :class:`GearSlot`

   .. method:: getCategorySlots( category)

      

      :param category: 

      :type category: str

      :rtype: :class:`StringList`

   .. method:: getContentQuantity( arg2)

      

      :param arg2: 

      :type arg2: :class:`Content`

      :rtype: int

   .. method:: getSlot( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :rtype: str

   .. method:: hasSlot( slotName)

      

      :param slotName: 

      :type slotName: str

      :rtype: bool

   .. method:: hasUniqueItem( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :rtype: bool

   .. method:: isEnabled( slot)

      

      :param slot: 

      :type slot: str

      :rtype: bool

   .. method:: isOpen( slot)

      

      :param slot: 

      :type slot: str

      :rtype: bool

   .. method:: next( )

      

      :rtype: object

   .. method:: remove( content[, quantity=1])

      

      :param content: 

      :type content: :class:`Content`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: remove( content[, quantity=1])

      

      :param content: 

      :type content: :class:`Entity`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: resetGraphics( )

      

   .. method:: stack( item)

      

      :param item: 

      :type item: :class:`InventoryItem`

      :rtype: :class:`InventoryItem`

   .. method:: unequip( slotName)

      

      :param slotName: 

      :type slotName: str

      :rtype: :class:`InventoryItem`

   .. attribute:: onChange

      

   .. attribute:: ordered

      

InventoryComponent
-----------------------------------
.. class:: InventoryComponent

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Component`

      :rtype: bool

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: add( entity[, quantity=1])

      

      :param entity: 

      :type entity: :class:`Entity`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: addBag( bagIndex, bagEntity)

      

      :param bagIndex: 

      :type bagIndex: int

      :param bagEntity: 

      :type bagEntity: :class:`Entity`

      :rtype: :class:`ItemBag`

   .. method:: addBag( bagIndex, size)

      

      :param bagIndex: 

      :type bagIndex: int

      :param size: 

      :type size: int

      :rtype: :class:`ItemBag`

   .. method:: canAdd( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: canAdd( bagIndex, item)

      

      :param bagIndex: 

      :type bagIndex: int

      :param item: 

      :type item: :class:`Entity`

      :rtype: bool

   .. method:: clear( bagIndex, index)

      

      :param bagIndex: 

      :type bagIndex: int

      :param index: 

      :type index: int

   .. method:: decrement( bagIndex, index, quantity)

      

      :param bagIndex: 

      :type bagIndex: int

      :param index: 

      :type index: int

      :param quantity: 

      :type quantity: int

   .. method:: exists( bagIndex)

      

      :param bagIndex: 

      :type bagIndex: int

      :rtype: bool

   .. method:: get( bagIndex, index)

      

      :param bagIndex: 

      :type bagIndex: int

      :param index: 

      :type index: int

      :rtype: :class:`InventoryItem`

   .. method:: getBag( index)

      

      :param index: 

      :type index: int

      :rtype: :class:`ItemBag`

   .. method:: getBagCount( )

      

      :rtype: int

   .. method:: getBagIndexForContent( content)

      

      :param content: 

      :type content: :class:`Content`

      :rtype: int

   .. method:: getBagIndexForUniqueItem( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: int

   .. method:: getBags( )

      

      :rtype: :class:`ItemBags`

   .. method:: getContentQuantity( content)

      

      :param content: 

      :type content: :class:`Content`

      :rtype: int

   .. method:: getSlot( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :rtype: str

   .. method:: handleChange( bagIndex, index, previous, item)

      

      :param bagIndex: 

      :type bagIndex: int

      :param index: 

      :type index: int

      :param previous: 

      :type previous: :class:`InventoryItem`

      :param item: 

      :type item: :class:`InventoryItem`

   .. method:: hasContentQuantity( content, quantity)

      

      :param content: 

      :type content: :class:`Content`

      :param quantity: 

      :type quantity: int

      :rtype: bool

   .. method:: hasUniqueItem( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: isEmpty( index)

      

      :param index: 

      :type index: int

      :rtype: bool

   .. method:: isEmpty( arg2, bagIndex)

      

      :param arg2: 

      :type arg2: int

      :param bagIndex: 

      :type bagIndex: int

      :rtype: bool

   .. method:: isFull( )

      

      :rtype: bool

   .. method:: isFull( bagIndex)

      

      :param bagIndex: 

      :type bagIndex: int

      :rtype: bool

   .. method:: next( )

      

      :rtype: object

   .. method:: remove( content[, quantity=1])

      

      :param content: 

      :type content: :class:`Content`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: remove( content[, quantity=1])

      

      :param content: 

      :type content: :class:`Entity`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: removeBag( bagIndex)

      

      :param bagIndex: 

      :type bagIndex: int

   .. method:: set( bagIndex, index, item)

      

      :param bagIndex: 

      :type bagIndex: int

      :param index: 

      :type index: int

      :param item: 

      :type item: :class:`InventoryItem`

   .. attribute:: capacity

      

   .. attribute:: onBagChange

      

   .. attribute:: onCapacityChange

      

   .. attribute:: onChange

      

ItemComponent
-----------------------------------
.. class:: ItemComponent

   

   .. method:: hasTag( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. attribute:: buyPrice

      

   .. attribute:: canRepeatUse

      

   .. attribute:: classification

      

   .. attribute:: cooldown

      

   .. attribute:: description

      

   .. attribute:: features

      

   .. attribute:: flavor

      

   .. attribute:: genus

      

   .. attribute:: hold

      

   .. attribute:: holdExterior

      

   .. attribute:: isUnique

      

   .. attribute:: isUsable

      

   .. attribute:: quality

      

   .. attribute:: requiresResearch

       |      :class:`Item` requires to be research through research system otherwise item is automatically researched when first discovered.


   .. attribute:: scraps

      

   .. attribute:: sellPrice

      

   .. attribute:: stack

      

   .. attribute:: tags

      

   .. attribute:: use

      

   .. attribute:: useAnimation

      

   .. attribute:: useTime

      

LegendComponent
-----------------------------------
.. class:: LegendComponent

   

   .. method:: disableMarker( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: enableMarker( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: getMarkerCount( )

      

      :rtype: int

   .. method:: hasMarker( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: isMarkerEnabled( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: loseMarker( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: obtainMarker( arg2)

      

      :param arg2: 

      :type arg2: str

   .. attribute:: onMarkerChange

      

LightComponent
-----------------------------------
.. class:: LightComponent

   

   .. method:: addSource( arg2)

      

      :param arg2: 

      :type arg2: :class:`LightSourceData`

      :rtype: :class:`LightSource`

   .. method:: getSource( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`LightSource`

   .. method:: hasSource( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: removeSource( arg2)

      

      :param arg2: 

      :type arg2: :class:`LightSource`

   .. method:: removeSource( arg2)

      

      :param arg2: 

      :type arg2: str

   .. attribute:: sources

      

MapMarkerComponent
-----------------------------------
.. class:: MapMarkerComponent

   

   .. attribute:: icon

      

   .. attribute:: markerType

      

   .. attribute:: updatePosition

      

MonsterComponent
-----------------------------------
.. class:: MonsterComponent

   

   .. method:: create( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. attribute:: biomes

      

   .. attribute:: core

      

   .. attribute:: hostile

      

   .. attribute:: isParagon

      

   .. attribute:: layer

      

   .. attribute:: levels

      

   .. attribute:: placementCallback

      

   .. attribute:: placementType

      

   .. attribute:: spawnOffset

      

   .. attribute:: spawner

      

   .. attribute:: weight

      

OrganicComponent
-----------------------------------
.. class:: OrganicComponent

   

   .. method:: onConstruct( arg2)

      

      :param arg2: 

      :type arg2: list

   .. attribute:: axis

      

   .. attribute:: habitables

      

   .. attribute:: organic

      

   .. attribute:: size

      

ParticleComponent
-----------------------------------
.. class:: ParticleComponent

   

PhysicsComponent
-----------------------------------
.. class:: PhysicsComponent

   

   .. method:: addPassingThrough( physics)

      

      :param physics: 

      :type physics: :class:`PhysicsComponent`

   .. method:: addTouching( direction)

      

      :param direction: 

      :type direction: :class:`Direction`

   .. method:: applyForce( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

   .. method:: calculateJumpHeight( speed, height)

      

      :param speed: 

      :type speed: float

      :param height: 

      :type height: float

      :rtype: float

   .. method:: clearPassingThrough( )

      

   .. method:: factorSurfaceFriction( surfaceFriction)

      

      :param surfaceFriction: 

      :type surfaceFriction: :class:`Vector`

   .. method:: flipX( flip)

      

      :param flip: 

      :type flip: bool

   .. method:: getBody( )

      

      :rtype: :class:`Rect`

   .. method:: getCenter( )

      

      :rtype: :class:`Vector`

   .. method:: getCollision( )

      

      :rtype: int

   .. method:: getFriction( )

      

      :rtype: :class:`Vector`

   .. method:: getGravity( )

      

      :rtype: :class:`Vector`

   .. method:: getGroundFriction( )

      

      :rtype: :class:`Vector`

   .. method:: getPassingThrough( )

      

      :rtype: :class:`PhysicsComponentList`

   .. method:: getPassthrough( )

      

      :rtype: int

   .. method:: getPreviousPosition( )

      

      :rtype: :class:`Vector`

   .. method:: getRestitution( )

      

      :rtype: :class:`Vector`

   .. method:: getTouching( )

      

      :rtype: int

   .. method:: getVelocity( )

      

      :rtype: :class:`Vector`

   .. method:: getWorldBody( )

      

      :rtype: :class:`Rect`

   .. method:: isTouching( direction)

      

      :param direction: 

      :type direction: :class:`Direction`

      :rtype: bool

   .. method:: isTouchingTile( position)

      

      :param position: 

      :type position: :class:`TileVector`

      :rtype: bool

   .. method:: resetGroundFriction( )

      

   .. method:: setBody( arg2)

      

      :param arg2: 

      :type arg2: :class:`Rect`

   .. method:: setFriction( friction)

      

      :param friction: 

      :type friction: :class:`Vector`

   .. method:: setGravity( gravity)

      

      :param gravity: 

      :type gravity: :class:`Vector`

   .. method:: setGroundFriction( friction)

      

      :param friction: 

      :type friction: :class:`Vector`

   .. method:: setRestitution( restitution)

      

      :param restitution: 

      :type restitution: :class:`Vector`

   .. method:: setVelocity( velocity)

      

      :param velocity: 

      :type velocity: :class:`Vector`

   .. method:: wake( )

      

   .. attribute:: active

      

   .. attribute:: applyGravityOnGround

      

   .. attribute:: hasGroundCollision

      

   .. attribute:: immovable

      

   .. attribute:: isUnderwater

      

   .. attribute:: jumpTimer

      

   .. attribute:: onTimeStep

      

   .. attribute:: sleeping

      

TilePhysicsComponent
-----------------------------------
.. class:: TilePhysicsComponent

   

   .. attribute:: tilePosition

      

PlacementComponent
-----------------------------------
.. class:: PlacementComponent

   

   .. method:: getArea( )

      

      :rtype: :class:`Rect`

   .. method:: getDropped( )

      

      :rtype: :class:`InventoryItem`

   .. method:: getRect( )

      

      :rtype: :class:`PixelRect`

   .. method:: getSupports( )

      

      :rtype: object

   .. method:: setAxisAnimation( )

      

   .. method:: setPlacement( placement)

      

      :param placement: 

      :type placement: :class:`PlacementComponent`

   .. method:: shouldDropItem( )

      

      :rtype: bool

   .. attribute:: allowCollection

      

   .. attribute:: allowSupportRemoval

      

   .. attribute:: axes

      

   .. attribute:: axis

      

   .. attribute:: destroyOnSupportRemoved

      

   .. attribute:: onCreate

      

   .. attribute:: onHit

      

   .. attribute:: supportEntity

      

   .. attribute:: supportTiles

      

PlayerStateComponent
-----------------------------------
.. class:: PlayerStateComponent

   

   .. method:: addGrappler( id, support)

      

      :param id: 

      :type id: int

      :param support: 

      :type support: :class:`PhysicsComponent`

   .. method:: clearGrapplers( )

      

   .. method:: hasGrapplers( )

      

      :rtype: bool

   .. method:: removeGrappler( index)

      

      :param index: 

      :type index: int

   .. attribute:: activeItem

      

   .. attribute:: canAttack

      

   .. attribute:: canCast

      

   .. attribute:: canMove

      

   .. attribute:: channel

      

   .. attribute:: grapplerId

      

   .. attribute:: grapplers

      

   .. attribute:: mapMode

      

   .. attribute:: mode

      

   .. attribute:: perseveranceTime

      

   .. attribute:: perseveranceTimerJob

      

   .. attribute:: toolState

      

RecipeSetComponent
-----------------------------------
.. class:: RecipeSetComponent

   

   .. attribute:: recipes

      

RenderComponent
-----------------------------------
.. class:: RenderComponent

   

   .. method:: faceDirection( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :param arg3: 

      :type arg3: int

   .. method:: flipX( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: flipY( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: getCenter( )

      

      :rtype: :class:`Vector`

   .. method:: getColor( )

      

      :rtype: :class:`Color`

   .. method:: getFlipX( )

      

      :rtype: bool

   .. method:: getFlipY( )

      

      :rtype: bool

   .. method:: getFrame( [group=''])

      

      :param group: 

      :type group: str

      :rtype: :class:`Frame`

   .. method:: getIconPath( )

      

      :rtype: str

   .. method:: getImagePath( )

      

      :rtype: str

   .. method:: getOrigin( )

      

      :rtype: :class:`Vector`

   .. method:: getPreviousPosition( )

      

      :rtype: :class:`Vector`

   .. method:: getRect( )

      

      :rtype: :class:`Rect`

   .. method:: getRotation( )

      

      :rtype: float

   .. method:: getScale( )

      

      :rtype: :class:`Vector`

   .. method:: getSize( )

      

      :rtype: :class:`PixelVector`

   .. method:: getWorldIconPath( )

      

      :rtype: str

   .. method:: hasMoved( )

      

      :rtype: bool

   .. method:: render( target[, loopWidth=0])

      

      :param target: 

      :type target: :class:`sfRenderTarget`

      :param loopWidth: 

      :type loopWidth: int

   .. method:: setColor( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

   .. method:: setFrame( frame[, group=''])

      

      :param frame: 

      :type frame: :class:`Frame`

      :param group: 

      :type group: str

   .. method:: setOrigin( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: setOriginToCenter( )

      

   .. method:: setRotation( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: setScale( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

   .. method:: setTexture( arg2)

      

      :param arg2: 

      :type arg2: :class:`Texture`

   .. method:: setTextureRect( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelRect`

   .. method:: setTrail( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: setVolatilePosition( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :param arg3: 

      :type arg3: int

   .. method:: updateSprite( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: useIconTexture( )

      

   .. method:: useTexture( )

      

   .. method:: useWorldIconTexture( )

      

   .. attribute:: alpha

      

   .. attribute:: brightness

      

   .. attribute:: onMove

      

   .. attribute:: rotation

      

   .. attribute:: sprite

      

   .. attribute:: states

      

ExtendableRenderComponent
-----------------------------------
.. class:: ExtendableRenderComponent

   

   .. method:: getTransform( )

      

      :rtype: :class:`Transform`

   .. attribute:: length

      

ModularRenderComponent
-----------------------------------
.. class:: ModularRenderComponent

   

   .. method:: addTexture( spriteId, texturePath)

      

      :param spriteId: 

      :type spriteId: int

      :param texturePath: 

      :type texturePath: str

   .. method:: addTexture( spriteId, texturePath, textureRect)

      

      :param spriteId: 

      :type spriteId: int

      :param texturePath: 

      :type texturePath: str

      :param textureRect: 

      :type textureRect: :class:`PixelRect`

   .. method:: changeSprite( arg2)

      

      :param arg2: 

      :type arg2: :class:`Substitution`

   .. method:: changeSpriteColor( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`Vector3`

   .. method:: changeSpriteVisibility( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: bool

   .. method:: changeSprites( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubstitutionMap`

   .. method:: getColor( )

      

      :rtype: :class:`Color`

   .. method:: getRect( )

      

      :rtype: :class:`Rect`

   .. method:: getScale( )

      

      :rtype: :class:`Vector`

   .. method:: getSprites( )

      

      :rtype: :class:`ModularRenderSpriteList`

   .. method:: getSprites( arg2)

      

      :param arg2: 

      :type arg2: :class:`StringList`

      :rtype: :class:`ModularRenderSpriteList`

   .. method:: getSprites( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`ModularRenderSpriteList`

   .. method:: getTopSprite( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: :class:`ModularRenderSprite`

   .. method:: hideSprite( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: render( target[, loopWidth=0])

      

      :param target: 

      :type target: :class:`sfRenderTarget`

      :param loopWidth: 

      :type loopWidth: int

   .. method:: renderLooped( target, position, >[, loopWidth=0]])

      

      :param target: 

      :type target: :class:`sfRenderTarget`

      :param position: 

      :type position: :class:`Vector`

      :param >: 

      :type >: =0

      :param loopWidth: 

      :type loopWidth: int

   .. method:: resetTextures( )

      

   .. method:: setColor( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

   .. method:: setPosition( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :param arg3: 

      :type arg3: int

   .. method:: setScale( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

   .. method:: showSprite( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: update( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: updateForced( )

      

   .. attribute:: alpha

      

   .. attribute:: brightness

      

   .. attribute:: modularSprites

      

   .. attribute:: onUpdate

      

   .. attribute:: shouldIgnorePosition

      

   .. attribute:: spriteIds

      

ReservesComponent
-----------------------------------
.. class:: ReservesComponent

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`ItemBag`

   .. method:: clear( reserveName)

      

      :param reserveName: 

      :type reserveName: str

   .. method:: observe( reserveName, droppedHandler)

      

      :param reserveName: 

      :type reserveName: str

      :param droppedHandler: 

      :type droppedHandler: object

   .. method:: resize( reserveName, size)

      

      :param reserveName: 

      :type reserveName: str

      :param size: 

      :type size: int

   .. method:: restore( reserveName, droppedHandler[, remove=True])

      

      :param reserveName: 

      :type reserveName: str

      :param droppedHandler: 

      :type droppedHandler: :class:`DroppedHandler`

      :param remove: 

      :type remove: bool

   .. method:: restoreAll( droppedHandler, blacklist)

      

      :param droppedHandler: 

      :type droppedHandler: :class:`DroppedHandler`

      :param blacklist: 

      :type blacklist: :class:`StringSet`

ShieldComponent
-----------------------------------
.. class:: ShieldComponent

   

   .. attribute:: blockSound

      

   .. attribute:: magicalReduction

      

   .. attribute:: onUse

      

   .. attribute:: physicalReduction

      

   .. attribute:: staminaCost

      

   .. attribute:: threshold

      

StatisticsComponent
-----------------------------------
.. class:: StatisticsComponent

   

   .. method:: adjust( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: int

      :rtype: int

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: int

   .. method:: has( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: set( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: int

   .. method:: unwatch( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: watch( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

StatsComponent
-----------------------------------
.. class:: StatsComponent

   

   .. method:: __getattr__( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: object

   .. method:: get( stat)

      

      :param stat: 

      :type stat: str

      :rtype: :class:`DynamicStat`

   .. method:: has( stat)

      

      :param stat: 

      :type stat: str

      :rtype: bool

   .. attribute:: stats

      

SurfaceComponent
-----------------------------------
.. class:: SurfaceComponent

   

   .. method:: addService( service)

      

      :param service: 

      :type service: str

   .. method:: getServices( )

      

      :rtype: :class:`StringSet`

   .. method:: has( service)

      

      :param service: 

      :type service: str

      :rtype: bool

   .. method:: removeService( service)

      

      :param service: 

      :type service: str

   .. attribute:: onServiceAdded

      

   .. attribute:: onServiceRemoved

      

TalentsComponent
-----------------------------------
.. class:: TalentsComponent

   

   .. method:: __getattr__( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: object

   .. method:: get( talent)

      

      :param talent: 

      :type talent: str

      :rtype: :class:`ActiveTalent`

   .. method:: has( talent)

      

      :param talent: 

      :type talent: str

      :rtype: bool

   .. attribute:: ordered

      

TileComponent
-----------------------------------
.. class:: TileComponent

   

   .. method:: getDropped( )

      

      :rtype: str

   .. method:: getGroups( )

      

      :rtype: list

   .. method:: getLayer( )

      

      :rtype: :class:`Layer`

   .. method:: getName( )

      

      :rtype: str

   .. method:: getOnBreakSound( )

      

      :rtype: str

   .. method:: getOnHitSound( )

      

      :rtype: str

   .. method:: getRenderLayer( )

      

      :rtype: :class:`TileRenderLayer`

   .. method:: getTileId( )

      

      :rtype: int

   .. method:: getUpdateTime( )

      

      :rtype: :class:`RangeUint`

   .. method:: isCompatible( compatibles)

      

      :param compatibles: 

      :type compatibles: :class:`StringList`

      :rtype: bool

   .. attribute:: canPlace

      

   .. attribute:: consumeOnUse

      

   .. attribute:: durability

      

   .. attribute:: isFoliage

      

   .. attribute:: isFragile

      

   .. attribute:: isReplaceable

      

   .. attribute:: isSolid

      

   .. attribute:: isUpdateVisual

      

   .. attribute:: level

      

   .. attribute:: lightSource

      

   .. attribute:: onCreated

      

   .. attribute:: onDamaged

      

   .. attribute:: onDestroyed

      

   .. attribute:: onFoliageChange

      

   .. attribute:: onLoad

      

   .. attribute:: onNeighborChange

      

   .. attribute:: onPhysicsEntityContact

      

   .. attribute:: onUpdate

      

   .. attribute:: particleColor

      

   .. attribute:: providesSupport

      

ToolComponent
-----------------------------------
.. class:: ToolComponent

   

   .. method:: checkUsability( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`LayerManager`

      :param arg3: 

      :type arg3: :class:`Player`

      :param arg4: 

      :type arg4: :class:`Vector`

      :rtype: :class:`ToolUsabilityResult`

   .. method:: getHitTiles( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: :class:`TileLayer`

      :param arg3: 

      :type arg3: :class:`Player`

      :param arg4: 

      :type arg4: :class:`Vector`

      :param arg5: 

      :type arg5: float

      :rtype: :class:`TileVectorList`

   .. attribute:: compatibles

      

   .. attribute:: harvestPower

      

   .. attribute:: power

      

   .. attribute:: reach

      

ToolbarComponent
-----------------------------------
.. class:: ToolbarComponent

   

   .. method:: bagChanged( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`ItemBag`

   .. method:: changeToolbar( )

      

   .. method:: clearQuick( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: clearQuick( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`ToolItem`

   .. method:: get( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: :class:`ToolItem`

   .. method:: getQuick( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`ToolItem`

   .. method:: getQuick( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: :class:`ToolItem`

   .. method:: isEmpty( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: isEmpty( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. method:: isQuickEmpty( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: isQuickEmpty( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. method:: set( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`ToolItem`

   .. method:: set( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :param arg4: 

      :type arg4: :class:`ToolItem`

   .. method:: setQuick( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`ToolItem`

   .. method:: setQuick( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :param arg4: 

      :type arg4: :class:`ToolItem`

   .. method:: setQuickBar( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: setToolbar( arg2)

      

      :param arg2: 

      :type arg2: int

   .. attribute:: items

      

   .. attribute:: onChange

      

   .. attribute:: onQuickBarChange

      

   .. attribute:: onQuickChange

      

   .. attribute:: onSelectedChange

      

   .. attribute:: onToolbarChange

      

   .. attribute:: quickSize

      

   .. attribute:: quickbarIndex

      

   .. attribute:: quickbarSize

      

   .. attribute:: selected

      

   .. attribute:: size

      

   .. attribute:: toolbarIndex

      

   .. attribute:: toolbarSize

      

TriggerComponent
-----------------------------------
.. class:: TriggerComponent

   

   .. attribute:: actions

      

   .. attribute:: checkExpired

      

   .. attribute:: data

      

   .. attribute:: trigger

      

WeaponComponent
-----------------------------------
.. class:: WeaponComponent

   

   .. attribute:: attackType

      

   .. attribute:: category

      

   .. attribute:: currentAttack

      

   .. attribute:: damageType

      

   .. attribute:: onUse

      

   .. attribute:: power

      

   .. attribute:: swapBackOnAnimationFinish

      

   .. attribute:: weaponAttacks

      

ComponentDefinition
-----------------------------------
.. class:: ComponentDefinition

   

   .. method:: freeze( )

      Freezes this disallowing any further attributes to be added.


   .. method:: getType( )

      Retrieves the type of this component.


      :returns: The given type of this component.


      :rtype: str


   .. method:: getType( )

      

   .. method:: read( stream)

      Called when this is being read from the network. This is only needed when this :class:`ComponentDefinition` is dynamically added to entities.


      :param stream:  The stream that the :class:`ComponentDefinition` data should be read from.


      :type stream: :class:`DataStream`

   .. method:: set( attr, kwargs)

      Uses the given attribute name to set the attribute on this object from the provided dictionary.


      :param attr:  The name of the attribute to set.


      :type attr: str

      :param kwargs:  The dictionary from which to retrieve the attribute value.


      :type kwargs: dict

   .. method:: set( attrs, kwargs)

      Uses the given attribute names to set the attributes on this object from the provided dictionary.


      :param attrs:  The names of the attribute to set.


      :type attrs:  list of str


      :param kwargs:  The dictionary from which to retrieve the attribute value.


      :type kwargs: dict

   .. method:: write( stream)

      Called when this needs to be synced over the network. This is only needed when this :class:`ComponentDefinition` is dynamically added to entities.


      :param stream:  The stream that the :class:`Component` data should be written to.


      :type stream: :class:`DataStream`

   .. attribute:: isFrozen

       |      The current frozen state of this :class:`ComponentDefinition`.


Animation
-----------------------------------
.. class:: Animation

   

   .. method:: __init__( [start=''])

      

      :param start: 

      :type start: str

   .. method:: base( base)

      

      :param base: 

      :type base: str

   .. method:: bind( key, animation[, base=''])

      

      :param key: 

      :type key: str

      :param animation: 

      :type animation: str

      :param base: 

      :type base: str

   .. method:: setLooping( animation, looping)

      

      :param animation: 

      :type animation: str

      :param looping: 

      :type looping: bool

   .. attribute:: looping

      

   .. attribute:: start

      

Attachment
-----------------------------------
.. class:: Attachment

   

Bag
-----------------------------------
.. class:: Bag

   

   .. method:: __init__( [capacity=1[, canCarry=False]])

      

      :param capacity: 

      :type capacity: int

      :param canCarry: 

      :type canCarry: bool

   .. attribute:: canCarry

      

   .. attribute:: capacity

      

Combat
-----------------------------------
.. class:: Combat

   

   .. method:: __init__( [team=siege.component.CombatTeam.ALPHA, numberOffset, >]])

      

      :param team: 

      :type team: :class:`CombatTeam`

      :param numberOffset: 

      :type numberOffset: :class:`Vector`

      :param >]]: 

      :type >]]: =0

   .. attribute:: blockStaminaCost

      

   .. attribute:: blockThreshold

      

   .. attribute:: experienceYield

      

   .. attribute:: knockbackModifier

      

   .. attribute:: levels

      

   .. attribute:: magicalReduction

      

   .. attribute:: numberOffset

      

   .. attribute:: onDamageSound

      

   .. attribute:: onDeath

      

   .. attribute:: onDeathSound

      

   .. attribute:: onLevelUp

      

   .. attribute:: physicalReduction

      

   .. attribute:: team

      

Craft
-----------------------------------
.. class:: Craft

   

   .. method:: __init__( [category=''[, subcategory=''[, level=1[, experience=0]]]])

      

      :param category: 

      :type category: str

      :param subcategory: 

      :type subcategory: str

      :param level: 

      :type level: int

      :param experience: 

      :type experience: int

   .. method:: genus( item, quantity)

      

      :param item: 

      :type item: str

      :param quantity: 

      :type quantity: int

   .. method:: material( itemPath, quantity, requiresDiscovery)

      

      :param itemPath: 

      :type itemPath: str

      :param quantity: 

      :type quantity: int

      :param requiresDiscovery: 

      :type requiresDiscovery: bool

   .. method:: result( quantity, quality)

      

      :param quantity: 

      :type quantity: int

      :param quality: 

      :type quality: int

   .. method:: result( itemPath, quantity, quality)

      

      :param itemPath: 

      :type itemPath: str

      :param quantity: 

      :type quantity: int

      :param quality: 

      :type quality: int

   .. method:: result( items, quality)

      

      :param items: 

      :type items: list

      :param quality: 

      :type quality: int

   .. attribute:: category

      

   .. attribute:: experience

      

   .. attribute:: isResearchable

      

   .. attribute:: level

      

   .. attribute:: materials

      

   .. attribute:: onCraft

      

   .. attribute:: requiresDiscoveryMaterials

      

   .. attribute:: results

      

   .. attribute:: servicesRequired

      

   .. attribute:: subcategory

      

Dropped
-----------------------------------
.. class:: Dropped

   

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. attribute:: delay

      

   .. attribute:: quantity

      

Effects
-----------------------------------
.. class:: Effects

   

Event
-----------------------------------
.. class:: Event

   

   .. method:: __getitem__( name)

      

      :param name: 

      :type name: str

      :rtype: :class:`GameEvent`

   .. attribute:: events

      

Foliage
-----------------------------------
.. class:: Foliage

   

   .. attribute:: compatibleTiles

      

   .. attribute:: drops

      

   .. attribute:: foliageNeighbors

      

   .. attribute:: foliageType

      

   .. attribute:: growChance

      

   .. attribute:: growDepth

      

   .. attribute:: growthDirections

      

   .. attribute:: growthType

      

   .. attribute:: hasAutotiling

      

   .. attribute:: maxLength

      

   .. attribute:: onPhysicsEntityContact

      

   .. attribute:: onlyAutotileWithSelf

      

   .. attribute:: particlePath

      

   .. attribute:: priority

      

   .. attribute:: reactivateOnNeighborChange

      

   .. attribute:: requiresEmptyNeighbor

      

   .. attribute:: simple

      

   .. attribute:: spreadRange

      

   .. attribute:: spreadRate

       |      The frequency this foliage is considered a spreader. 0 being very rarely and 100 is all of the time.


   .. attribute:: spreadTimeRange

      

   .. attribute:: standard

      

   .. attribute:: supportDirection

      

   .. attribute:: updateTimeRange

      

   .. attribute:: variants

      

Gear
-----------------------------------
.. class:: Gear

   

   .. attribute:: slots

      

Hull
-----------------------------------
.. class:: Hull

   

   .. method:: __init__( [opacity=0])

      

      :param opacity: 

      :type opacity: int

   .. attribute:: enabled

      

   .. attribute:: opacity

      

Inventory
-----------------------------------
.. class:: Inventory

   

   .. method:: __init__( bags])

      

      :param bags]: 

      :type bags]: list

   .. attribute:: bags

      

Item
-----------------------------------
.. class:: Item

   

   .. method:: __init__( [stack=1[, useTime=100[, usable=True[, unique=False[, use=<siege.graphic.Substitution[, hold=<siege.graphic.Substitution)

      

      :param stack: 

      :type stack: int

      :param useTime: 

      :type useTime: int

      :param usable: 

      :type usable: bool

      :param unique: 

      :type unique: bool

      :param use: 

      :type use: :class:`Substitution`

      :param hold: 

      :type hold: :class:`Substitution`

   .. method:: setUseAnimation( animation[, group=''])

      

      :param animation: 

      :type animation: str

      :param group: 

      :type group: str

   .. attribute:: buyPrice

      

   .. attribute:: canRepeatUse

      

   .. attribute:: classification

      

   .. attribute:: cooldown

      

   .. attribute:: features

      

   .. attribute:: genus

      

   .. attribute:: hold

      

   .. attribute:: holdExterior

      

   .. attribute:: quality

      

   .. attribute:: requiresResearch

      

   .. attribute:: scraps

      

   .. attribute:: sellPrice

      

   .. attribute:: stack

      

   .. attribute:: tags

      

   .. attribute:: unique

      

   .. attribute:: usable

      

   .. attribute:: use

      

   .. attribute:: useAnimation

      

   .. attribute:: useGroup

      

   .. attribute:: useTime

      

Legend
-----------------------------------
.. class:: Legend

   

Light
-----------------------------------
.. class:: Light

   

   .. attribute:: sources

      

MapMarker
-----------------------------------
.. class:: MapMarker

   

   .. method:: __init__( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: str

      :param arg4: 

      :type arg4: bool

   .. attribute:: icon

      

   .. attribute:: markerType

      

   .. attribute:: updatePosition

      

ModularRender
-----------------------------------
.. class:: ModularRender

   

   .. method:: __init__( [dataFile=''[, icon=''[, contentPath='']]])

      

      :param dataFile: 

      :type dataFile: str

      :param icon: 

      :type icon: str

      :param contentPath: 

      :type contentPath: object

   .. method:: addMapping( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: str

   .. method:: setOrder( arg2)

      

      :param arg2: 

      :type arg2: list

   .. attribute:: attachmentAnimationBlacklists

      

   .. attribute:: dataFile

      

   .. attribute:: icon

      

   .. attribute:: origin

      

   .. attribute:: sheets

      

   .. attribute:: wicon

      

Monster
-----------------------------------
.. class:: Monster

   

   .. method:: __init__( [onCreate=None, spawnOffset, >]])

      

      :param onCreate: 

      :type onCreate: object

      :param spawnOffset: 

      :type spawnOffset: :class:`Vector`

      :param >]]: 

      :type >]]: =0

   .. attribute:: biomes

      

   .. attribute:: hostile

      

   .. attribute:: isParagon

      

   .. attribute:: layer

      

   .. attribute:: levels

      

   .. attribute:: onCreate

      

   .. attribute:: placementCallback

      

   .. attribute:: placementType

      

   .. attribute:: spawnOffset

      

   .. attribute:: weight

      

Organic
-----------------------------------
.. class:: Organic

   

   .. method:: __init__( arg2, arg3, arg4])

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: :class:`PixelVector`

      :param arg4]: 

      :type arg4]: list

   .. attribute:: axis

      

   .. attribute:: habitables

      

   .. attribute:: onCreate

      

   .. attribute:: size

      

Particle
-----------------------------------
.. class:: Particle

   

   .. attribute:: alpha

      

   .. attribute:: amount

      

   .. attribute:: color

      

   .. attribute:: lifetime

      

   .. attribute:: lightSource

      

   .. attribute:: particleArea

      

   .. attribute:: particleLife

      

   .. attribute:: particlePositions

      

   .. attribute:: position

      

   .. attribute:: rate

      

   .. attribute:: rotation

      

   .. attribute:: scale

      

   .. attribute:: textureCoords

      

   .. attribute:: texturePath

      

   .. attribute:: x

      

   .. attribute:: y

      

Physics
-----------------------------------
.. class:: Physics

   

   .. attribute:: active

      

   .. attribute:: applyGravityOnGround

      

   .. attribute:: body

      

   .. attribute:: collision

      

   .. attribute:: fallCap

      

   .. attribute:: friction

      

   .. attribute:: gravity

      

   .. attribute:: groundFriction

      

   .. attribute:: hasGroundCollision

      

   .. attribute:: immovable

      

   .. attribute:: passthrough

      

   .. attribute:: restitution

      

   .. attribute:: simulated

      

   .. attribute:: slope

      

Placement
-----------------------------------
.. class:: Placement

   

   .. method:: __init__( [axis=<siege.component.PlacementAxis[, allowCollection=True[, allowSupportRemoval=False]]])

      

      :param axis: 

      :type axis: :class:`PlacementAxis`

      :param allowCollection: 

      :type allowCollection: bool

      :param allowSupportRemoval: 

      :type allowSupportRemoval: bool

   .. method:: addAxis( data)

      

      :param data: 

      :type data: :class:`PlacementAxis`

   .. attribute:: allowCollection

      

   .. attribute:: allowSupportRemoval

      

   .. attribute:: axes

      

   .. attribute:: destroyOnSupportRemoved

      

   .. attribute:: dropped

      

   .. attribute:: onCreate

      

   .. attribute:: onHit

      

   .. attribute:: shouldDropItem

      

PlayerState
-----------------------------------
.. class:: PlayerState

   

RecipeSet
-----------------------------------
.. class:: RecipeSet

   

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: list

Render
-----------------------------------
.. class:: Render

   

   .. method:: __init__( arg2, arg3])

      

      :param arg2: 

      :type arg2: str

      :param arg3]: 

      :type arg3]: object

   .. attribute:: color

      

   .. attribute:: data

      

   .. attribute:: flipX

      

   .. attribute:: flipY

      

   .. attribute:: icon

      

   .. attribute:: image

      

   .. attribute:: mask

      

   .. attribute:: position

      

   .. attribute:: resetStates

      

   .. attribute:: rotation

      

   .. attribute:: scale

      

   .. attribute:: states

      

   .. attribute:: wicon

      

ExtendableRender
-----------------------------------
.. class:: ExtendableRender

   

   .. method:: __init__( image[, contentPath=''])

      

      :param image: 

      :type image: str

      :param contentPath: 

      :type contentPath: object

   .. attribute:: endWidth

      

   .. attribute:: middleWidth

      

   .. attribute:: startWidth

      

Reserves
-----------------------------------
.. class:: Reserves

   

Shield
-----------------------------------
.. class:: Shield

   

   .. method:: __init__( [physicalReduction=0[, magicalReduction=0[, onUse=None]]])

      

      :param physicalReduction: 

      :type physicalReduction: int

      :param magicalReduction: 

      :type magicalReduction: int

      :param onUse: 

      :type onUse: object

   .. attribute:: blockSound

      

   .. attribute:: magicalReduction

      

   .. attribute:: onUse

      

   .. attribute:: physicalReduction

      

   .. attribute:: staminaCost

      

   .. attribute:: threshold

      

Statistics
-----------------------------------
.. class:: Statistics

   

Stats
-----------------------------------
.. class:: Stats

   

   .. attribute:: stats

      

SubstitutionDefinition
-----------------------------------
.. class:: SubstitutionDefinition

   

   .. method:: addSub( base, replacement, origin, >])

      

      :param base: 

      :type base: str

      :param replacement: 

      :type replacement: str

      :param origin: 

      :type origin: :class:`Vector`

      :param >]: 

      :type >]: =0

   .. method:: hide( arg2)

      

      :param arg2: 

      :type arg2: str

   .. attribute:: substitutions

      

Body
-----------------------------------
.. class:: Body

   

   .. method:: __init__( [identifier=''])

      

      :param identifier: 

      :type identifier: str

   .. method:: addComponent( component)

      

      :param component: 

      :type component: object

   .. method:: addCustom( custom)

      

      :param custom: 

      :type custom: :class:`BodyCustomization`

   .. attribute:: animation

      

   .. attribute:: colors

      

   .. attribute:: customizations

      

   .. attribute:: identifier

      

   .. attribute:: initialize

      

Customization
-----------------------------------
.. class:: Customization

   

   .. method:: __init__( arg2, arg3])

      

      :param arg2: 

      :type arg2: str

      :param arg3]: 

      :type arg3]: bool

   .. attribute:: bodies

      

   .. attribute:: group

      

   .. attribute:: supportsColor

      

Equipment
-----------------------------------
.. class:: Equipment

   

   .. method:: __init__( [slots=[][, levelRequired=0]])

      

      :param slots: 

      :type slots: list

      :param levelRequired: 

      :type levelRequired: int

   .. attribute:: attributes

      

   .. attribute:: canEquip

      

   .. attribute:: isAttached

      

   .. attribute:: levelRequired

      

   .. attribute:: onCreate

      

   .. attribute:: onEquip

      

   .. attribute:: onUnequip

      

   .. attribute:: paths

      

   .. attribute:: potentialRange

      

   .. attribute:: potentials

      

   .. attribute:: slots

      

Surface
-----------------------------------
.. class:: Surface

   

   .. method:: __init__( [services=[]])

      

      :param services: 

      :type services: list

   .. attribute:: services

      

Talents
-----------------------------------
.. class:: Talents

   

   .. attribute:: talents

      

Tile
-----------------------------------
.. class:: Tile

   

   .. method:: __init__( [layer=siege.world.realm.Layer.WallAndGround[, level=1[, durability=1[, priority=500[, variants=3]]]]])

      

      :param layer: 

      :type layer: :class:`Layer`

      :param level: 

      :type level: int

      :param durability: 

      :type durability: int

      :param priority: 

      :type priority: int

      :param variants: 

      :type variants: int

   .. method:: addVariant( variant)

      

      :param variant: 

      :type variant: list

   .. attribute:: allowLightThrough

      

   .. attribute:: canPlace

      

   .. attribute:: collisions

      

   .. attribute:: consume

      

   .. attribute:: dropped

      

   .. attribute:: durability

      

   .. attribute:: foliage

      

   .. attribute:: fragile

      

   .. attribute:: groups

      

   .. attribute:: layer

      

   .. attribute:: level

      

   .. attribute:: lightSource

      

   .. attribute:: mapGroundColor

      

   .. attribute:: mapWallColor

      

   .. attribute:: onBreakSound

      

   .. attribute:: onCreated

      

   .. attribute:: onDamaged

      

   .. attribute:: onDestroyed

      

   .. attribute:: onFoliageChange

      

   .. attribute:: onHitSound

      

   .. attribute:: onLoad

      

   .. attribute:: onNeighborChange

      

   .. attribute:: onPhysicsEntityContact

      

   .. attribute:: onUpdate

      

   .. attribute:: onlyAutotileWithSelf

      

   .. attribute:: opacity

      

   .. attribute:: particleColor

      

   .. attribute:: passthrough

      

   .. attribute:: priority

      

   .. attribute:: renderLayer

      

   .. attribute:: replaceable

      

   .. attribute:: simple

      

   .. attribute:: solid

      

   .. attribute:: stable

      

   .. attribute:: standard

      

   .. attribute:: support

      

   .. attribute:: surfaceFriction

      

   .. attribute:: updateTime

      

   .. attribute:: updateVisual

      

   .. attribute:: variants

      

   .. attribute:: wallOpacity

      

Tool
-----------------------------------
.. class:: Tool

   

   .. method:: __init__( [power=0[, harvestPower=0[, reach=0[, compatible=[]]]]])

      

      :param power: 

      :type power: int

      :param harvestPower: 

      :type harvestPower: int

      :param reach: 

      :type reach: int

      :param compatible: 

      :type compatible: list

   .. attribute:: compatible

      

   .. attribute:: harvestPower

      

   .. attribute:: power

      

   .. attribute:: reach

      

Toolbar
-----------------------------------
.. class:: Toolbar

   

Trigger
-----------------------------------
.. class:: Trigger

   

   .. method:: __init__( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: list

      :param arg4: 

      :type arg4: object

      :param arg5: 

      :type arg5: dict

   .. attribute:: actions

      

   .. attribute:: checkExpired

      

   .. attribute:: data

      

   .. attribute:: trigger

      

Weapon
-----------------------------------
.. class:: Weapon

   

   .. method:: __init__( [category=''[, power=0[, attackType=0[, damageType=0[, onUse=None]]]]])

      

      :param category: 

      :type category: str

      :param power: 

      :type power: int

      :param attackType: 

      :type attackType: int

      :param damageType: 

      :type damageType: int

      :param onUse: 

      :type onUse: object

   .. attribute:: attackType

      

   .. attribute:: category

      

   .. attribute:: damageType

      

   .. attribute:: onUse

      

   .. attribute:: power

      

   .. attribute:: swapBackOnAnimationFinish

      

   .. attribute:: weaponAttacks

      

ComponentFactory
-----------------------------------
.. class:: ComponentFactory

   

   .. method:: __call__( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: str

      :param arg4: 

      :type arg4: object

      :rtype: :class:`Component`

   .. staticmethod:: create( [func=None])

      

      :param func: 

      :type func: object

      :rtype: :class:`ComponentFactory`

ComponentMap
-----------------------------------
.. class:: ComponentMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

CooldownMap
-----------------------------------
.. class:: CooldownMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

CraftResult
-----------------------------------
.. class:: CraftResult

   

   .. method:: __init__( quality)

      

      :param quality: 

      :type quality: int

   .. method:: __init__( craftResult)

      

      :param craftResult: 

      :type craftResult: :class:`CraftResult`

   .. attribute:: items

      

   .. attribute:: quality

      

CraftResultList
-----------------------------------
.. class:: CraftResultList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

Customizations
-----------------------------------
.. class:: Customizations

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

EventMap
-----------------------------------
.. class:: EventMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

EventResult
-----------------------------------
.. class:: EventResult

   

   .. attribute:: result

      

FoliageNeighbor
-----------------------------------
.. class:: FoliageNeighbor

   

   .. method:: __init__( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`TileVector`

      :param arg4: 

      :type arg4: :class:`RangeUint`

      :param arg5: 

      :type arg5: int

   .. attribute:: chance

      

   .. attribute:: delay

      

   .. attribute:: direction

      

   .. attribute:: foliage

      

FoliageNeighborList
-----------------------------------
.. class:: FoliageNeighborList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

GearSlot
-----------------------------------
.. class:: GearSlot

   

   .. method:: __init__( name, category, icon[, attachment=''[, active=True[, showInUi=False]]])

      

      :param name: 

      :type name: str

      :param category: 

      :type category: str

      :param icon: 

      :type icon: object

      :param attachment: 

      :type attachment: str

      :param active: 

      :type active: bool

      :param showInUi: 

      :type showInUi: bool

   .. attribute:: active

      

   .. attribute:: attachment

      

   .. attribute:: category

      

   .. attribute:: enabled

      

   .. attribute:: icon

      

   .. attribute:: item

      

   .. attribute:: name

      

   .. attribute:: showInUi

      

GearSlots
-----------------------------------
.. class:: GearSlots

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

GrapplerData
-----------------------------------
.. class:: GrapplerData

   

   .. method:: __init__( id, support)

      

      :param id: 

      :type id: int

      :param support: 

      :type support: :class:`PhysicsComponent`

   .. attribute:: id

      

   .. attribute:: support

      

GrapplerDataList
-----------------------------------
.. class:: GrapplerDataList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

ItemBags
-----------------------------------
.. class:: ItemBags

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

LoopingMap
-----------------------------------
.. class:: LoopingMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

MaterialList
-----------------------------------
.. class:: MaterialList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

ModularRenderSprite
-----------------------------------
.. class:: ModularRenderSprite

   

   .. attribute:: id

      

   .. attribute:: modular

      

   .. attribute:: sprite

      

   .. attribute:: texture

      

ModularRenderSpriteList
-----------------------------------
.. class:: ModularRenderSpriteList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

ModularSprite
-----------------------------------
.. class:: ModularSprite

   

   .. attribute:: flipX

      

   .. attribute:: hsl

      

   .. attribute:: id

      

   .. attribute:: isVisible

      

   .. attribute:: position

      

   .. attribute:: scale

      

   .. attribute:: spriteId

      

   .. attribute:: states

      

ModularSpriteList
-----------------------------------
.. class:: ModularSpriteList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

ModularSpriteListMap
-----------------------------------
.. class:: ModularSpriteListMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

PlacementAxes
-----------------------------------
.. class:: PlacementAxes

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

PlacementAxis
-----------------------------------
.. class:: PlacementAxis

   

   .. method:: __init__( axis, area, >[, layer=siege.world.realm.Layer.None]])

      

      :param axis: 

      :type axis: :class:`AxisType`

      :param area: 

      :type area: :class:`PixelRect`

      :param >: 

      :type >: eight=0

      :param layer: 

      :type layer: :class:`Layer`

   .. method:: addSupport( data)

      

      :param data: 

      :type data: :class:`PlacementSupport`

   .. attribute:: animation

      

   .. attribute:: area

      

   .. attribute:: layer

      

   .. attribute:: range

      

   .. attribute:: type

      

PlacementSupport
-----------------------------------
.. class:: PlacementSupport

   

   .. method:: __init__( type, range])

      

      :param type: 

      :type type: :class:`SupportType`

      :param range]: 

      :type range]: :class:`PixelVector`

   .. attribute:: range

      

   .. attribute:: support

      

PotentialAttribute
-----------------------------------
.. class:: PotentialAttribute

   

   .. method:: __init__( type, onCreate, weight, quality])

      

      :param type: 

      :type type: str

      :param onCreate: 

      :type onCreate: object

      :param weight: 

      :type weight: int

      :param quality]: 

      :type quality]: int

   .. attribute:: onCreate

      

   .. attribute:: quality

      

   .. attribute:: type

      

   .. attribute:: weight

      

PotentialAttributeList
-----------------------------------
.. class:: PotentialAttributeList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

SheetEntry
-----------------------------------
.. class:: SheetEntry

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SheetEntry`

      :rtype: bool

   .. method:: __init__( arg2, arg3, arg4])

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`PixelRect`

      :param arg4]: 

      :type arg4]: :class:`Vector`

   .. attribute:: image

      

   .. attribute:: origin

      

   .. attribute:: textureRect

      

SkillDefinitionList
-----------------------------------
.. class:: SkillDefinitionList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

SkillList
-----------------------------------
.. class:: SkillList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

SpriteNameIdsMap
-----------------------------------
.. class:: SpriteNameIdsMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

SpriteSheet
-----------------------------------
.. class:: SpriteSheet

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

SpriteSheetsMap
-----------------------------------
.. class:: SpriteSheetsMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

Stat
-----------------------------------
.. class:: Stat

   

   .. method:: __init__( name, fullName, start, cap, hasMax, visible)

      

      :param name: 

      :type name: str

      :param fullName: 

      :type fullName: str

      :param start: 

      :type start: float

      :param cap: 

      :type cap: float

      :param hasMax: 

      :type hasMax: bool

      :param visible: 

      :type visible: bool

   .. attribute:: cap

      

   .. attribute:: fullName

      

   .. attribute:: hasMax

      

   .. attribute:: isVisible

      

   .. attribute:: name

      

   .. attribute:: start

      

StatDefinitionList
-----------------------------------
.. class:: StatDefinitionList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

TalentDefinitionList
-----------------------------------
.. class:: TalentDefinitionList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

TalentList
-----------------------------------
.. class:: TalentList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

TalentMap
-----------------------------------
.. class:: TalentMap

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

ToolItemList
-----------------------------------
.. class:: ToolItemList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

ToolUsabilityResult
-----------------------------------
.. class:: ToolUsabilityResult

   

   .. attribute:: entity

      

   .. attribute:: harvestCompatible

      

   .. attribute:: isUsable

      

   .. attribute:: layer

      

   .. attribute:: position

      

   .. attribute:: useTile

      

WeaponAttack
-----------------------------------
.. class:: WeaponAttack

   

   .. method:: __init__( power, animation[, hitFrames=[][, attackTime=0[, comboTime=0[, cost=0[, sound='']]]]])

      

      :param power: 

      :type power: int

      :param animation: 

      :type animation: str

      :param hitFrames: 

      :type hitFrames: list

      :param attackTime: 

      :type attackTime: int

      :param comboTime: 

      :type comboTime: int

      :param cost: 

      :type cost: int

      :param sound: 

      :type sound: str

   .. attribute:: animation

      

   .. attribute:: attackTime

      

   .. attribute:: comboTime

      

   .. attribute:: hitFrames

      

   .. attribute:: power

      

   .. attribute:: sound

      

   .. attribute:: staminaCost

      

WeaponAttackList
-----------------------------------
.. class:: WeaponAttackList

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __delitem__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: extend( arg2)

      

      :param arg2: 

      :type arg2: object

