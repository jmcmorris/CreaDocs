.. _siege.subsystem:

siege.subsystem
==================

BodyComponentMap
-----------------------------------
.. class:: BodyComponentMap

   

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

CraftComponentMap
-----------------------------------
.. class:: CraftComponentMap

   

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

CustomizationComponentMap
-----------------------------------
.. class:: CustomizationComponentMap

   

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

EquipmentAttributes
-----------------------------------
.. class:: EquipmentAttributes

   

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

ItemComponentMap
-----------------------------------
.. class:: ItemComponentMap

   

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

Subsystem
-----------------------------------
.. class:: Subsystem

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: add( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: add( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: clear( )

      

   .. method:: clear( )

      

   .. method:: create( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: str

      :param arg4: 

      :type arg4: object

   .. method:: create( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: str

      :param arg4: 

      :type arg4: object

   .. method:: freeze( )

      

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: update( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: update( arg2)

      

      :param arg2: 

      :type arg2: int

AnimationSystem
-----------------------------------
.. class:: AnimationSystem

   

BodySystem
-----------------------------------
.. class:: BodySystem

   

   .. method:: getBodies( )

      

      :rtype: :class:`BodyComponentMap`

CraftSystem
-----------------------------------
.. class:: CraftSystem

   

   .. method:: getAvailableInventories( layerManager, layers, playerEntity, reachModifier)

      

      :param layerManager: 

      :type layerManager: :class:`LayerManager`

      :param layers: 

      :type layers: list

      :param playerEntity: 

      :type playerEntity: :class:`Entity`

      :param reachModifier: 

      :type reachModifier: float

      :rtype: list

   .. method:: getAvailableServices( layerManager, layers, playerEntity, reachModifier)

      

      :param layerManager: 

      :type layerManager: :class:`LayerManager`

      :param layers: 

      :type layers: list

      :param playerEntity: 

      :type playerEntity: :class:`Entity`

      :param reachModifier: 

      :type reachModifier: float

      :rtype: :class:`StringSet`

   .. method:: getComponents( )

      

      :rtype: :class:`CraftComponentMap`

CustomizationSystem
-----------------------------------
.. class:: CustomizationSystem

   

   .. method:: getCustomizations( )

      

      :rtype: :class:`CustomizationComponentMap`

EffectsSystem
-----------------------------------
.. class:: EffectsSystem

   

   .. method:: get( effect)

      

      :param effect: 

      :type effect: str

      :rtype: object

   .. method:: getAll( )

      

      :rtype: :class:`ObjectMap`

   .. method:: register( name, effect)

      

      :param name: 

      :type name: str

      :param effect: 

      :type effect: object

EquipmentSystem
-----------------------------------
.. class:: EquipmentSystem

   

   .. method:: create( content, quality[, attributes=[]])

      

      :param content: 

      :type content: :class:`Content`

      :param quality: 

      :type quality: int

      :param attributes: 

      :type attributes: list

      :rtype: :class:`Entity`

   .. method:: getAttributes( )

      

      :rtype: :class:`ObjectMap`

   .. method:: registerAttribute( attribute)

      

      :param attribute: 

      :type attribute: object

FoliageSystem
-----------------------------------
.. class:: FoliageSystem

   

   .. method:: getFoliage( foliageId)

      

      :param foliageId: 

      :type foliageId: int

      :rtype: :class:`FoliageComponent`

   .. method:: getFoliageEntity( foliageId)

      

      :param foliageId: 

      :type foliageId: int

      :rtype: :class:`Entity`

   .. method:: hasFoliage( foliageId)

      

      :param foliageId: 

      :type foliageId: int

      :rtype: bool

ItemsSystem
-----------------------------------
.. class:: ItemsSystem

   

   .. attribute:: components

      

LightSystem
-----------------------------------
.. class:: LightSystem

   

MonsterSystem
-----------------------------------
.. class:: MonsterSystem

   

   .. method:: getConnectedSpawnPosition( arg2, arg3, arg4, arg5, arg6)

      

      :param arg2: 

      :type arg2: :class:`Realm`

      :param arg3: 

      :type arg3: :class:`Entity`

      :param arg4: 

      :type arg4: :class:`Vector`

      :param arg5: 

      :type arg5: :class:`Rect`

      :param arg6: 

      :type arg6: :class:`Rect`

      :rtype: :class:`Vector`

   .. method:: getCount( )

      

      :rtype: int

   .. method:: getMonstersForBiome( biomeName)

      

      :param biomeName: 

      :type biomeName: str

      :rtype: :class:`Entities`

   .. method:: registerAffix( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. attribute:: affixes

      

OrganicSystem
-----------------------------------
.. class:: OrganicSystem

   

   .. method:: checkPosition( arg2, arg3, arg4, arg5, arg6)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: :class:`Realm`

      :param arg4: 

      :type arg4: :class:`Vector`

      :param arg5: 

      :type arg5: :class:`Layer`

      :param arg6: 

      :type arg6: :class:`UnderwaterSupport`

      :rtype: bool

   .. method:: plant( arg2, arg3, arg4, arg5, arg6)

      

      :param arg2: 

      :type arg2: :class:`Content`

      :param arg3: 

      :type arg3: :class:`Realm`

      :param arg4: 

      :type arg4: :class:`Layer`

      :param arg5: 

      :type arg5: :class:`Vector`

      :param arg6: 

      :type arg6: :class:`UnderwaterSupport`

      :rtype: :class:`Entity`

   .. method:: plantMany( arg2, arg3, arg4, arg5, arg6, arg7)

      

      :param arg2: 

      :type arg2: :class:`Content`

      :param arg3: 

      :type arg3: :class:`Realm`

      :param arg4: 

      :type arg4: :class:`RealmArea`

      :param arg5: 

      :type arg5: :class:`Layer`

      :param arg6: 

      :type arg6: int

      :param arg7: 

      :type arg7: :class:`UnderwaterSupport`

      :rtype: :class:`EntitySet`

PhysicsSystem
-----------------------------------
.. class:: PhysicsSystem

   

PlacementSystem
-----------------------------------
.. class:: PlacementSystem

   

   .. method:: damage( damage)

      

      :param damage: 

      :type damage: :class:`Entity`

RenderSystem
-----------------------------------
.. class:: RenderSystem

   

   .. method:: addRenderable( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Renderable`

      :param arg3: 

      :type arg3: int

   .. method:: clearRenderables( )

      

   .. method:: create( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`Entity`

      :param arg3: 

      :type arg3: str

      :param arg4: 

      :type arg4: object

   .. method:: createShader( path[, setCurrentTextureParam=True])

      

      :param path: 

      :type path: str

      :param setCurrentTextureParam: 

      :type setCurrentTextureParam: bool

      :rtype: :class:`Shader`

   .. method:: getImageSize( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: :class:`PixelVector`

   .. method:: getWindowSize( )

      

      :rtype: :class:`PixelVector`

   .. method:: removeRenderable( arg2)

      

      :param arg2: 

      :type arg2: :class:`Renderable`

   .. method:: setMode( mode, displayMode)

      

      :param mode: 

      :type mode: :class:`VideoMode`

      :param displayMode: 

      :type displayMode: :class:`DisplayMode`

   .. method:: setVerticalSync( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: zoomIn( )

      

   .. method:: zoomOut( )

      

   .. attribute:: onResize

      

   .. attribute:: windowPosition

      

   .. attribute:: zoom

      

TileSystem
-----------------------------------
.. class:: TileSystem

   

   .. method:: getTile( tileId)

      

      :param tileId: 

      :type tileId: int

      :rtype: :class:`TileComponent`

   .. method:: getTileEntity( tileId)

      

      :param tileId: 

      :type tileId: int

      :rtype: :class:`Entity`

   .. method:: hasTile( tileId)

      

      :param tileId: 

      :type tileId: int

      :rtype: bool

