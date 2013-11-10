.. _siege.worldgen:

siege.worldgen
==================

FillMode
-----------------------------------
.. class:: FillMode

   

   .. data:: ALL = siege.worldgen.FillMode.ALL

   .. data:: OPEN_ONLY = siege.worldgen.FillMode.OPEN_ONLY

   .. data:: SOLID_ONLY = siege.worldgen.FillMode.SOLID_ONLY

   .. data:: names = {'ALL': siege.worldgen.FillMode.ALL, 'OPEN_ONLY': siege.worldg...

   .. data:: values = {0: siege.worldgen.FillMode.ALL, 1: siege.worldgen.FillMode.S...

Biome
-----------------------------------
.. class:: Biome

   

   .. method:: __init__( )

      

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: getActions( )

      

      :rtype: list

   .. method:: getOccurrences( realmSize)

      

      :param realmSize: 

      :type realmSize: :class:`RealmSize`

      :rtype: :class:`RangeUint`

   .. method:: getPostActions( )

      

      :rtype: list

   .. method:: getRules( )

      

      :rtype: dict

   .. method:: getStamps( remainingSpace)

      

      :param remainingSpace: 

      :type remainingSpace: int

      :rtype: list

   .. method:: isCompatible( biome)

      

      :param biome: 

      :type biome: :class:`Biome`

      :rtype: bool

   .. method:: reset( area)

      

      :param area: 

      :type area: :class:`TileRect`

   .. attribute:: back1

       |      Background layers for parallax scrolling.


   .. attribute:: back2

      

   .. attribute:: back3

      

   .. attribute:: frequency

      

   .. attribute:: height

      

   .. attribute:: layer

      

   .. attribute:: name

      

   .. attribute:: sky

      

   .. attribute:: width

      

BoolStamp
-----------------------------------
.. class:: BoolStamp

   

   .. method:: __init__( imagePath, allowFlipX, allowFlipY)

      

      :param imagePath: 

      :type imagePath: str

      :param allowFlipX: 

      :type allowFlipX: bool

      :param allowFlipY: 

      :type allowFlipY: bool

   .. method:: canFlipX( )

      

      :rtype: bool

   .. method:: canFlipY( )

      

      :rtype: bool

   .. method:: get( x, y, size, flipX, flipY)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param size: 

      :type size: :class:`TileVector`

      :param flipX: 

      :type flipX: bool

      :param flipY: 

      :type flipY: bool

      :rtype: bool

ColorStamp
-----------------------------------
.. class:: ColorStamp

   

   .. method:: __init__( imagePath, allowFlipX, allowFlipY]])

      

      :param imagePath: 

      :type imagePath: str

      :param allowFlipX: 

      :type allowFlipX: bool

      :param allowFlipY]]: 

      :type allowFlipY]]: bool

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: canFlipX( )

      

      :rtype: bool

   .. method:: canFlipY( )

      

      :rtype: bool

   .. method:: forceFlipX( )

      

      :rtype: bool

   .. method:: get( x, y, size, flipX, flipY)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param size: 

      :type size: :class:`TileVector`

      :param flipX: 

      :type flipX: bool

      :param flipY: 

      :type flipY: bool

      :rtype: int

   .. method:: getColor( color)

      

      :param color: 

      :type color: int

      :rtype: :class:`TileVectorList`

   .. method:: getSimple( x, y, flipX)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param flipX: 

      :type flipX: bool

      :rtype: int

   .. method:: getSize( )

      

      :rtype: :class:`TileVector`

   .. method:: has( color)

      

      :param color: 

      :type color: int

      :rtype: bool

   .. method:: setForceFlipX( flipX)

      

      :param flipX: 

      :type flipX: bool

   .. attribute:: image

      

Terraform
-----------------------------------
.. class:: Terraform

   

   .. method:: __init__( game, world)

      

      :param game: 

      :type game: :class:`Game`

      :param world: 

      :type world: :class:`World`

   .. staticmethod:: applySimpleStamp( stamp, position, rules, flipX, ground, wall, automata)

      

      :param stamp: 

      :type stamp: :class:`ColorStamp`

      :param position: 

      :type position: :class:`TileVector`

      :param rules: 

      :type rules: dict

      :param flipX: 

      :type flipX: bool

      :param ground: 

      :type ground: :class:`TileLayer`

      :param wall: 

      :type wall: :class:`TileLayer`

      :param automata: 

      :type automata: :class:`AutomataManager`

   .. staticmethod:: createSegments( layer, area, tileId)

      

      :param layer: 

      :type layer: :class:`TileLayer`

      :param area: 

      :type area: :class:`SegmentRect`

      :param tileId: 

      :type tileId: int

   .. staticmethod:: fillTiles( layer, area, tileId, fillMode)

      

      :param layer: 

      :type layer: :class:`TileLayer`

      :param area: 

      :type area: :class:`TileRect`

      :param tileId: 

      :type tileId: int

      :param fillMode: 

      :type fillMode: :class:`FillMode`

   .. staticmethod:: overlapsSurface( startX, y, width, threshold, realmSize)

      

      :param startX: 

      :type startX: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param threshold: 

      :type threshold: list

      :param realmSize: 

      :type realmSize: :class:`RealmSize`

      :rtype: bool

   .. staticmethod:: placeTiles( arg1, area, layer, fillMode, stamp)

      

      :param arg1: 

      :type arg1: int

      :param area: 

      :type area: :class:`TileRect`

      :param layer: 

      :type layer: :class:`TileLayer`

      :param fillMode: 

      :type fillMode: :class:`FillMode`

      :param stamp: 

      :type stamp: :class:`BoolStamp`

   .. staticmethod:: populateAreaEmptyThreshold( layer, area, tolerance, threshold)

      

      :param layer: 

      :type layer: :class:`TileLayer`

      :param area: 

      :type area: :class:`TileRect`

      :param tolerance: 

      :type tolerance: int

      :param threshold: 

      :type threshold: list

   .. staticmethod:: populateMapAutomataData( realm, data)

      

      :param realm: 

      :type realm: :class:`Realm`

      :param data: 

      :type data: list

   .. staticmethod:: populateMapData( realm, data, colors)

      

      :param realm: 

      :type realm: :class:`Realm`

      :param data: 

      :type data: list

      :param colors: 

      :type colors: dict

TileVectorList
-----------------------------------
.. class:: TileVectorList

   

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

