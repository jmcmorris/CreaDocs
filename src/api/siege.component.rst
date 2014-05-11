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

   .. data:: Idle = siege.component.CombatStatus.Idle

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

MonsterPlacementType
-----------------------------------
.. class:: MonsterPlacementType

   

   .. data:: Custom = siege.component.MonsterPlacementType.Custom

   .. data:: InAir = siege.component.MonsterPlacementType.InAir

   .. data:: InGround = siege.component.MonsterPlacementType.InGround

   .. data:: OnGround = siege.component.MonsterPlacementType.OnGround

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

ToolbarSlot
-----------------------------------
.. class:: ToolbarSlot

   

   .. data:: LEFT = siege.component.ToolbarSlot.LEFT

   .. data:: RIGHT = siege.component.ToolbarSlot.RIGHT

ActiveEffect
-----------------------------------
.. class:: ActiveEffect

   

   .. method:: __init__( )

      

   .. attribute:: effect

      

   .. attribute:: level

      

   .. attribute:: name

      

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

   .. method:: __init__( )

      

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

   

   .. method:: __init__( )

      

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

   

   .. method:: __init__( )

      

   .. method:: __setattr__( attr, value)

      

      :param attr: 

      :type attr: str

      :param value: 

      :type value: object

   .. method:: clean( )

      

   .. method:: create( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: destroy( )

      

   .. method:: dirty( )

      

   .. method:: freeze( )

      

   .. method:: fullDirty( )

      

   .. method:: getCid( )

      

      :rtype: int

   .. method:: getCid( )

      

   .. method:: getParent( )

      

      :rtype: :class:`Entity`

   .. method:: getType( )

      

      :rtype: str

   .. method:: getType( )

      

   .. method:: getVersion( )

      

      :rtype: int

   .. method:: getVersion( )

      

   .. method:: isDirty( )

      

      :rtype: bool

   .. method:: pack( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: read( stream, version)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param version: 

      :type version: int

   .. method:: restore( state)

      

      :param state: 

      :type state: int

   .. method:: save( state)

      

      :param state: 

      :type state: int

   .. method:: unpack( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: update( frameTime)

      

      :param frameTime: 

      :type frameTime: int

   .. method:: validate( )

      

      :rtype: bool

   .. method:: write( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

AnimationComponent
-----------------------------------
.. class:: AnimationComponent

   

   .. method:: clearQueue( [group=''])

      

      :param group: 

      :type group: str

   .. method:: getAnimationLength( arg2)

      

      :param arg2: 

      :type arg2: str

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

   .. method:: hide( [group=''])

      

      :param group: 

      :type group: str

   .. method:: hold( [group=''])

      

      :param group: 

      :type group: str

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

   .. method:: pause( [group=''])

      

      :param group: 

      :type group: str

   .. method:: play( [name=''[, group=''[, forceRestart=False]]])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

      :param forceRestart: 

      :type forceRestart: bool

   .. method:: queue( name[, group=''])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

   .. method:: scale( totalDelay[, group=''[, downOnly=True]])

      

      :param totalDelay: 

      :type totalDelay: int

      :param group: 

      :type group: str

      :param downOnly: 

      :type downOnly: bool

   .. method:: stop( [group=''])

      

      :param group: 

      :type group: str

   .. method:: wasPlaying( name[, group=''])

      

      :param name: 

      :type name: str

      :param group: 

      :type group: str

      :rtype: bool

   .. attribute:: onFinished

      

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

   .. method:: getExperienceToLevel( )

      

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

   .. method:: setCooldown( cooldown)

      

      :param cooldown: 

      :type cooldown: :class:`Cooldown`

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

   .. attribute:: cooldowns

      

   .. attribute:: experience

      

   .. attribute:: experienceYield

      

   .. attribute:: isAlive

      

   .. attribute:: isHitStunned

      

   .. attribute:: isInvincible

      

   .. attribute:: isTargetable

      

   .. attribute:: knockback

      

   .. attribute:: knockbackModifier

      

   .. attribute:: level

      

   .. attribute:: levels

      

   .. attribute:: numberOffset

      

   .. attribute:: onDamageSound

      

   .. attribute:: onDeathSound

      

   .. attribute:: onExpiredCooldown

      

   .. attribute:: onHit

      

   .. attribute:: onSetCooldown

      

   .. attribute:: onStatusChange

      

   .. attribute:: status

      

   .. attribute:: team

      

   .. attribute:: timeSinceCombat

      

CraftComponent
-----------------------------------
.. class:: CraftComponent

   

   .. attribute:: category

      

   .. attribute:: experience

      

   .. attribute:: isResearchable

      

   .. attribute:: level

      

   .. attribute:: materials

      

   .. attribute:: onCraft

      

   .. attribute:: results

      

   .. attribute:: serviceRequired

      

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

      

   .. attribute:: quantity

      

EffectsComponent
-----------------------------------
.. class:: EffectsComponent

   

   .. method:: add( effect, level, duration)

      

      :param effect: 

      :type effect: str

      :param level: 

      :type level: int

      :param duration: 

      :type duration: int

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

   .. method:: remove( effect[, duration=0])

      

      :param effect: 

      :type effect: str

      :param duration: 

      :type duration: int

   .. attribute:: onAddEffect

      

   .. attribute:: onRemoveEffect

      

   .. attribute:: onUpdateEffect

      

EquipmentComponent
-----------------------------------
.. class:: EquipmentComponent

   

   .. method:: addAttribute( attribute[, ignoreMax=False])

      

      :param attribute: 

      :type attribute: object

      :param ignoreMax: 

      :type ignoreMax: bool

   .. method:: getAttributes( )

      

      :rtype: :class:`EquipmentAttributes`

   .. method:: getModifiedName( )

      

      :rtype: str

   .. method:: getSlot( )

      

      :rtype: str

   .. method:: getSubstitutions( )

      

      :rtype: :class:`SubstitutionMap`

   .. method:: hasAttribute( type)

      

      :param type: 

      :type type: str

      :rtype: bool

   .. method:: isFull( )

      

      :rtype: bool

   .. method:: removeAttribute( attribute)

      

      :param attribute: 

      :type attribute: object

   .. attribute:: levelRequired

      

   .. attribute:: maxAttributes

      

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

   

   .. method:: getCompatableTiles( )

      

      :rtype: list

   .. method:: getTimeToUpdate( )

      

      :rtype: int

   .. attribute:: foliageType

      

   .. attribute:: growthType

      

   .. attribute:: particlePath

      

   .. attribute:: priority

      

GearComponent
-----------------------------------
.. class:: GearComponent

   

   .. method:: __getattr__( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: object

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

   .. method:: isEnabled( slot)

      

      :param slot: 

      :type slot: str

      :rtype: bool

   .. method:: resetGraphics( )

      

   .. method:: unequip( slotName)

      

      :param slotName: 

      :type slotName: str

      :rtype: :class:`InventoryItem`

   .. attribute:: onChange

      

   .. attribute:: ordered

      

InventoryComponent
-----------------------------------
.. class:: InventoryComponent

   

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

   .. method:: getBags( )

      

      :rtype: :class:`ItemBags`

   .. method:: getContentQuantity( content)

      

      :param content: 

      :type content: :class:`Content`

      :rtype: int

   .. method:: handleChange( bagIndex, index, previous, item)

      

      :param bagIndex: 

      :type bagIndex: int

      :param index: 

      :type index: int

      :param previous: 

      :type previous: :class:`InventoryItem`

      :param item: 

      :type item: :class:`InventoryItem`

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

   .. method:: remove( content[, quantity=1])

      

      :param content: 

      :type content: :class:`Content`

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

   

   .. attribute:: buyPrice

      

   .. attribute:: cooldown

      

   .. attribute:: description

      

   .. attribute:: features

      

   .. attribute:: flavor

      

   .. attribute:: hold

      

   .. attribute:: isDiscovered

      

   .. attribute:: isUnique

      

   .. attribute:: isUsable

      

   .. attribute:: quality

      

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

      

   .. attribute:: layer

      

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

   .. method:: setImage( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`ModularSprite`

   .. attribute:: axis

      

   .. attribute:: habitables

      

   .. attribute:: organic

      

   .. attribute:: size

      

PhysicsComponent
-----------------------------------
.. class:: PhysicsComponent

   

   .. method:: addPassingThrough( physics)

      

      :param physics: 

      :type physics: :class:`PhysicsComponent`

   .. method:: addTouching( direction)

      

      :param direction: 

      :type direction: :class:`Direction`

   .. method:: calculateJumpHeight( speed, height)

      

      :param speed: 

      :type speed: float

      :param height: 

      :type height: float

      :rtype: float

   .. method:: clearPassingThrough( )

      

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

      

   .. attribute:: jumpTimer

      

   .. attribute:: onTimeStep

      

   .. attribute:: sleeping

      

TilePhysicsComponent
-----------------------------------
.. class:: TilePhysicsComponent

   

PlacementComponent
-----------------------------------
.. class:: PlacementComponent

   

   .. method:: getArea( )

      

      :rtype: :class:`Rect`

   .. method:: getDropped( )

      

      :rtype: str

   .. method:: getRect( )

      

      :rtype: :class:`PixelRect`

   .. method:: getSupports( )

      

      :rtype: object

   .. method:: setPlacement( placement)

      

      :param placement: 

      :type placement: :class:`PlacementComponent`

   .. attribute:: allowCollection

      

   .. attribute:: allowSupportRemoval

      

   .. attribute:: axes

      

   .. attribute:: axis

      

   .. attribute:: supportEntity

      

   .. attribute:: supportTiles

      

PlayerStateComponent
-----------------------------------
.. class:: PlayerStateComponent

   

   .. attribute:: activeItem

      

   .. attribute:: canMove

      

   .. attribute:: perseveranceTime

      

   .. attribute:: perseveranceTimerJob

      

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

   .. method:: setOrigin( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: setOriginToCenter( )

      

   .. method:: setRotation( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: setTexture( arg2)

      

      :param arg2: 

      :type arg2: :class:`Texture`

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

   .. attribute:: onMove

      

   .. attribute:: sprite

      

   .. attribute:: states

      

ModularRenderComponent
-----------------------------------
.. class:: ModularRenderComponent

   

   .. method:: addTexture( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: str

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

   .. method:: render( target[, realmHalfWidth=0])

      

      :param target: 

      :type target: :class:`sfRenderTarget`

      :param realmHalfWidth: 

      :type realmHalfWidth: int

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

   .. attribute:: alpha

      

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

   .. method:: getTileId( )

      

      :rtype: int

   .. method:: isCompatible( compatibles)

      

      :param compatibles: 

      :type compatibles: list

      :rtype: bool

   .. attribute:: canPlace

      

   .. attribute:: durability

      

   .. attribute:: isFragile

      

   .. attribute:: isReplaceable

      

   .. attribute:: isSolid

      

   .. attribute:: level

      

   .. attribute:: particleColor

      

   .. attribute:: providesSupport

      

ToolComponent
-----------------------------------
.. class:: ToolComponent

   

   .. attribute:: compatible

      

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

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`ToolbarItem`

   .. method:: get( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`ToolbarSlot`

      :rtype: :class:`ToolItem`

   .. method:: isEmpty( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`ToolbarSlot`

      :rtype: bool

   .. method:: set( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`ToolbarSlot`

      :param arg4: 

      :type arg4: :class:`ToolItem`

   .. attribute:: onChange

      

   .. attribute:: onSelectedChange

      

   .. attribute:: selected

      

   .. attribute:: size

      

   .. attribute:: tools

      

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

      

   .. attribute:: damageType

      

   .. attribute:: onUse

      

   .. attribute:: power

      

ComponentDefinition
-----------------------------------
.. class:: ComponentDefinition

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: freeze( )

      

   .. method:: getType( )

      

      :rtype: str

   .. method:: getType( )

      

   .. method:: read( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: set( attr, kwargs)

      

      :param attr: 

      :type attr: str

      :param kwargs: 

      :type kwargs: dict

   .. method:: set( attr, kwargs)

      

      :param attr: 

      :type attr: list

      :param kwargs: 

      :type kwargs: dict

   .. method:: write( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. attribute:: isFrozen

      

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

   .. attribute:: experienceYield

      

   .. attribute:: knockbackModifier

      

   .. attribute:: levels

      

   .. attribute:: numberOffset

      

   .. attribute:: onDamageSound

      

   .. attribute:: onDeath

      

   .. attribute:: onDeathSound

      

   .. attribute:: onLevelUp

      

   .. attribute:: team

      

Craft
-----------------------------------
.. class:: Craft

   

   .. method:: __init__( [category=''[, subcategory=''[, level=1[, experience=0[, serviceRequired='']]]]])

      

      :param category: 

      :type category: str

      :param subcategory: 

      :type subcategory: str

      :param level: 

      :type level: int

      :param experience: 

      :type experience: int

      :param serviceRequired: 

      :type serviceRequired: str

   .. method:: insertMaterial( itemPath, quantity)

      

      :param itemPath: 

      :type itemPath: str

      :param quantity: 

      :type quantity: int

   .. method:: material( itemPath, quantity)

      

      :param itemPath: 

      :type itemPath: str

      :param quantity: 

      :type quantity: int

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

      

   .. attribute:: results

      

   .. attribute:: serviceRequired

      

   .. attribute:: subcategory

      

Dropped
-----------------------------------
.. class:: Dropped

   

   .. method:: __init__( )

      

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

   

   .. method:: __init__( )

      

Event
-----------------------------------
.. class:: Event

   

   .. method:: __getitem__( name)

      

      :param name: 

      :type name: str

      :rtype: :class:`GameEvent`

   .. method:: __init__( )

      

   .. attribute:: events

      

Foliage
-----------------------------------
.. class:: Foliage

   

   .. method:: __init__( )

      

   .. attribute:: compatibleTiles

      

   .. attribute:: drops

      

   .. attribute:: foliageNeighbors

      

   .. attribute:: foliageType

      

   .. attribute:: growChance

      

   .. attribute:: growDepth

      

   .. attribute:: growthDirections

      

   .. attribute:: growthType

      

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

   

   .. method:: __init__( )

      

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

   

   .. method:: __init__( )

      

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

      

   .. attribute:: cooldown

      

   .. attribute:: discovered

      

   .. attribute:: features

      

   .. attribute:: hold

      

   .. attribute:: quality

      

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

   

   .. method:: __init__( )

      

Light
-----------------------------------
.. class:: Light

   

   .. method:: __init__( )

      

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

      

   .. attribute:: layer

      

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

      

Physics
-----------------------------------
.. class:: Physics

   

   .. method:: __init__( )

      

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

      

   .. attribute:: dropped

      

PlayerState
-----------------------------------
.. class:: PlayerState

   

   .. method:: __init__( )

      

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

      

   .. attribute:: rotation

      

   .. attribute:: scale

      

   .. attribute:: wicon

      

Reserves
-----------------------------------
.. class:: Reserves

   

   .. method:: __init__( )

      

Stats
-----------------------------------
.. class:: Stats

   

   .. method:: __init__( )

      

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

   

   .. method:: __init__( [slot=''[, levelRequired=0]])

      

      :param slot: 

      :type slot: str

      :param levelRequired: 

      :type levelRequired: int

   .. attribute:: canEquip

      

   .. attribute:: levelRequired

      

   .. attribute:: onCreate

      

   .. attribute:: onEquip

      

   .. attribute:: onUnequip

      

   .. attribute:: paths

      

   .. attribute:: potentials

      

   .. attribute:: slot

      

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

   

   .. method:: __init__( )

      

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

   .. attribute:: canPlace

      

   .. attribute:: collisions

      

   .. attribute:: dropped

      

   .. attribute:: durability

      

   .. attribute:: fragile

      

   .. attribute:: groups

      

   .. attribute:: layer

      

   .. attribute:: level

      

   .. attribute:: mapGroundColor

      

   .. attribute:: mapWallColor

      

   .. attribute:: onBreakSound

      

   .. attribute:: onHitSound

      

   .. attribute:: onlyAutotileWithSelf

      

   .. attribute:: opacity

      

   .. attribute:: particleColor

      

   .. attribute:: passthrough

      

   .. attribute:: priority

      

   .. attribute:: replaceable

      

   .. attribute:: simple

      

   .. attribute:: solid

      

   .. attribute:: stable

      

   .. attribute:: standard

      

   .. attribute:: support

      

   .. attribute:: variants

      

Tool
-----------------------------------
.. class:: Tool

   

   .. method:: __init__( [power=0[, reach=0[, compatible=[]]]])

      

      :param power: 

      :type power: int

      :param reach: 

      :type reach: int

      :param compatible: 

      :type compatible: list

   .. attribute:: compatible

      

   .. attribute:: power

      

   .. attribute:: reach

      

Toolbar
-----------------------------------
.. class:: Toolbar

   

   .. method:: __init__( )

      

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

   .. staticmethod:: create( arg1)

      

      :param arg1: 

      :type arg1: object

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

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

   .. method:: __init__( )

      

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

   

   .. method:: __init__( name, category, icon)

      

      :param name: 

      :type name: str

      :param category: 

      :type category: str

      :param icon: 

      :type icon: object

   .. attribute:: category

      

   .. attribute:: enabled

      

   .. attribute:: icon

      

   .. attribute:: item

      

   .. attribute:: name

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

ModularRenderSprite
-----------------------------------
.. class:: ModularRenderSprite

   

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

      

   .. attribute:: axis

      

   .. attribute:: layer

      

   .. attribute:: range

      

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

   

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

StringList
-----------------------------------
.. class:: StringList

   

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

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

   .. method:: __init__( )

      

   .. method:: __iter__( )

      

      :rtype: object

   .. method:: __len__( )

      

      :rtype: int

   .. method:: __setitem__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

ToolbarItem
-----------------------------------
.. class:: ToolbarItem

   

   .. method:: __init__( )

      

   .. attribute:: left

      

   .. attribute:: right

      

ToolbarItemList
-----------------------------------
.. class:: ToolbarItemList

   

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

   .. method:: __init__( )

      

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

