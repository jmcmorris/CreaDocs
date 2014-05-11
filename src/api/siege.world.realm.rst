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

Layer
-----------------------------------
.. class:: Layer

   

   .. data:: Active = siege.world.realm.Layer.Active

   .. data:: BG1 = siege.world.realm.Layer.BG1

   .. data:: BG2 = siege.world.realm.Layer.BG2

   .. data:: BG3 = siege.world.realm.Layer.BG3

   .. data:: BG4 = siege.world.realm.Layer.BG4

   .. data:: Back = siege.world.realm.Layer.Back

   .. data:: Dropped = siege.world.realm.Layer.Dropped

   .. data:: Fore = siege.world.realm.Layer.Fore

   .. data:: Ground = siege.world.realm.Layer.Ground

   .. data:: Item = siege.world.realm.Layer.Item

   .. data:: None = siege.world.realm.Layer.None

   .. data:: Wall = siege.world.realm.Layer.Wall

   .. data:: WallAndGround = siege.world.realm.Layer.WallAndGround

LightSourceType
-----------------------------------
.. class:: LightSourceType

   

   .. data:: Basic = siege.world.realm.LightSourceType.Basic

   .. data:: Cone = siege.world.realm.LightSourceType.Cone

MapMode
-----------------------------------
.. class:: MapMode

   

   .. data:: Fullscreen = siege.world.realm.MapMode.Fullscreen

   .. data:: Hidden = siege.world.realm.MapMode.Hidden

   .. data:: Minimap = siege.world.realm.MapMode.Minimap

   .. data:: Overlay = siege.world.realm.MapMode.Overlay

ActiveTile
-----------------------------------
.. class:: ActiveTile

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileComponent`

   .. method:: getId( )

      Returns the tile id for this tile's component. If tile is empty then 0 is returned.


      :rtype: int

   .. attribute:: component

       |      The component for this tile


   .. attribute:: foliage

       |      The foliage component for this tile


   .. attribute:: frame

       |      The current frame of animation


AutomataCell
-----------------------------------
.. class:: AutomataCell

   

   .. method:: getMaxQuantity( )

      Returns max quantity of this cell


      :rtype: int

   .. method:: isActive( )

      Return whether or not this cell is marked as active


      :rtype: bool

   .. method:: isFull( )

      Returns true if quantity==max quantity, false otherwise


      :rtype: bool

   .. method:: setActive( active)

      Mark cell as active or inactive


      :param active:  Set to true for active, false otherwise


      :type active: bool

   .. method:: update( north, south, east, west)

      Must be defined by parent class


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

       |      Quantity count for this cell


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

      

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`BiomeBackground`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. attribute:: images

       |      A :class:`StringList` of paths to image files


   .. attribute:: loop

       |      Set to true to loop background, false otherwise


   .. attribute:: offset

       |      :class:`Vector` for render offset


   .. attribute:: scroll

       |      :class:`Vector` for scroll movement


BiomeData
-----------------------------------
.. class:: BiomeData

   

   .. method:: __init__( biome)

      

      :param biome: 

      :type biome: :class:`Biome`

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`BiomeData`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. attribute:: area

       |      Coordinates of this biome


   .. attribute:: biome

       |      :class:`Biome` associated with this :class:`Biome`Data


   .. attribute:: ratio

       |      Biomes ratio value


   .. attribute:: uid

       |      Unique identifier


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

   

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`BiomeTracker`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: add( biome)

      Add a :class:`Biome` to this :class:`Biome`Tracker


      :param biome:  The biome to add


      :type biome: :class:`BiomeData`

   .. method:: getBiome( position)

      Returns a the Biomedata that position is within


      :param position:  The coordinates to target


      :type position: :class:`Vector`

      :rtype: :class:`BiomeData`

   .. method:: getBiomeInfo( name)

      Returns a :class:`Biome` with matching name


      :param name:  The name of the biome to search for


      :type name: str

      :rtype: :class:`Biome`

   .. method:: getBiomes( area)

      Returns a BiomedataSet full of all biomes that area is within


      :param area:  The coordinates to search


      :type area: :class:`Rect`

      :rtype: :class:`BiomeDataSet`

   .. method:: getRandomUndergroundPosition( depthStart, depthEnd)

      Returns a random position from depthStart to depthEnd based on underground threshold


      :param depthStart:  Maximum height for position


      :type depthStart: float

      :param depthEnd:  Minimum height for position


      :type depthEnd: float

      :rtype: :class:`TileVector`

   .. method:: getUid( )

      Return a unique Id based on the biome's unique Ids


      :rtype: int

   .. method:: hasBiome( uid)

      Checks if a biome is in this :class:`BiomeTracker`


      :param uid:  Unique Id for a biome


      :type uid: int

      :returns: True if biome found, false otherwise


      :rtype: bool

   .. method:: initializeUndergroundThreshold( )

      Sets up all related information for underground threshold after it has been populated


   .. method:: remove( biome)

      Remove a biome from this :class:`BiomeTracker`


      :param biome:  The :class:`BiomeData` to remove


      :type biome: :class:`BiomeData`

   .. method:: updatePlayer( player[, force=False])

      Updates the position based on entity. Also handles transitions from one biome to another


      :param player:  :class:`Entity` to track


      :type player: :class:`Entity`

      :param force:  Set to true to force a check for biome transitions, false otherwise


      :type force: bool

   .. attribute:: biomes

       |      Map of all biomes


   .. attribute:: currentBiome

       |      The biome the player is in


   .. attribute:: data

       |      Map of Ids to biome data


   .. attribute:: thresholdWrg

       |      :class:`WeightedRandomGenerator` for creating biomes


   .. attribute:: undergroundThreshold

       |      Threshold for depth of caves


   .. attribute:: undergroundVolume

       |      Total size of space between threshold and the edge of the realm


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

   

   .. method:: create( item, position, velocity, >[, delay=500]])

      Adds an item entity to the realm


      :param item:  :class:`Item` data


      :type item: :class:`InventoryItem`

      :param position:  Coordinates for new entity


      :type position: :class:`Vector`

      :param velocity:  Movement vector for new entity


      :type velocity: :class:`Vector`

      :param >: 

      :type >: =0

      :param delay:  :class:`Item` delay time


      :type delay: int

      :returns: The entity created


      :rtype: :class:`Entity`

   .. method:: createMany( item, position[, delay=500])

      Adds multiple item entities to the realm


      :param item:  :class:`Item` data


      :type item: :class:`InventoryItem`

      :param position:  Coordinates for new entity


      :type position: :class:`Vector`

      :param delay:  :class:`Item` delay time


      :type delay: int

      :returns: A list of entities created


      :rtype: :class:`Entities`

FoliageHandler
-----------------------------------
.. class:: FoliageHandler

   

   .. method:: hasActive( )

      

      :rtype: bool

   .. method:: spreadFoliage( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`FoliageComponent`

      :param arg3: 

      :type arg3: :class:`TileRect`

      :param arg4: 

      :type arg4: int

   .. method:: update( arg2)

      

      :param arg2: 

      :type arg2: int

   .. attribute:: groundLevel

      

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

   

   .. method:: isSpaceAvailable( area)

      Function must be overwritten by parent class


      :param area:  Coordinates to search within


      :type area: :class:`Rect`

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

      Changes the transition color


      :param color:  :class:`Color` to use for change


      :type color: :class:`Color`

   .. method:: transition( time, paths, offset, scroll, loop, center, move)

      Start a transition with new parameters


      :param time:  Remaining time for transition


      :type time: int

      :param paths:  List of paths to image files


      :type paths: :class:`StringList`

      :param offset:  :class:`Render` offsest


      :type offset: :class:`Vector`

      :param scroll:  Scrolling vector for camera


      :type scroll: :class:`Vector`

      :param loop:  Set to true for looping images, false otherwise


      :type loop: bool

      :param center:  Position for the center of the view


      :type center: :class:`Vector`

      :param move:  :class:`Vector` for camera movement speed


      :type move: :class:`Vector`

EntityLayer
-----------------------------------
.. class:: EntityLayer

   

   .. method:: add( entity)

      Adds an entity to the :class:`EntityLayer`


      :param entity:  The entity to add


      :type entity: :class:`Entity`

   .. method:: getAll( )

      Return an :class:`EntitySet` containing all entities in this layer


      :rtype: :class:`EntitySet`

   .. method:: getNearby( entity)

      Returns an :class:`EntitySet` containing all entities in close proximity to entity


      :param entity:  The entity to search around


      :type entity: :class:`Entity`

      :rtype: :class:`EntitySet`

   .. method:: getNearby( rect)

      Returns an :class:`EntitySet` containing all entities in close proximity to rect


      :param rect:  The Coordinates to search around


      :type rect: :class:`Rect`

      :rtype: :class:`EntitySet`

   .. method:: getNearby( point, radius)

      Returns an :class:`EntitySet` containing all entities in close proximity to rectangle created by parameters


      :param point:  The center point for the rectangle


      :type point: :class:`Vector`

      :param radius:  How far to extend from the radius in each direction


      :type radius: float

      :rtype: :class:`EntitySet`

   .. method:: has( entity)

      Returns true is entity is present in this layer


      :param entity:  Target to search for


      :type entity: :class:`Entity`

      :rtype: bool

   .. method:: isSpaceAvailable( area)

      Returns true if there are no entities near the area, false otherwise


      :param area:  Coordinates to search around


      :type area: :class:`Rect`

      :rtype: bool

   .. method:: remove( entity)

      Removes the entity from this layer if it is present


      :param entity:  Target entity to remove


      :type entity: :class:`Entity`

   .. method:: remove( entityId)

      Removes the entity from this layer if it is present


      :param entityId:  Id of entity to remove


      :type entityId: int

TileLayer
-----------------------------------
.. class:: TileLayer

   

   .. method:: clearVertices( )

      Clears all vertices to ensure a clean rendering of tiles.


   .. method:: copyTo( targetLayer, startPosition, destination)

      Copies the contents of this :class:`TileLayer` to the provided :class:`TileLayer`. This does not check for overlaps in the source and destination.


      :param targetLayer:  The targeted :class:`TileLayer` to copy to.


      :type targetLayer: :class:`TileLayer`

      :param startPosition:  The top left corner to start copying from.


      :type startPosition: :class:`TileVector`

      :param destination:  The targeted area to copy to. Automatically resized to fit within the bounds of the world.


      :type destination: :class:`TileRect`

   .. method:: damageTile( position, damage)

      Reduces the durability of a tile by damage


      :param position:  The tile position to damage


      :type position: :class:`TileVector`

      :param damage:  The amount to reduce the tile's durability by


      :type damage: int

      :returns: True if the tile was destroyed, false otherwise


      :rtype: bool

   .. method:: fullDirty( )

      Mark all regions in realm as changed


   .. method:: getIdMap( area)

      Returns a map of ids to :class:`TileVectorList` containing all tiles inside of the given area


      :param area:  Coordinates to search within


      :type area: :class:`TileRect`

      :rtype: :class:`IdTilesMap`

   .. method:: getTile( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: :class:`ActiveTile`

   .. method:: getTile( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: :class:`ActiveTile`

   .. method:: getTileInDirection( position, direction[, solidOnly=False])

      If position is valid add direction to position and return the tile underneath


      :param position:  Position to search


      :type position: :class:`Vector`

      :param direction:  :class:`Vector` to add to position


      :type direction: :class:`TileVector`

      :param solidOnly:  Set to true to stop direction on a solid tile, false otherwise


      :type solidOnly: bool

      :returns: A :class:`TileVector` from the search position


      :rtype: :class:`TileVector`

   .. method:: getTileList( area, tileId[, amount=4294967295L])

      Returns a :class:`TileVectorList` that contains all tile positions matching the given tileId within the provided area


      :param area:  Coordinates to search within


      :type area: :class:`TileRect`

      :param tileId:  Id of tiles to search


      :type tileId: int

      :param amount:  Maximum number of tiles to return. Defaults to unbounded amount


      :type amount: int

      :rtype: :class:`TileVectorList`

   .. method:: initialize( )

      Clears and reinitializes all tile regions for world generation.


   .. method:: isEmpty( position)

      Checks if there is no tile at position


      :param position:  The position to check


      :type position: :class:`TileVector`

      :returns: True if tile at position is empty, false otherwise


      :rtype: bool

   .. method:: isLoaded( arg2, arg3)

      Returns True if the specified tile position is loaded otherwise False.


      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. method:: isLoaded( arg2)

      Returns True if the specified tile position is loaded otherwise False.


      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: bool

   .. method:: isSolid( position)

      Checks if the tile at position is a solid tile


      :param position:  The position to check


      :type position: :class:`TileVector`

      :returns: True if position is not empty and solid, false otherwise


      :rtype: bool

   .. method:: isSpaceAvailable( area)

      Returns true if there are no tile under area, false otherwise


      :param area:  Coordinates to search within


      :type area: :class:`Rect`

      :rtype: bool

   .. method:: overlaps( rect, solidOnly, includeTouching[, ignoreTiles=[]])

      Returns all tiles under the area rect


      :param rect:  The coordinates to search under


      :type rect: :class:`Rect`

      :param solidOnly:  Set to true to skip non solid tiles, set false otherwise


      :type solidOnly: bool

      :param includeTouching:  Set to true to include tiles touching border tiles, set false otherwise


      :type includeTouching: bool

      :param ignoreTiles:  A list of tileIds to skip during the search


      :type ignoreTiles: list

      :rtype: :class:`TileVectorList`

   .. method:: setFoliage( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :param arg3: 

      :type arg3: :class:`FoliageComponent`

   .. method:: setTile( position, tileId)

      Changes the tile type at position to the type specified by tileId


      :param position:  The position of the tile to change


      :type position: :class:`TileVector`

      :param tileId:  Id of the new type of tile


      :type tileId: int

LayerManager
-----------------------------------
.. class:: LayerManager

   

   .. method:: __getitem__( layer)

      Returns the :class:`LayerBase` of type layer.  If layer is not in manager it will return an empty :class:`LayerBase`.


      :param layer:  :class:`Layer` to search for


      :type layer: :class:`Layer`

      :rtype: :class:`LayerBase`

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`LayerManager`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: canChangeTile( layer, position, tileId)

      Returns true if tile at the position can be changed to a new tile of tileId


      :param layer:  :class:`Layer` to search


      :type layer: :class:`Layer`

      :param position:  Position of tile


      :type position: :class:`TileVector`

      :param tileId:  Id of the new tile


      :type tileId: int

      :returns: True if change can occur, false otherwise


      :rtype: bool

   .. method:: distanceFromTile( entity, position)

      Returns the distance from the center of entity to the center of the ground tile at position


      :param entity:  The entity used for the calculation


      :type entity: :class:`Entity`

      :param position:  The tile position for the calculation


      :type position: :class:`Vector`

      :returns: FLT_MAX if position is invalid, otherwise returns distance


      :rtype: float

   .. method:: getOrdered( )

      Returns all layers stored in this :class:`LayerManager`, in sorted order.


      :rtype: :class:`Layers`

   .. method:: isSpaceAvailable( layer, area)

      Returns the value from a call to isSpaceAvailable on target layer


      :param layer:  :class:`Layer` to use


      :type layer: :class:`Layer`

      :param area:  Coordinates to search within


      :type area: :class:`Rect`

      :rtype: bool

   .. method:: setTile( layer, tilePos, tileId[, forced=False])

      Returns true if tile at the position is successfully changed to a new tile of tileId


      :param layer:  :class:`Layer` to search


      :type layer: :class:`Layer`

      :param tilePos:  Position of tile


      :type tilePos: :class:`TileVector`

      :param tileId:  Id of the new tile


      :type tileId: int

      :param forced:  Set forced to true to disable canceling


      :type forced: bool

      :returns: True if change can occur, false otherwise


      :rtype: bool

   .. method:: setTile( layer, tilePos, tileId, forced)

      Returns true if tile at the position is successfully changed to a new tile of tileId


      :param layer:  :class:`Layer` to search


      :type layer: :class:`Layer`

      :param tilePos:  Position of tile


      :type tilePos: :class:`TileVector`

      :param tileId:  Id of the new tile


      :type tileId: int

      :param forced:  Set forced to true to disable canceling


      :type forced: bool

      :returns: True if change can occur, false otherwise


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

   

   .. method:: updateLightColor( )

      Updates light color to be used in lighting system.


   .. attribute:: angle

       |      (float) The angle (in degrees) the light spreads out from the direction on each side.


   .. attribute:: brightness

       |      The brightness of the light's color.


   .. attribute:: center

       |      The positional offset of the light source to the attached entity.


   .. attribute:: color

       |      The color of the light source


   .. attribute:: decay

       |      The rate at which the light dissipates.


   .. attribute:: direction

       |      (float) The direction (in degrees) this light is pointing at.


   .. attribute:: enabled

       |      Whether this light is on or not.


   .. attribute:: intensity

       |      The intensity of the light source. Ranging from pure darkness (0) to pure light (128).


   .. attribute:: name

       |      (str) Name of light source used to identify it within the :class:`LightComponent`.


   .. attribute:: onVisible

       |      (callable) Called when the light source is visible and being simulated. Signature is void(frameTime).


   .. attribute:: position

       |      The world coordinates of this light source.


   .. attribute:: size

       |      The size of the light source.


   .. attribute:: type

       |      (LightType) The type of light.


LightSourceData
-----------------------------------
.. class:: LightSourceData

   

   .. method:: __init__( )

      

   .. attribute:: angle

       |      (float) The angle (in degrees) the light spreads out from the direction on each side.


   .. attribute:: brightness

       |      (float) The brightness of the light's color. Default is 1.0.


   .. attribute:: center

       |      (:class:`Vector`) The positional offset of the light source to the attached entity.


   .. attribute:: color

       |      The color of this light source.


   .. attribute:: decay

       |      (float) The rate at which the light dissipates.


   .. attribute:: direction

       |      (float) The direction (in degrees) this light is pointing at.


   .. attribute:: enabled

       |      (bool) Whether the light starts enabled (on) or not (off).


   .. attribute:: intensity

       |      The intensity of the light source. Ranging from pure darkness (0) to pure light (128).


   .. attribute:: lightType

       |      (LightType) The type of light.


   .. attribute:: name

       |      (str) Name of light source used to identify it within the :class:`LightComponent`.


   .. attribute:: onVisible

       |      (callable) Called when the light source is visible and being simulated. Signature is void(frameTime).


   .. attribute:: size

       |      The size of the light source.


LightSourceDataList
-----------------------------------
.. class:: LightSourceDataList

   

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

LightSourceMap
-----------------------------------
.. class:: LightSourceMap

   

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

MapConflictRegion
-----------------------------------
.. class:: MapConflictRegion

   

   .. attribute:: icon

      

   .. attribute:: level

      

   .. attribute:: uid

      

MapConflictRegionList
-----------------------------------
.. class:: MapConflictRegionList

   

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

PhysicsCollision
-----------------------------------
.. class:: PhysicsCollision

   

   .. method:: __init__( )

      

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`PhysicsCollision`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. attribute:: component

       |      :class:`PhysicsComponent` of the collision


   .. attribute:: shouldCollide

       |      Marked true if collision should happen, false otherwise


   .. attribute:: slope

       |      :class:`Slope` value of collision


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

   

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`PhysicsHandler`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: add( entity)

      Adds entity to this :class:`PhysicsHandler`


      :param entity:  :class:`Entity` to add


      :type entity: :class:`Entity`

   .. method:: getCollisionX( entityId, body)

      Checks for collisions on the x axis of a body


      :param entityId:  Id for entity that has the body


      :type entityId: int

      :param body:  :class:`Physics` body to test against:returns: Collision data from results


      :type body: :class:`PhysicsComponent`

      :rtype: :class:`PhysicsCollision`

   .. method:: getCollisionX( entityId, body, area, direction, bodyWidth)

      Checks for collisions on the x axis of a body in area


      :param entityId:  Id for entity that has the body


      :type entityId: int

      :param body:  :class:`Physics` body to test against:param area: Coordinates to test within


      :type body: :class:`PhysicsComponent`

      :param area: 

      :type area: :class:`Rect`

      :param direction:  Which way is the body Moving


      :type direction: :class:`Direction`

      :param bodyWidth:  Width of body


      :type bodyWidth: float

      :returns: Collision data from results


      :rtype: :class:`PhysicsCollision`

   .. method:: getCollisionY( entityId, component)

      Checks for collisions on the y axis of a body


      :param entityId:  Id for entity that has the body


      :type entityId: int

      :param component: 

      :type component: :class:`PhysicsComponent`

      :rtype: :class:`PhysicsCollision`

   .. method:: getCollisionY( entityId, body, area, direction, bodyWidth)

      Checks for collisions on the y axis of a body in area


      :param entityId:  Id for entity that has the body


      :type entityId: int

      :param body:  :class:`Physics` body to test against:param area: Coordinates to test within


      :type body: :class:`PhysicsComponent`

      :param area: 

      :type area: :class:`Rect`

      :param direction:  Which way is the body Moving


      :type direction: :class:`Direction`

      :param bodyWidth:  Width of body


      :type bodyWidth: float

      :returns: Collision data from resutls


      :rtype: :class:`PhysicsCollision`

   .. method:: getTouching( body, direction)

      Return a list of all physic bodies that touch body moved in direction


      :param body:  :class:`Physics` body to test against


      :type body: :class:`PhysicsComponent`

      :param direction:  Which way the body will go


      :type direction: :class:`Direction`

      :rtype: :class:`PhysicsComponentList`

   .. method:: isOnSlope( entity)

      Checks if entity is on a slope


      :param entity: 

      :type entity: :class:`Entity`

      :returns: True if entity is colliding with a slope, false otherwise


      :rtype: bool

   .. method:: remove( entity)

      Removes entity to this :class:`PhysicsHandler`


      :param entity:  :class:`Entity` to remove


      :type entity: :class:`Entity`

   .. method:: separateSlope( physics, collision)

      Adjust a physics body according to a collision with a slope


      :param physics: 

      :type physics: :class:`PhysicsComponent`

      :param collision:  The collision data


      :type collision: :class:`PhysicsCollision`

   .. method:: separateX( body1, body2)

      Seperate two overlapping bodies on the x axis


      :param body1:  The first body to move


      :type body1: :class:`PhysicsComponent`

      :param body2:  The second body to move


      :type body2: :class:`PhysicsComponent`

      :returns: True if bodies no longer overlap on the x axis, false otherwise


      :rtype: bool

   .. method:: separateY( body1, body2)

      Seperate two overlapping bodies on the y axis


      :param body1:  The first body to move


      :type body1: :class:`PhysicsComponent`

      :param body2:  The second body to move


      :type body2: :class:`PhysicsComponent`

      :returns: True if bodies no longer overlap on the y axis, false otherwise


      :rtype: bool

   .. method:: wakeNearby( area)

      Awake all sleeping entities within area


      :param area:  Coordinates to search within


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

      Finds nearest valid new position based on mouse position, entity positions, and level structure


      :param mousePos:  Position of the mouse cursor


      :type mousePos: :class:`Vector`

      :param entity:  The entity to use in the calculation


      :type entity: :class:`Entity`

      :returns: Empty :class:`Vector` if no valid positions, else new position


      :rtype: :class:`Vector`

   .. method:: checkPosition( result, neighbor, entity, x, y)

      Checks the results of calculatePosition on entity and neighbor added to x,y. 


      :param result:  Result of caclulatePosition if SUCCESS is returned


      :type result: :class:`Vector`

      :param neighbor:  Target TilePosition


      :type neighbor: :class:`TileVector`

      :param entity:  The entity to use in the calculation


      :type entity: :class:`Entity`

      :param x:  Change in tile x coordinate


      :type x: int

      :param y:  Change in tile y coordinate


      :type y: int

      :returns: HIT_SURFACE if a solid tile is found. CONTINUE is open space is found. SUCCESS if there is space


      :rtype: :class:`DistributeResult`

   .. method:: createPlacement( position, entity, isFlipped)

      Convert an entity into a placed item


      :param position:  Where to place new entity


      :type position: :class:`Vector`

      :param entity:  Original entity to convert


      :type entity: :class:`Entity`

      :param isFlipped:  Set to true to force flip render on x axis, false otherwise


      :type isFlipped: bool

      :rtype: :class:`Entity`

   .. method:: destroyPlacement( entity)

      Create a new  dropped entity and destroy current one


      :param entity:  :class:`Entity` to convert


      :type entity: :class:`Entity`

      :returns: The new dropped entity


      :rtype: :class:`Entity`

   .. method:: findSpace( content, realmArea, axisType)

      Returns vector to available space near content in direction of axisType


      :param content:  Where to find space near


      :type content: :class:`Content`

      :param realmArea:  Which realm to search


      :type realmArea: :class:`RealmArea`

      :param axisType:  Which direction to search


      :type axisType: :class:`AxisType`

      :rtype: :class:`Vector`

   .. method:: remove( entity)

      Remove destroy method from an entity


      :param entity:  :class:`Entity` to remove


      :type entity: :class:`Entity`

   .. attribute:: onCreate

      

   .. attribute:: onDestroy

      

Realm
-----------------------------------
.. class:: Realm

   

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`Realm`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: add( entity)

      Adds an entity to this realm


      :param entity:  The entity to add


      :type entity: :class:`Entity`

   .. method:: add( arg2, player)

      Adds an player to this realm


      :param arg2: 

      :type arg2: :class:`Player`

      :param player:  The player to add


      :type player: bool

   .. method:: clear( )

      Removes all layers from this realm


   .. method:: getClosestPlayer( position)

      Returns the closest player to position


      :param position:  Coordinates to search near


      :type position: :class:`Vector`

      :rtype: object

   .. method:: getInteracted( player, position)

      Returns an entity that player can interact with at position


      :param player:  The player to use for the calculation


      :type player: :class:`Player`

      :param position:  The coordinates to search


      :type position: :class:`Vector`

      :rtype: :class:`Entity`

   .. method:: getTargeted( position[, filter=None])

      Returns an entity that can be targeted at position based on filter rules


      :param position:  Coordinates to search


      :type position: :class:`Vector`

      :param filter: 

      :type filter: object

      :rtype: :class:`Entity`

   .. method:: isActive( )

      Returns true if there are any players in this realm, false otherwise


      :rtype: bool

   .. method:: remove( entity)

      Removes an entity from this realm


      :param entity:  The entity to remove


      :type entity: :class:`Entity`

   .. method:: remove( player)

      Removes a player from this realm


      :param player:  The player to remove


      :type player: :class:`Player`

   .. method:: save( stream)

      Save this realm to a stream


      :param stream:  Where to write to


      :type stream: :class:`DataStream`

   .. method:: update( frameTime)

      Update all sub systems in this realm


      :param frameTime:  elapsed time this frame


      :type frameTime: int

   .. staticmethod:: create( arg1, arg2, game, uid, name, realmSize, groundLevel)

      Creates a new realm according to parameters and returns it


      :param arg1: 

      :type arg1: :class:`Game`

      :param arg2: 

      :type arg2: int

      :param game:  Which game the realm will be in


      :type game: str

      :param uid:  Unique identifier for this realm


      :type uid: :class:`RealmSize`

      :param name:  Text name for this realm


      :type name: :class:`WorldTime`

      :param realmSize:  The size of this realm


      :type realmSize: int

      :param groundLevel:  The ground level value for this realm


      :type groundLevel: dict

      :rtype: :class:`Realm`

   .. staticmethod:: load( game, path, time, stream)

      Loads in a realm from a stream and returns it


      :param game:  Which game the realm will be in


      :type game: :class:`Game`

      :param path:  Path to realm save file


      :type path: object

      :param time:  :class:`Time` from the world


      :type time: :class:`WorldTime`

      :param stream:  Where to read from


      :type stream: :class:`DataStream`

      :rtype: :class:`Realm`

   .. attribute:: automata

       |      :class:`AutomataManager` for this realm


   .. attribute:: biomeTracker

       |      :class:`BiomeTracker` for this realm


   .. attribute:: dropped

       |      :class:`DroppedHandler` for this realm


   .. attribute:: foliage

       |      :class:`FoliageHandler` for this realm


   .. attribute:: groundLevel

       |      Position for ground level


   .. attribute:: layers

       |      :class:`LayerManager` for this realm


   .. attribute:: lighting

       |      LightHandler for this realm


   .. attribute:: loader

       |      :class:`RealmLoader` for this realm


   .. attribute:: loopWidth

       |      X coordinate for world wrap around


   .. attribute:: map

       |      :class:`RealmMap` for this realm


   .. attribute:: name

       |      Text name for this realm


   .. attribute:: onPlayerEnter

      

   .. attribute:: onPlayerLeave

      

   .. attribute:: options

       |      Python dictionary of options


   .. attribute:: path

       |      Path to realm save file


   .. attribute:: physics

       |      :class:`PhysicsHandler` for this realm


   .. attribute:: placement

       |      :class:`PlacementHandler` for this realm


   .. attribute:: players

       |      Players in this realm


   .. attribute:: size

       |      Size of this realm


   .. attribute:: startArea

       |      Start area value


   .. attribute:: startCrystal

       |      Start crystal value


   .. attribute:: surfaceLevel

       |      Position for surface level


   .. attribute:: uid

       |      Unique identifier for this realm


RealmArea
-----------------------------------
.. class:: RealmArea

   

   .. method:: __init__( area[, onSurface=False[, isUnderground=False[, allowLooping=True]]])

      

      :param area: 

      :type area: :class:`Rect`

      :param onSurface: 

      :type onSurface: bool

      :param isUnderground: 

      :type isUnderground: bool

      :param allowLooping: 

      :type allowLooping: bool

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`RealmArea`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: randomDistribute( biometracker, callback, max)

      Randomly use callback function over this :class:`RealmArea`


      :param biometracker:  Level data to effect


      :type biometracker: :class:`BiomeTracker`

      :param callback:  Function to call randomly


      :type callback: object

      :param max:  Maximum times to call callback


      :type max: int

   .. attribute:: area

       |      Coordinates of this :class:`RealmArea`


   .. attribute:: isUnderground

       |      Set to true is underground, false otherwise


   .. attribute:: onSurface

       |      Set to true if on surface, false otherwise


RealmInfo
-----------------------------------
.. class:: RealmInfo

   

   .. method:: __init__( )

      

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`BiomeBackground`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: unpack( stream)

      Reads data from a stream


      :param stream:  Where to read from


      :type stream: :class:`DataStream`

   .. staticmethod:: pack( realm, stream)

      Writes data from realm to the stream


      :param realm:  Data write


      :type realm: :class:`Realm`

      :param stream:  Where to write data


      :type stream: :class:`DataStream`

   .. attribute:: groundLevel

       |      Position for groundLevel


   .. attribute:: name

       |      The name of this :class:`RealmInfo`


   .. attribute:: options

       |      Dictionary of options for this :class:`RealmInfo`


   .. attribute:: size

       |      Coordinates for this :class:`RealmInfo` size


   .. attribute:: startArea

       |      Coordinates for the start area


   .. attribute:: uid

       |      The unique identifier for this :class:`RealmInfo`


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

RealmMap
-----------------------------------
.. class:: RealmMap

   

   .. method:: addMarker( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`Entity`

      :param arg4: 

      :type arg4: str

      :param arg5: 

      :type arg5: bool

   .. method:: moveFullscreen( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: removeMarker( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`Entity`

   .. method:: setOriginToPosition( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

   .. method:: zoomIn( )

      

      :rtype: bool

   .. method:: zoomOut( )

      

      :rtype: bool

   .. attribute:: conflictRegions

      

   .. attribute:: isVisible

      

   .. attribute:: mode

      

   .. attribute:: origin

      

   .. attribute:: position

      

RealmSize
-----------------------------------
.. class:: RealmSize

   

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :param arg3: 

      :type arg3: int

   .. method:: getSegmentId( arg2)

      Gets the segmentId for a given :class:`Vector` position


      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: int

   .. method:: getSegmentId( arg2)

      Gets the segmentId for a given :class:`TileVector` position


      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: int

   .. method:: isTileValid( arg2, arg3)

      Checks if the given tile coordinates are within the bounds of the realm


      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. method:: isValid( arg2)

      Checks if a given tile position is within the bounds of the realm


      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: bool

   .. attribute:: chunkCount

       |      Number of segments in the current realm


   .. attribute:: chunkHeight

       |      Height of the realm in segments


   .. attribute:: chunkWidth

       |      Width of the realm in segments


   .. attribute:: halfHeight

       |      Half the height of realm in pixels


   .. attribute:: halfWidth

       |      Half the width of realm in pixels


   .. attribute:: height

       |      Height of realm in pixels


   .. attribute:: loopTileWidth

       |      Loop tile width of world


   .. attribute:: loopWidth

       |      Loop width of world


   .. attribute:: regionCount

       |      Number of regions in the current realm


   .. attribute:: regionHeight

       |      Height of the realm in regions


   .. attribute:: regionWidth

       |      Width of the realm in regions


   .. attribute:: segmentCount

       |      Number of segments in the current realm


   .. attribute:: segmentHeight

       |      Height of the realm in segments


   .. attribute:: segmentWidth

       |      Width of the realm in segments


   .. attribute:: size

       |      Size of realm in pixels


   .. attribute:: subtileCount

       |      Number of subtiles in the realm


   .. attribute:: subtileHeight

       |      Height of realm in subtiles


   .. attribute:: subtileWidth

       |      Width of realm in subtiles


   .. attribute:: tileCount

       |      Number of tiles in the realm


   .. attribute:: tileHeight

       |      Height of realm in tiles


   .. attribute:: tileWidth

       |      Width of realm in tiles


   .. attribute:: width

       |      Width of realm in pixels


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

AutomataManager
-----------------------------------
.. class:: AutomataManager

   

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`BiomeBackground`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: activateCells( area)

      Mark all cells within area as active


      :param area:  Coordinates to search


      :type area: :class:`Rect`

   .. method:: activateCells( area)

      Mark all cells within area as active


      :param area:  Coordinates to search


      :type area: :class:`PixelRect`

   .. method:: clearNode( x, y)

      Remove cell and sub cells from simulation


      :param x:  X coordinate for search


      :type x: int

      :param y:  Y coordinate for search


      :type y: int

   .. method:: getActiveCount( )

      Return the number of active cells


      :rtype: int

   .. method:: getCell( position)

      Return the first matching cell from this simulation


      :param position:  The coordinates for the search


      :type position: :class:`Vector`

      :returns: Matching cell if found or an empty :class:`AutomataCell` if not found


      :rtype: :class:`AutomataCell`

   .. method:: getCells( area)

      Return a list of cells that are within area


      :param area:  Coordinates to search


      :type area: :class:`Rect`

      :rtype: :class:`CellList`

   .. method:: getCells( area)

      Return a list of cells that are within area


      :param area:  Coordinates to search


      :type area: :class:`PixelRect`

      :rtype: :class:`CellList`

   .. method:: isSettled( )

      Returns true if active count is 0


      :rtype: bool

   .. method:: setCell( x, y, cell)

      Adds a cell to the simulation and activates it


      :param x:  X coordinate of cell


      :type x: int

      :param y:  Y coordinate of cell


      :type y: int

      :param cell:  Cell to add


      :type cell: :class:`AutomataCell`

   .. method:: setCell( position, cell)

      Adds a cell to the simulation and activates it


      :param position:  Coordinates of cell


      :type position: :class:`Vector`

      :param cell:  Cell to add


      :type cell: :class:`AutomataCell`

   .. method:: simulate( )

      Run one step of simulation


   .. attribute:: activeCells

      

   .. attribute:: skippedCells

      

Subsystem)
-----------------------------------
.. class:: Subsystem)

   

Subsystem)
-----------------------------------
.. class:: Subsystem)

   

