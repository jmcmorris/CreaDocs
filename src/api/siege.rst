.. _siege:

siege
==================

GrabbedItemLocation
-----------------------------------
.. class:: GrabbedItemLocation

   

   .. data:: BAG = siege.GrabbedItemLocation.BAG

   .. data:: BAGSLOT = siege.GrabbedItemLocation.BAGSLOT

   .. data:: CUSTOM = siege.GrabbedItemLocation.CUSTOM

   .. data:: GADGET = siege.GrabbedItemLocation.GADGET

   .. data:: GEAR = siege.GrabbedItemLocation.GEAR

   .. data:: HAND = siege.GrabbedItemLocation.HAND

   .. data:: NONE = siege.GrabbedItemLocation.NONE

   .. data:: QUICKBAR = siege.GrabbedItemLocation.QUICKBAR

   .. data:: RESERVE = siege.GrabbedItemLocation.RESERVE

   .. data:: SKILL = siege.GrabbedItemLocation.SKILL

   .. data:: TOOLBAR = siege.GrabbedItemLocation.TOOLBAR

PauseLocation
-----------------------------------
.. class:: PauseLocation

   

   .. data:: Custom = siege.PauseLocation.Custom

   .. data:: Focus = siege.PauseLocation.Focus

   .. data:: None = siege.PauseLocation.None

   .. data:: Option = siege.PauseLocation.Option

   .. data:: PauseNoPlayers = siege.PauseLocation.PauseNoPlayers

   .. data:: Steam = siege.PauseLocation.Steam

PlayMode
-----------------------------------
.. class:: PlayMode

   

   .. data:: Creative = siege.PlayMode.Creative

   .. data:: Easy = siege.PlayMode.Easy

   .. data:: Hardcore = siege.PlayMode.Hardcore

   .. data:: Normal = siege.PlayMode.Normal

SkillType
-----------------------------------
.. class:: SkillType

   

   .. data:: Active = siege.SkillType.Active

   .. data:: Passive = siege.SkillType.Passive

ActiveTalent
-----------------------------------
.. class:: ActiveTalent

   

   .. method:: gainPoints( amount)

      

      :param amount: 

      :type amount: int

   .. method:: get( skillName)

      

      :param skillName: 

      :type skillName: str

      :rtype: :class:`EngineSkill`

   .. method:: getLevelCap( )

      

      :rtype: int

   .. method:: getPointsToLevel( )

      

      :rtype: int

   .. method:: getSkills( )

      

      :rtype: :class:`SkillList`

   .. method:: has( skillName)

      

      :param skillName: 

      :type skillName: str

      :rtype: bool

   .. method:: isMaxLevel( )

      

      :rtype: bool

   .. method:: purchaseSkill( player, skill)

      

      :param player: 

      :type player: :class:`Player`

      :param skill: 

      :type skill: :class:`EngineSkill`

   .. attribute:: icon

      

   .. attribute:: level

      

   .. attribute:: locked

      

   .. attribute:: name

      

   .. attribute:: onSkillChanged

      

   .. attribute:: points

      

   .. attribute:: stored

      

Camera
-----------------------------------
.. class:: Camera

   

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RenderSystem`

   .. method:: attachTo( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: :class:`sfView`

      :param arg4: 

      :type arg4: :class:`Vector`

      :param arg5: 

      :type arg5: :class:`RealmSize`

   .. method:: reset( )

      

   .. method:: setPosition( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

   .. attribute:: entity

      

   .. attribute:: movement

      

   .. attribute:: position

      

   .. attribute:: windowSize

      

CharacterInfo
-----------------------------------
.. class:: CharacterInfo

   

   .. method:: __init__( )

      

   .. attribute:: body

      

   .. attribute:: customizations

      

   .. attribute:: level

      

   .. attribute:: name

      

   .. attribute:: playtime

       |      Tracks playtime in seconds


ContentData
-----------------------------------
.. class:: ContentData

   

   .. method:: __init__( )

      

   .. attribute:: components

      

   .. attribute:: name

      

   .. attribute:: persistent

      

ContentDataMap
-----------------------------------
.. class:: ContentDataMap

   

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

Cooldown
-----------------------------------
.. class:: Cooldown

   

   .. method:: __init__( )

      

   .. method:: __init__( key, duration)

      

      :param key: 

      :type key: str

      :param duration: 

      :type duration: int

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Cooldown`

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. attribute:: duration

      

   .. attribute:: key

      

CustomizationInfo
-----------------------------------
.. class:: CustomizationInfo

   

   .. method:: __init__( )

      

   .. method:: read( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. method:: write( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: content

      

   .. attribute:: group

      

   .. attribute:: hsl

      

CustomizationInfoList
-----------------------------------
.. class:: CustomizationInfoList

   

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

DynamicStat
-----------------------------------
.. class:: DynamicStat

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: adjust( value)

      

      :param value: 

      :type value: float

      :rtype: float

   .. method:: adjustMax( value)

      

      :param value: 

      :type value: float

      :rtype: float

   .. method:: get( )

      

      :rtype: float

   .. method:: getMax( )

      

      :rtype: float

   .. method:: getRaw( )

      

      :rtype: float

   .. method:: getRawMax( )

      

      :rtype: float

   .. method:: hasMax( )

      

      :rtype: bool

   .. method:: isFull( )

      

      :rtype: bool

   .. method:: mod( value[, isMultiplier=False])

      

      :param value: 

      :type value: float

      :param isMultiplier: 

      :type isMultiplier: bool

      :rtype: int

   .. method:: mod( key, value[, isMultiplier=False])

      

      :param key: 

      :type key: str

      :param value: 

      :type value: float

      :param isMultiplier: 

      :type isMultiplier: bool

   .. method:: set( value)

      

      :param value: 

      :type value: float

   .. method:: setMax( value)

      

      :param value: 

      :type value: float

   .. method:: unmod( uid)

      

      :param uid: 

      :type uid: int

   .. method:: unmod( key)

      

      :param key: 

      :type key: str

   .. attribute:: fullName

      

   .. attribute:: isVisible

      

   .. attribute:: name

      

   .. attribute:: onChange

      

   .. attribute:: onChangeMax

      

EngineSkill
-----------------------------------
.. class:: EngineSkill

   

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: getCost( )

      

      :rtype: int

   .. method:: getLevelCap( )

      

      :rtype: int

   .. method:: isMaxLevel( )

      

      :rtype: bool

   .. attribute:: canRepeatUse

      

   .. attribute:: cooldown

      

   .. attribute:: costs

      

   .. attribute:: getDescription

      

   .. attribute:: getIcon

      

   .. attribute:: getModifiers

      

   .. attribute:: getName

      

   .. attribute:: icon

      

   .. attribute:: isAvailable

      

   .. attribute:: isUsable

      

   .. attribute:: level

      

   .. attribute:: name

      

   .. attribute:: onActivate

      

   .. attribute:: onDeactivate

      

   .. attribute:: onUse

      

   .. attribute:: type

      

   .. attribute:: unlockLevel

      

Entities
-----------------------------------
.. class:: Entities

   

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

Entity
-----------------------------------
.. class:: Entity

   

   .. method:: __eq__( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: __getattr__( attr)

      

      :param attr: 

      :type attr: str

      :rtype: object

   .. method:: __init__( name, id, content, persistent)

      

      :param name: 

      :type name: str

      :param id: 

      :type id: int

      :param content: 

      :type content: :class:`Content`

      :param persistent: 

      :type persistent: bool

   .. method:: __neq__( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: add( component)

      

      :param component: 

      :type component: :class:`Component`

   .. method:: destroy( [unload=False])

      

      :param unload: 

      :type unload: bool

   .. method:: get( componentType)

      

      :param componentType: 

      :type componentType: str

      :rtype: :class:`Component`

   .. method:: get( cid)

      

      :param cid: 

      :type cid: int

      :rtype: :class:`Component`

   .. method:: getName( )

      

      :rtype: str

   .. method:: getPosition( )

      

      :rtype: :class:`Vector`

   .. method:: getRender( )

      

      :rtype: :class:`RenderComponent`

   .. method:: has( componentType)

      

      :param componentType: 

      :type componentType: str

      :rtype: bool

   .. method:: has( cid)

      

      :param cid: 

      :type cid: int

      :rtype: bool

   .. method:: hasRealm( )

      

      :rtype: bool

   .. method:: isContentEntity( )

      

      :rtype: bool

   .. method:: isDestroyed( )

      

      :rtype: bool

   .. method:: isPlayer( )

      

      :rtype: bool

   .. method:: remove( component)

      

      :param component: 

      :type component: :class:`Component`

   .. method:: remove( componentType)

      

      :param componentType: 

      :type componentType: str

   .. method:: setInitialPosition( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: setName( name)

      

      :param name: 

      :type name: str

   .. method:: setPosition( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. attribute:: components

      

   .. attribute:: content

      

   .. attribute:: id

      

   .. attribute:: layer

      

   .. attribute:: loopWidth

      

   .. attribute:: name

      

   .. attribute:: onDestroyed

      

   .. attribute:: persistent

      

   .. attribute:: realm

      

   .. attribute:: realmUid

      

EntityManager
-----------------------------------
.. class:: EntityManager

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: addComponent( entity, definition)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param definition: 

      :type definition: object

   .. method:: associate( contentObject)

      

      :param contentObject: 

      :type contentObject: object

      :rtype: :class:`Content`

   .. method:: create( [components=[]])

      

      :param components: 

      :type components: :class:`Content`

      :rtype: :class:`Entity`

   .. method:: destroy( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: destroyCreatedCharacter( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`Entity`

   .. method:: getContentEntity( contentName)

      

      :param contentName: 

      :type contentName: str

      :rtype: :class:`Entity`

   .. method:: getContentEntity( content)

      

      :param content: 

      :type content: :class:`Content`

      :rtype: :class:`Entity`

   .. method:: getDefinition( cid)

      

      :param cid: 

      :type cid: int

      :rtype: object

   .. method:: getDefinition( type)

      

      :param type: 

      :type type: str

      :rtype: object

   .. method:: hasDefinition( cid)

      

      :param cid: 

      :type cid: int

      :rtype: bool

   .. method:: hasDefinition( type)

      

      :param type: 

      :type type: str

      :rtype: bool

   .. method:: initialize( )

      

   .. method:: reloadContentEntities( content)

      

      :param content: 

      :type content: :class:`Content`

   .. method:: removeComponent( entity, component)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param component: 

      :type component: :class:`Component`

   .. method:: requestCid( componentType, definition)

      

      :param componentType: 

      :type componentType: str

      :param definition: 

      :type definition: object

      :rtype: int

   .. method:: reset( )

      

   .. attribute:: contentComponents

      

EntitySet
-----------------------------------
.. class:: EntitySet

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

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

   .. method:: add( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: clear( )

      

   .. method:: has( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :rtype: bool

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

Game
-----------------------------------
.. class:: Game

   

   .. method:: __getattr__( attr)

      

      :param attr: 

      :type attr: str

      :rtype: object

   .. method:: __init__( )

      

   .. method:: abort( error)

      

      :param error: 

      :type error: str

   .. method:: broadcastMessage( message)

      

      :param message: 

      :type message: str

   .. method:: cleanup( )

      

   .. method:: exit( )

      

   .. method:: getMousePosition( )

      

      :rtype: :class:`PixelVector`

   .. method:: getSubsystem( subsystem)

      

      :param subsystem: 

      :type subsystem: str

      :rtype: :class:`Subsystem`

   .. method:: getSystem( system)

      

      :param system: 

      :type system: str

      :rtype: object

   .. method:: hasSystem( system)

      

      :param system: 

      :type system: str

      :rtype: bool

   .. method:: initialize( )

      

   .. method:: isOnTick( )

      

      :rtype: bool

   .. method:: openUrl( url[, forceBrowser=False])

      

      :param url: 

      :type url: str

      :param forceBrowser: 

      :type forceBrowser: bool

   .. method:: pause( arg2)

      

      :param arg2: 

      :type arg2: :class:`PauseLocation`

   .. method:: registerComponent( name, factory)

      

      :param name: 

      :type name: str

      :param factory: 

      :type factory: :class:`ComponentFactory`

   .. method:: registerSubsystem( subsystem, subsystemName, component)

      

      :param subsystem: 

      :type subsystem: :class:`Subsystem`

      :param subsystemName: 

      :type subsystemName: str

      :param component: 

      :type component: str

   .. method:: registerSubsystem( subsystem, subsystemName, components)

      

      :param subsystem: 

      :type subsystem: :class:`Subsystem`

      :param subsystemName: 

      :type subsystemName: str

      :param components: 

      :type components: :class:`StringList`

   .. method:: registerSystem( subsystemName, system)

      

      :param subsystemName: 

      :type subsystemName: str

      :param system: 

      :type system: object

   .. method:: reinitialize( )

      

   .. method:: requestTextInput( description, maxCharacters, currentText, isPassword, callback)

      

      :param description: 

      :type description: str

      :param maxCharacters: 

      :type maxCharacters: int

      :param currentText: 

      :type currentText: str

      :param isPassword: 

      :type isPassword: bool

      :param callback: 

      :type callback: object

   .. method:: reset( )

      

   .. method:: resume( arg2)

      

      :param arg2: 

      :type arg2: :class:`PauseLocation`

   .. method:: sendMessage( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :param arg3: 

      :type arg3: str

   .. method:: setMousePosition( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

   .. method:: sleep( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: unregisterSubsystem( subsystemName)

      

      :param subsystemName: 

      :type subsystemName: str

   .. method:: unregisterSystem( subsystemName)

      

      :param subsystemName: 

      :type subsystemName: str

   .. staticmethod:: get( )

      

      :rtype: :class:`Game`

   .. attribute:: achievements

      

   .. attribute:: args

      

   .. attribute:: audio

      

   .. attribute:: configDirectory

      

   .. attribute:: content

      

   .. attribute:: data

      

   .. attribute:: entity

      

   .. attribute:: events

      

   .. attribute:: file

      

   .. attribute:: gui

      

   .. attribute:: hasFocus

      

   .. attribute:: hasInputFocus

      

   .. attribute:: isPaused

      

   .. attribute:: network

      

   .. attribute:: onUnregistration

      

   .. attribute:: onUpdate

      

   .. attribute:: particles

      

   .. attribute:: profiler

      

   .. attribute:: renderCursor

      

   .. attribute:: scene

      

   .. attribute:: state

      

   .. attribute:: steamUid

      

   .. attribute:: version

      

GrabbedItem
-----------------------------------
.. class:: GrabbedItem

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`GrabbedItem`

      :rtype: bool

   .. method:: __init__( )

      

   .. method:: __init__( item)

      

      :param item: 

      :type item: :class:`GrabbedItem`

   .. method:: __nonzero__( )

      

      :rtype: bool

   .. method:: read( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

      :param arg3: 

      :type arg3: :class:`ContentStash`

      :param arg4: 

      :type arg4: :class:`EntityManager`

      :param arg5: 

      :type arg5: :class:`Player`

   .. method:: write( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

      :param arg3: 

      :type arg3: :class:`ContentStash`

      :param arg4: 

      :type arg4: :class:`EntityManager`

   .. attribute:: bagIndex

      

   .. attribute:: customLocation

      

   .. attribute:: elapsed

      

   .. attribute:: entity

      

   .. attribute:: index

      

   .. attribute:: item

      

   .. attribute:: location

      

   .. attribute:: reserve

      

   .. attribute:: slot

      

Integrity
-----------------------------------
.. class:: Integrity

   

   .. method:: __init__( )

      

   .. staticmethod:: checkModule( arg1)

      

      :param arg1: 

      :type arg1: object

      :rtype: bool

   .. staticmethod:: checkPath( arg1)

      

      :param arg1: 

      :type arg1: str

      :rtype: bool

   .. staticmethod:: create( arg1)

      

      :param arg1: 

      :type arg1: list

   .. staticmethod:: isEnabled( )

      

      :rtype: bool

   .. staticmethod:: isValid( )

      

      :rtype: bool

   .. staticmethod:: load( )

      

InventoryItem
-----------------------------------
.. class:: InventoryItem

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`InventoryItem`

      :rtype: object

   .. method:: __init__( content[, quantity=1])

      

      :param content: 

      :type content: :class:`Content`

      :param quantity: 

      :type quantity: int

   .. method:: __init__( )

      

   .. method:: __init__( contentName[, quantity=1])

      

      :param contentName: 

      :type contentName: str

      :param quantity: 

      :type quantity: int

   .. method:: __init__( entity[, quantity=1])

      

      :param entity: 

      :type entity: :class:`Entity`

      :param quantity: 

      :type quantity: int

   .. method:: __init__( entity, contentName[, quantity=1])

      

      :param entity: 

      :type entity: :class:`Entity`

      :param contentName: 

      :type contentName: :class:`Content`

      :param quantity: 

      :type quantity: int

   .. method:: __init__( item)

      

      :param item: 

      :type item: :class:`InventoryItem`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`InventoryItem`

      :rtype: object

   .. method:: __nonzero__( )

      

      :rtype: bool

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: getContentId( )

      

      :rtype: int

   .. method:: pack( stream, contentStash)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

   .. method:: read( stream, contentStash, entityManager)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

   .. method:: swap( item)

      

      :param item: 

      :type item: :class:`InventoryItem`

   .. method:: unpack( stream, contentStash, entityManager)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

   .. method:: write( arg2, stream, contentStash)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

      :param stream: 

      :type stream: :class:`ContentStash`

      :param contentStash: 

      :type contentStash: :class:`EntityManager`

   .. staticmethod:: stackItems( base, held, entityManager)

      

      :param base: 

      :type base: :class:`InventoryItem`

      :param held: 

      :type held: :class:`InventoryItem`

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

      :rtype: bool

   .. attribute:: content

      

   .. attribute:: entity

       |      (:class:`Entity`)


   .. attribute:: quantity

      

ItemGenus
-----------------------------------
.. class:: ItemGenus

   

   .. method:: __init__( content[, quantity=1])

      

      :param content: 

      :type content: :class:`Content`

      :param quantity: 

      :type quantity: int

   .. method:: __init__( )

      

   .. method:: __init__( contentName[, quantity=1])

      

      :param contentName: 

      :type contentName: str

      :param quantity: 

      :type quantity: int

   .. method:: __init__( entity[, quantity=1])

      

      :param entity: 

      :type entity: :class:`Entity`

      :param quantity: 

      :type quantity: int

   .. method:: __init__( entity, contentName[, quantity=1])

      

      :param entity: 

      :type entity: :class:`Entity`

      :param contentName: 

      :type contentName: :class:`Content`

      :param quantity: 

      :type quantity: int

   .. method:: __init__( item)

      

      :param item: 

      :type item: :class:`ItemGenus`

   .. attribute:: genus

      

ToolItem
-----------------------------------
.. class:: ToolItem

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ToolItem`

      :rtype: bool

   .. method:: __init__( )

      

   .. method:: __init__( item)

      

      :param item: 

      :type item: :class:`InventoryItem`

   .. method:: __init__( talent, skill)

      

      :param talent: 

      :type talent: :class:`ActiveTalent`

      :param skill: 

      :type skill: :class:`EngineSkill`

   .. method:: __nonzero__( )

      

      :rtype: bool

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: getCooldown( )

      

      :rtype: :class:`Cooldown`

   .. method:: getIconPath( player)

      

      :param player: 

      :type player: :class:`Player`

      :rtype: str

   .. method:: isItem( )

      

      :rtype: bool

   .. method:: isSkill( )

      

      :rtype: bool

   .. method:: pack( stream, contentStash)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

   .. method:: read( arg2, stream, contentStash, entityManager, player)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

      :param stream: 

      :type stream: :class:`ContentStash`

      :param contentStash: 

      :type contentStash: :class:`EntityManager`

      :param entityManager: 

      :type entityManager: :class:`Player`

      :param player: 

      :type player: int

   .. method:: unpack( stream, contentStash, entityManager, player)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

      :param player: 

      :type player: :class:`Player`

   .. method:: write( arg2, stream, contentStash)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

      :param stream: 

      :type stream: :class:`ContentStash`

      :param contentStash: 

      :type contentStash: :class:`EntityManager`

   .. attribute:: skill

       |      (:class:`Skill`)


   .. attribute:: talent

       |      (:class:`Talent`)


ItemBag
-----------------------------------
.. class:: ItemBag

   

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`Entity`

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: add( entity, quantity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: addToEmptySlot( entity, quantity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: canAdd( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: clear( )

      

   .. method:: clear( index)

      

      :param index: 

      :type index: int

   .. method:: decrement( index, quantity)

      

      :param index: 

      :type index: int

      :param quantity: 

      :type quantity: int

   .. method:: fullDirty( )

      

   .. method:: get( index)

      

      :param index: 

      :type index: int

      :rtype: :class:`InventoryItem`

   .. method:: getContentQuantity( content)

      

      :param content: 

      :type content: :class:`Content`

      :rtype: int

   .. method:: hasContent( content)

      

      :param content: 

      :type content: :class:`Content`

      :rtype: bool

   .. method:: hasUniqueItem( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: isEmpty( )

      

      :rtype: bool

   .. method:: isEmpty( index)

      

      :param index: 

      :type index: int

      :rtype: bool

   .. method:: pack( stream, contentStash)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

   .. method:: read( stream, contentStash, entityManager)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

   .. method:: remove( entity, quantity)

      

      :param entity: 

      :type entity: :class:`Content`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: remove( entity, quantity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: resize( size)

      

      :param size: 

      :type size: int

   .. method:: set( index, item)

      

      :param index: 

      :type index: int

      :param item: 

      :type item: :class:`InventoryItem`

   .. method:: stack( entity, quantity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: unpack( stream, contentStash, entityManager)

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

   .. method:: write( arg2, stream, contentStash)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

      :param stream: 

      :type stream: :class:`ContentStash`

      :param contentStash: 

      :type contentStash: :class:`EntityManager`

   .. attribute:: entity

      

   .. attribute:: index

      

   .. attribute:: items

      

   .. attribute:: onChange

      

   .. attribute:: openSlots

      

   .. attribute:: size

      

ItemList
-----------------------------------
.. class:: ItemList

   

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

Locale
-----------------------------------
.. class:: Locale

   

   .. staticmethod:: get( text)

      

      :param text: 

      :type text: str

      :rtype: str

   .. staticmethod:: getEscaped( text)

      

      :param text: 

      :type text: str

      :rtype: str

   .. staticmethod:: getFont( name)

      

      :param name: 

      :type name: str

      :rtype: str

   .. staticmethod:: getLocale( )

      

      :rtype: str

   .. staticmethod:: getLocales( arg1)

      

      :param arg1: 

      :type arg1: :class:`Packages`

      :rtype: dict

   .. staticmethod:: has( text)

      

      :param text: 

      :type text: str

      :rtype: bool

   .. staticmethod:: setLocale( locale, packages)

      

      :param locale: 

      :type locale: str

      :param packages: 

      :type packages: :class:`Packages`

Player
-----------------------------------
.. class:: Player

   

   .. method:: __init__( )

      

   .. method:: applySubstitutions( substitutions, hsl, paths)

      

      :param substitutions: 

      :type substitutions: :class:`SubstitutionMap`

      :param hsl: 

      :type hsl: :class:`Vector3`

      :param paths: 

      :type paths: :class:`StringList`

   .. method:: attachHeldItems( [removeAnimationHandler=True])

      

      :param removeAnimationHandler: 

      :type removeAnimationHandler: bool

   .. method:: attemptEquip( slot, item)

      Attempts to equip the item to the player.


      :param slot:  Name of the equipment slot.


      :type slot: str

      :param item:  The item to equip. If successful this item contents is swapped with the item currently equipped in the specified slot.


      :type item: :class:`InventoryItem`

      :returns: Whether the item was successfully equipped or not.


      :rtype: bool


   .. method:: canEquip( slot, item)

      Checks to see if an item can be equipped by the player.


      :param slot:  Name of the equipment slot.


      :type slot: str

      :param item:  The item to check if it is equippable.


      :type item: :class:`InventoryItem`

      :returns: Whether the player can equip item or not.


      :rtype: bool


   .. method:: canSplitItem( item[, quantity=1])

      

      :param item: 

      :type item: :class:`InventoryItem`

      :param quantity: 

      :type quantity: int

      :rtype: bool

   .. method:: getHarvestPower( arg2)

      

      :param arg2: 

      :type arg2: :class:`ToolComponent`

      :rtype: int

   .. method:: getPath( )

      

      :rtype: str

   .. method:: getSplitItemQuantity( item, quantity)

      

      :param item: 

      :type item: :class:`InventoryItem`

      :param quantity: 

      :type quantity: int

      :rtype: int

   .. method:: getToolPower( arg2)

      

      :param arg2: 

      :type arg2: :class:`ToolComponent`

      :rtype: int

   .. method:: getToolReach( arg2)

      

      :param arg2: 

      :type arg2: :class:`ToolComponent`

      :rtype: int

   .. method:: isAggressive( )

      

      :rtype: bool

   .. method:: isPassive( )

      

      :rtype: bool

   .. method:: loadInfo( contentStash, entityManager, playerPath[, setupEntity=True])

      Loads the character information from the provided path.


      :param contentStash:  The :class:`ContentStash` provided by :class:`Game`.


      :type contentStash: :class:`ContentStash`

      :param entityManager:  The :class:`EntityManager` provided by :class:`Game`.


      :type entityManager: :class:`EntityManager`

      :param playerPath:  Path to the player's cpf file.


      :type playerPath:  str or unicode


      :param setupEntity: 

      :type setupEntity: bool

   .. method:: save( arg2, fileManager, contentStash, writers, asynchronous)

      Saves the character to file.


      :param arg2: 

      :type arg2: :class:`FileManager`

      :param fileManager:  (:class:`FileManager`) The file manager (game.file).


      :type fileManager: :class:`ContentStash`

      :param contentStash:  The :class:`ContentStash` provided by :class:`Game`.


      :type contentStash: :class:`EntityManager`

      :param writers:  A dictionary of {str: callable}. The callable should have the following signature ``(player, stream)``.


      :type writers: :class:`ObjectMap`

      :param asynchronous:  Set to true to force asynchronous file writing, false otherwise


      :type asynchronous: bool

   .. method:: setup( contentStash, entityManager, entityId)

      

      :param contentStash: 

      :type contentStash: :class:`ContentStash`

      :param entityManager: 

      :type entityManager: :class:`EntityManager`

      :param entityId: 

      :type entityId: int

   .. method:: showUseItem( position, index, slot, toolItem[, swapBackOnAnimationFinish=True])

      

      :param position: 

      :type position: :class:`Entity`

      :param index: 

      :type index: :class:`Vector`

      :param slot: 

      :type slot: bool

      :param toolItem: 

      :type toolItem: :class:`ToolItem`

      :param swapBackOnAnimationFinish: 

      :type swapBackOnAnimationFinish: bool

   .. method:: swapHeldItems( )

      

   .. attribute:: connectedTime

       |      (:class:`Clock`) Tracks the amount of time the player has been connected to this world.


   .. attribute:: data

       |      (dict) Container for miscellaneous player data.


   .. attribute:: directory

       |      Directory the character is saved into.


   .. attribute:: dirty

       |      (bool) Tracks if the player has data that needs to be sync'd from the server to client.


   .. attribute:: entity

       |      (:class:`Entity`) The :class:`Entity` instance for the :class:`Player`.


   .. attribute:: flipPlacedItems

       |      (bool) Whether or not placed items by player are flipped horizontally.


   .. attribute:: grabbed

       |      (:class:`GrabbedItem`) The item the player currently has grabbed with the mouse.


   .. attribute:: info

      

   .. attribute:: lastUsedItemTimer

       |      (:class:`Clock`) Tracks time since last used item.


   .. attribute:: mode

       |      (:class:`PlayMode`) The mode the :class:`Player` is in.


   .. attribute:: movement

       |      (:class:`Vector`) The distance moved over the last few seconds.


   .. attribute:: needsItemRestoration

      

   .. attribute:: networkId

       |      (:class:`NetworkId`) The :class:`NetworkId` associated with this player.


   .. attribute:: onGrabbedChange

       |      (:class:`GameEvent`) Invoked with ``(player, previousGrabbed, grabbed)`` when :attr:`grabbed` changes.


   .. attribute:: temp

       |      (dict) Container for temporary miscellaneous player data.


   .. attribute:: timeSinceLastUsedItem

       |      (int) Amount of time elapsed (ms) between the use of the previous and currently used item.


   .. attribute:: uid

       |      (int) Unique id for the given world the :class:`Player` is in.


   .. attribute:: useTimer

       |      (:class:`Timer`) Tracks the amount of time until the player can use an item again.


   .. attribute:: viewport

       |      (:class:`PixelRect`) The player's viewport. The area of the world that the player currently sees.


   .. attribute:: viewportSize

       |      (:class:`PixelVector`) Size of the player's viewport.


Profiler
-----------------------------------
.. class:: Profiler

   

   .. method:: disable( )

      

   .. method:: enable( )

      

   .. method:: finish( )

      

   .. method:: log( [name=''])

      

      :param name: 

      :type name: str

   .. method:: start( name[, parent=''[, isStandalone=False]])

      

      :param name: 

      :type name: str

      :param parent: 

      :type parent: str

      :param isStandalone: 

      :type isStandalone: bool

   .. attribute:: enabled

      

   .. attribute:: netProfile

      

PythonImporter
-----------------------------------
.. class:: PythonImporter

   

   .. method:: __init__( )

      

   .. method:: clearModuleDependencies( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: deepCopyModuleDict( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: object

   .. method:: getModuleDependencies( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`StringSet`

   .. staticmethod:: get( )

      

      :rtype: :class:`PythonImporter`

   .. attribute:: blacklist

      

SceneManager
-----------------------------------
.. class:: SceneManager

   

   .. method:: getActive( )

      

      :rtype: object

   .. method:: transition( arg2)

      

      :param arg2: 

      :type arg2: str

   .. attribute:: active

      

Scenes
-----------------------------------
.. class:: Scenes

   

   .. data:: GAMEPLAY = 'Gameplay'

   .. data:: LOGO = 'Logo'

   .. data:: MENU = 'Menu'

Skill
-----------------------------------
.. class:: Skill

   

   .. method:: __init__( name, type, icon, costs, unlockLevels)

      

      :param name: 

      :type name: str

      :param type: 

      :type type: :class:`SkillType`

      :param icon: 

      :type icon: str

      :param costs: 

      :type costs: list

      :param unlockLevels: 

      :type unlockLevels: list

   .. method:: __repr__( )

      

      :rtype: str

   .. attribute:: canRepeatUse

      

   .. attribute:: cooldown

      

   .. attribute:: getDescription

      

   .. attribute:: getIcon

      

   .. attribute:: getModifiers

      

   .. attribute:: getName

      

   .. attribute:: icon

      

   .. attribute:: isAvailable

      

   .. attribute:: isUsable

      

   .. attribute:: name

      

   .. attribute:: onActivate

      

   .. attribute:: onDeactivate

      

   .. attribute:: onUse

      

   .. attribute:: staminaCosts

      

   .. attribute:: type

      

StatList
-----------------------------------
.. class:: StatList

   

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

StateManager
-----------------------------------
.. class:: StateManager

   

   .. method:: getCurrent( )

      

      :rtype: int

   .. method:: reset( arg2)

      

      :param arg2: 

      :type arg2: :class:`Game`

   .. method:: setInput( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :param arg3: 

      :type arg3: object

   .. attribute:: onStep

      

   .. data:: TIMESTEP_TIME = 15

Talent
-----------------------------------
.. class:: Talent

   

   .. method:: __init__( name, icon, levels)

      

      :param name: 

      :type name: str

      :param icon: 

      :type icon: str

      :param levels: 

      :type levels: list

   .. attribute:: icon

      

   .. attribute:: levels

      

   .. attribute:: name

      

   .. attribute:: onLevelUp

      

   .. attribute:: skills

      

Damage
-----------------------------------
.. class:: Damage

   

   .. method:: __call__( id, amount, life, time)

      

      :param id: 

      :type id: str

      :param amount: 

      :type amount: int

      :param life: 

      :type life: int

      :param time: 

      :type time: int

      :rtype: bool

   .. method:: current( id)

      

      :param id: 

      :type id: str

      :rtype: int

TimerSystem
-----------------------------------
.. class:: TimerSystem

   

   .. method:: add( time, callback[, isPrecise=False[, isExitJob=False]])

      

      :param time: 

      :type time: int

      :param callback: 

      :type callback: object

      :param isPrecise: 

      :type isPrecise: bool

      :param isExitJob: 

      :type isExitJob: bool

      :rtype: int

   .. method:: cancel( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: clear( )

      

   .. method:: completeOnExit( )

      

   .. method:: getTime( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: int

   .. method:: update( arg2)

      

      :param arg2: 

      :type arg2: int

