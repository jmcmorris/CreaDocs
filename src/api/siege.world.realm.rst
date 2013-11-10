.. _siege.world.realm:

siege.world.realm
==================

DistributeResult
-----------------------------------
.. class:: DistributeResult

   

   .. data:: BREAK = siege.world.realm.DistributeResult.BREAK

   .. data:: CONTINUE = siege.world.realm.DistributeResult.CONTINUE

   .. data:: HIT_SURFACE = siege.world.realm.DistributeResult.HIT_SURFACE

   .. data:: SUCCESS = siege.world.realm.DistributeResult.SUCCESS

   .. data:: names = {'BREAK': siege.world.realm.DistributeResult.BREAK, 'CONTINUE'...

   .. data:: values = {0: siege.world.realm.DistributeResult.CONTINUE, 1: siege.wor...

Layer
-----------------------------------
.. class:: Layer

   

   .. data:: Active = siege.world.realm.Layer.Active

   .. data:: BG1 = siege.world.realm.Layer.BG1

   .. data:: BG2 = siege.world.realm.Layer.BG2

   .. data:: BG3 = siege.world.realm.Layer.BG3

   .. data:: Back = siege.world.realm.Layer.Back

   .. data:: Dropped = siege.world.realm.Layer.Dropped

   .. data:: Fore = siege.world.realm.Layer.Fore

   .. data:: Ground = siege.world.realm.Layer.Ground

   .. data:: Item = siege.world.realm.Layer.Item

   .. data:: None = siege.world.realm.Layer.None

   .. data:: Wall = siege.world.realm.Layer.Wall

   .. data:: WallAndGround = siege.world.realm.Layer.WallAndGround

   .. data:: names = {'Active': siege.world.realm.Layer.Active, 'BG1': siege.world....

   .. data:: values = {0: siege.world.realm.Layer.None, 1: siege.world.realm.Layer....

ActiveTile
-----------------------------------
.. class:: ActiveTile

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`TileComponent`

   .. attribute:: component

      

   .. attribute:: frame

      

   .. attribute:: id

      

AutomataCell
-----------------------------------
.. class:: AutomataCell

   

   .. method:: getMaxQuantity( )

      

      :rtype: int

   .. method:: isActive( )

      

      :rtype: bool

   .. method:: isFull( )

      

      :rtype: bool

   .. method:: setActive( quantity)

      

      :param quantity: 

      :type quantity: bool

   .. method:: update( north, south, east, west)

      

      :param north: 

      :type north: object

      :param south: 

      :type south: object

      :param east: 

      :type east: object

      :param west: 

      :type west: object

      :rtype: bool

   .. method:: update( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: object

      :param arg5: 

      :type arg5: object

   .. attribute:: quantity

      

WaterCell
-----------------------------------
.. class:: WaterCell

   

   .. method:: __init__( quantity)

      

      :param quantity: 

      :type quantity: int

LavaCell
-----------------------------------
.. class:: LavaCell

   

   .. method:: __init__( quantity)

      

      :param quantity: 

      :type quantity: int

BiomeBackground
-----------------------------------
.. class:: BiomeBackground

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. attribute:: images

      

   .. attribute:: offset

      

   .. attribute:: scroll

      

BiomeData
-----------------------------------
.. class:: BiomeData

   

   .. method:: __init__( biome)

      

      :param biome: 

      :type biome: :class:`Biome`

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. attribute:: area

      

   .. attribute:: biome

      

   .. attribute:: ratio

      

   .. attribute:: uid

      

BiomeDataSet
-----------------------------------
.. class:: BiomeDataSet

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: :class:`BiomeData`

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

      :type arg2: :class:`BiomeData`

   .. method:: clear( )

      

   .. method:: has( arg2)

      

      :param arg2: 

      :type arg2: :class:`BiomeData`

      :rtype: bool

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: :class:`BiomeData`

BiomeMap
-----------------------------------
.. class:: BiomeMap

   

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

BiomeTracker
-----------------------------------
.. class:: BiomeTracker

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: add( biome)

      

      :param biome: 

      :type biome: :class:`BiomeData`

   .. method:: getBiome( position)

      

      :param position: 

      :type position: :class:`Vector`

      :rtype: :class:`BiomeData`

   .. method:: getBiomeInfo( name)

      

      :param name: 

      :type name: str

      :rtype: :class:`Biome`

   .. method:: getBiomes( area)

      

      :param area: 

      :type area: :class:`Rect`

      :rtype: :class:`BiomeDataSet`

   .. method:: getRandomUndergroundPosition( depthStart, depthEnd)

      

      :param depthStart: 

      :type depthStart: float

      :param depthEnd: 

      :type depthEnd: float

      :rtype: :class:`TileVector`

   .. method:: getUid( )

      

      :rtype: int

   .. method:: hasBiome( uid)

      

      :param uid: 

      :type uid: int

      :rtype: bool

   .. method:: initializeUndergroundThreshold( )

      

   .. method:: remove( biome)

      

      :param biome: 

      :type biome: :class:`BiomeData`

   .. attribute:: biomes

      

   .. attribute:: data

      

   .. attribute:: thresholdWrg

      

   .. attribute:: undergroundThreshold

      

   .. attribute:: undergroundVolume

      

CellList
-----------------------------------
.. class:: CellList

   

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

DroppedHandler
-----------------------------------
.. class:: DroppedHandler

   

   .. method:: create( item, position, velocity[, delay=500]])

      

      :param item: 

      :type item: :class:`InventoryItem`

      :param position: 

      :type position: :class:`Vector`

      :param velocity: 

      :type velocity: :class:`Vector`

      :param delay: 

      :type delay: int

      :rtype: :class:`Entity`

IdTilesMap
-----------------------------------
.. class:: IdTilesMap

   

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

LayerBase
-----------------------------------
.. class:: LayerBase

   

   .. method:: isSpaceAvailable( arg2)

      

      :param arg2: 

      :type arg2: :class:`Rect`

      :rtype: bool

   .. method:: isSpaceAvailable( arg2)

      

      :param arg2: 

      :type arg2: :class:`Rect`

   .. attribute:: realmSize

      

   .. attribute:: type

      

BackLayer
-----------------------------------
.. class:: BackLayer

   

   .. method:: setColor( color)

      

      :param color: 

      :type color: :class:`Color`

   .. method:: transition( time, paths, offset, scroll, center, move)

      

      :param time: 

      :type time: int

      :param paths: 

      :type paths: :class:`StringList`

      :param offset: 

      :type offset: float

      :param scroll: 

      :type scroll: :class:`Vector`

      :param center: 

      :type center: :class:`Vector`

      :param move: 

      :type move: :class:`Vector`

EntityLayer
-----------------------------------
.. class:: EntityLayer

   

   .. method:: add( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: getAll( )

      

      :rtype: :class:`EntitySet`

   .. method:: getNearby( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: :class:`EntitySet`

   .. method:: getNearby( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

      :rtype: :class:`EntitySet`

   .. method:: getNearby( point, radius)

      

      :param point: 

      :type point: :class:`Vector`

      :param radius: 

      :type radius: float

      :rtype: :class:`EntitySet`

   .. method:: has( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: isSpaceAvailable( area)

      

      :param area: 

      :type area: :class:`Rect`

      :rtype: bool

   .. method:: remove( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: remove( entityId)

      

      :param entityId: 

      :type entityId: int

TileLayer
-----------------------------------
.. class:: TileLayer

   

   .. method:: damageTile( tilePosition, damage)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :param damage: 

      :type damage: int

      :rtype: bool

   .. method:: fullDirty( )

      

   .. method:: getFrame( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :rtype: int

   .. method:: getIdMap( area)

      

      :param area: 

      :type area: :class:`TileRect`

      :rtype: :class:`IdTilesMap`

   .. method:: getSegment( position)

      

      :param position: 

      :type position: :class:`Vector`

      :rtype: int

   .. method:: getSegment( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :rtype: int

   .. method:: getTile( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :rtype: int

   .. method:: getTileComponent( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :rtype: :class:`TileComponent`

   .. method:: getTileInDirection( position, direction[, solidOnly=False]])

      

      :param position: 

      :type position: :class:`Vector`

      :param direction: 

      :type direction: :class:`TileVector`

      :param solidOnly: 

      :type solidOnly: bool

      :rtype: :class:`TilePosition`

   .. method:: getTileList( area, tileId, amount])

      

      :param area: 

      :type area: :class:`TileRect`

      :param tileId: 

      :type tileId: int

      :param amount]: 

      :type amount]: int

      :rtype: :class:`TilePositionList`

   .. method:: getTilePosition( position)

      

      :param position: 

      :type position: :class:`TileVector`

      :rtype: :class:`TilePosition`

   .. method:: getTilePosition( position)

      

      :param position: 

      :type position: :class:`Vector`

      :rtype: :class:`TilePosition`

   .. method:: isEmpty( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :rtype: bool

   .. method:: isSolid( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :rtype: bool

   .. method:: isSpaceAvailable( area)

      

      :param area: 

      :type area: :class:`Rect`

      :rtype: bool

   .. method:: isValid( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :rtype: bool

   .. method:: overlaps( arg2, solidOnly, includeTouching)

      

      :param arg2: 

      :type arg2: :class:`Rect`

      :param solidOnly: 

      :type solidOnly: bool

      :param includeTouching: 

      :type includeTouching: bool

      :rtype: :class:`TilePositionList`

   .. method:: setTile( tilePosition, tileId)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

      :param tileId: 

      :type tileId: int

   .. attribute:: tiles

      

LayerManager
-----------------------------------
.. class:: LayerManager

   

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Layer`

      :rtype: :class:`LayerBase`

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: canChangeTile( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`Layer`

      :param arg3: 

      :type arg3: :class:`TilePosition`

      :param arg4: 

      :type arg4: int

      :rtype: bool

   .. method:: distanceFromTile( entity, position)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param position: 

      :type position: :class:`Vector`

      :rtype: float

   .. method:: getOrdered( )

      

      :rtype: :class:`Layers`

   .. method:: isSpaceAvailable( layer, area)

      

      :param layer: 

      :type layer: :class:`Layer`

      :param area: 

      :type area: :class:`Rect`

      :rtype: bool

   .. method:: setTile( layer, tilePos, tileId[, forced=False]])

      

      :param layer: 

      :type layer: :class:`Layer`

      :param tilePos: 

      :type tilePos: :class:`TilePosition`

      :param tileId: 

      :type tileId: int

      :param forced: 

      :type forced: bool

      :rtype: bool

   .. method:: setTile( layer, tilePos, tileId, forced)

      

      :param layer: 

      :type layer: :class:`Layer`

      :param tilePos: 

      :type tilePos: :class:`TilePosition`

      :param tileId: 

      :type tileId: int

      :param forced: 

      :type forced: bool

      :rtype: bool

Layers
-----------------------------------
.. class:: Layers

   

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

LightSource
-----------------------------------
.. class:: LightSource

   

   .. method:: __init__( )

      

   .. method:: invalidate( )

      

   .. method:: updateLightColor( )

      

   .. attribute:: brightness

      

   .. attribute:: color

      

   .. attribute:: enabled

      

   .. attribute:: falloff

      

   .. attribute:: intensity

      

   .. attribute:: isValid

      

   .. attribute:: position

      

   .. attribute:: size

      

PhysicsCollision
-----------------------------------
.. class:: PhysicsCollision

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. attribute:: component

      

   .. attribute:: shouldCollide

      

   .. attribute:: slope

      

PhysicsComponentList
-----------------------------------
.. class:: PhysicsComponentList

   

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

PhysicsHandler
-----------------------------------
.. class:: PhysicsHandler

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: add( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: getCollisionX( entityId, component)

      

      :param entityId: 

      :type entityId: int

      :param component: 

      :type component: :class:`PhysicsComponent`

      :rtype: :class:`PhysicsCollision`

   .. method:: getCollisionX( entityId, component, area, direction, bodyWidth)

      

      :param entityId: 

      :type entityId: int

      :param component: 

      :type component: :class:`PhysicsComponent`

      :param area: 

      :type area: :class:`Rect`

      :param direction: 

      :type direction: :class:`Direction`

      :param bodyWidth: 

      :type bodyWidth: float

      :rtype: :class:`PhysicsCollision`

   .. method:: getCollisionY( entityId, component)

      

      :param entityId: 

      :type entityId: int

      :param component: 

      :type component: :class:`PhysicsComponent`

      :rtype: :class:`PhysicsCollision`

   .. method:: getCollisionY( entityId, component, area, direction, bodyWidth)

      

      :param entityId: 

      :type entityId: int

      :param component: 

      :type component: :class:`PhysicsComponent`

      :param area: 

      :type area: :class:`Rect`

      :param direction: 

      :type direction: :class:`Direction`

      :param bodyWidth: 

      :type bodyWidth: float

      :rtype: :class:`PhysicsCollision`

   .. method:: getTouching( body, direction)

      

      :param body: 

      :type body: :class:`PhysicsComponent`

      :param direction: 

      :type direction: :class:`Direction`

      :rtype: :class:`PhysicsComponentList`

   .. method:: isOnSlope( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: remove( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: separateSlope( physics, collision)

      

      :param physics: 

      :type physics: :class:`PhysicsComponent`

      :param collision: 

      :type collision: :class:`PhysicsCollision`

   .. method:: separateX( body1, body2)

      

      :param body1: 

      :type body1: :class:`PhysicsComponent`

      :param body2: 

      :type body2: :class:`PhysicsComponent`

      :rtype: bool

   .. method:: separateY( body1, body2)

      

      :param body1: 

      :type body1: :class:`PhysicsComponent`

      :param body2: 

      :type body2: :class:`PhysicsComponent`

      :rtype: bool

   .. method:: wakeNearby( area)

      

      :param area: 

      :type area: :class:`Rect`

PlacementHandler
-----------------------------------
.. class:: PlacementHandler

   

   .. method:: __init__( game, realm)

      

      :param game: 

      :type game: :class:`Game`

      :param realm: 

      :type realm: :class:`Realm`

   .. method:: calculatePosition( mousePos, entity)

      

      :param mousePos: 

      :type mousePos: :class:`Vector`

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: :class:`Vector`

   .. method:: checkPosition( result, neighbor, entity, x, y)

      

      :param result: 

      :type result: :class:`Vector`

      :param neighbor: 

      :type neighbor: :class:`TileVector`

      :param entity: 

      :type entity: :class:`Entity`

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :rtype: :class:`DistributeResult`

   .. method:: createPlacement( position, entity, isFlipped)

      

      :param position: 

      :type position: :class:`Vector`

      :param entity: 

      :type entity: :class:`Entity`

      :param isFlipped: 

      :type isFlipped: bool

      :rtype: :class:`Entity`

   .. method:: destroyPlacement( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: :class:`Entity`

   .. method:: findSpace( content, realmArea, axisType)

      

      :param content: 

      :type content: :class:`Content`

      :param realmArea: 

      :type realmArea: :class:`RealmArea`

      :param axisType: 

      :type axisType: :class:`AxisType`

      :rtype: :class:`Vector`

   .. attribute:: onCreate

      

   .. attribute:: onDestroy

      

Realm
-----------------------------------
.. class:: Realm

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: add( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: add( player)

      

      :param player: 

      :type player: :class:`Player`

   .. method:: getClosestPlayer( position)

      

      :param position: 

      :type position: :class:`Vector`

      :rtype: object

   .. method:: getInteracted( arg2, position)

      

      :param arg2: 

      :type arg2: :class:`Player`

      :param position: 

      :type position: :class:`Vector`

      :rtype: :class:`Entity`

   .. method:: remove( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

   .. method:: remove( player)

      

      :param player: 

      :type player: :class:`Player`

   .. method:: save( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. method:: update( frameTime)

      

      :param frameTime: 

      :type frameTime: int

   .. staticmethod:: create( arg1, game, uid, name, realmSize, groundLevel)

      

      :param arg1: 

      :type arg1: :class:`Game`

      :param game: 

      :type game: int

      :param uid: 

      :type uid: str

      :param name: 

      :type name: :class:`RealmSize`

      :param realmSize: 

      :type realmSize: :class:`WorldTime`

      :param groundLevel: 

      :type groundLevel: int

      :rtype: :class:`Realm`

   .. staticmethod:: load( game, path, time, stream)

      

      :param game: 

      :type game: :class:`Game`

      :param path: 

      :type path: object

      :param time: 

      :type time: :class:`WorldTime`

      :param stream: 

      :type stream: :class:`DataStream`

      :rtype: :class:`Realm`

   .. attribute:: automata

      

   .. attribute:: biomeTracker

      

   .. attribute:: dropped

      

   .. attribute:: groundLevel

      

   .. attribute:: layers

      

   .. attribute:: lighting

      

   .. attribute:: loader

      

   .. attribute:: name

      

   .. attribute:: path

      

   .. attribute:: physics

      

   .. attribute:: placement

      

   .. attribute:: players

      

   .. attribute:: size

      

   .. attribute:: startArea

      

   .. attribute:: surfaceLevel

      

   .. attribute:: uid

      

RealmArea
-----------------------------------
.. class:: RealmArea

   

   .. method:: __init__( area[, onSurface=False[, isUnderground=False]]]])

      

      :param area: 

      :type area: :class:`Rect`

      :param onSurface: 

      :type onSurface: bool

      :param isUnderground: 

      :type isUnderground: bool

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: randomDistribute( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`BiomeTracker`

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: int

   .. attribute:: area

      

   .. attribute:: isUnderground

      

   .. attribute:: onSurface

      

RealmInfo
-----------------------------------
.. class:: RealmInfo

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: unpack( stream)

      

      :param stream: 

      :type stream: :class:`DataStream`

   .. staticmethod:: pack( realm, stream)

      

      :param realm: 

      :type realm: :class:`Realm`

      :param stream: 

      :type stream: :class:`DataStream`

   .. attribute:: groundLevel

      

   .. attribute:: name

      

   .. attribute:: size

      

   .. attribute:: startArea

      

   .. attribute:: uid

      

RealmInfoList
-----------------------------------
.. class:: RealmInfoList

   

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

RealmSize
-----------------------------------
.. class:: RealmSize

   

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

   .. attribute:: chunkCount

      

   .. attribute:: chunkHeight

      

   .. attribute:: chunkWidth

      

   .. attribute:: halfHeight

      

   .. attribute:: halfWidth

      

   .. attribute:: height

      

   .. attribute:: regionCount

      

   .. attribute:: regionHeight

      

   .. attribute:: regionWidth

      

   .. attribute:: segmentCount

      

   .. attribute:: segmentHeight

      

   .. attribute:: segmentWidth

      

   .. attribute:: size

      

   .. attribute:: subtileCount

      

   .. attribute:: subtileHeight

      

   .. attribute:: subtileWidth

      

   .. attribute:: tileCount

      

   .. attribute:: tileHeight

      

   .. attribute:: tileWidth

      

   .. attribute:: width

      

TerrainMap
-----------------------------------
.. class:: TerrainMap

   

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

TileList
-----------------------------------
.. class:: TileList

   

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

TilePosition
-----------------------------------
.. class:: TilePosition

   

   .. method:: __cmp__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TilePosition`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TilePosition`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

   .. method:: __init__( )

      

   .. method:: __init__( x, y, realmSize)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param realmSize: 

      :type realmSize: :class:`RealmSize`

   .. method:: __init__( segment, x, y, realmSize)

      

      :param segment: 

      :type segment: int

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param realmSize: 

      :type realmSize: :class:`RealmSize`

   .. method:: __init__( position, realmSize)

      

      :param position: 

      :type position: :class:`TileVector`

      :param realmSize: 

      :type realmSize: :class:`RealmSize`

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TilePosition`

   .. method:: __lt__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TilePosition`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TilePosition`

      :rtype: object

   .. method:: getNeighbor( x, y)

      Adds to the tile's coordinates and returns the tile at the other end.


      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :rtype: :class:`TilePosition`

   .. method:: getWorld( )

      The grid position of the tile.


      :rtype: :class:`TileVector`

   .. method:: getWorldCenter( )

      The center pixel position of the tile.


      :rtype: :class:`Vector`

   .. method:: getWorldPosition( )

      The pixel position of the tile.


      :rtype: :class:`Vector`

   .. method:: move( x, y)

      Moves the tile by adding to its coordinates.


      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. attribute:: isValid

      

   .. attribute:: realmSize

      

   .. attribute:: segment

      

   .. attribute:: x

      

   .. attribute:: y

      

TilePositionIter
-----------------------------------
.. class:: TilePositionIter

   

   .. method:: __init__( tilePosition)

      

      :param tilePosition: 

      :type tilePosition: :class:`TilePosition`

   .. method:: resetX( )

      

   .. method:: resetY( )

      

   .. method:: stepDown( )

      

   .. method:: stepLeft( )

      

   .. method:: stepRight( )

      

   .. method:: stepUp( )

      

   .. attribute:: current

      

   .. attribute:: start

      

TilePositionList
-----------------------------------
.. class:: TilePositionList

   

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

TileSegment
-----------------------------------
.. class:: TileSegment

   

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

AutomataManager
-----------------------------------
.. class:: AutomataManager

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: activateCells( area)

      

      :param area: 

      :type area: :class:`Rect`

   .. method:: activateCells( area)

      

      :param area: 

      :type area: :class:`PixelRect`

   .. method:: clearNode( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: getActiveCount( )

      

      :rtype: int

   .. method:: getCell( position)

      

      :param position: 

      :type position: :class:`Vector`

      :rtype: :class:`AutomataCell`

   .. method:: getCells( area)

      

      :param area: 

      :type area: :class:`Rect`

      :rtype: :class:`CellList`

   .. method:: getCells( area)

      

      :param area: 

      :type area: :class:`PixelRect`

      :rtype: :class:`CellList`

   .. method:: isSettled( )

      

      :rtype: bool

   .. method:: setCell( x, y, cell)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param cell: 

      :type cell: :class:`AutomataCell`

   .. method:: setCell( position, cell)

      

      :param position: 

      :type position: :class:`Vector`

      :param cell: 

      :type cell: :class:`AutomataCell`

   .. method:: simulate( )

      

   .. attribute:: activeCells

      

   .. attribute:: skippedCells

      

Subsystem)
-----------------------------------
.. class:: Subsystem)

   

Subsystem)
-----------------------------------
.. class:: Subsystem)

   

