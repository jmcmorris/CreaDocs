.. _siege.worldgen:

siege.worldgen
==================

FillMode
-----------------------------------
.. class:: FillMode

   

   .. data:: ALL = siege.worldgen.FillMode.ALL

   .. data:: OPEN_ONLY = siege.worldgen.FillMode.OPEN_ONLY

   .. data:: SOLID_ONLY = siege.worldgen.FillMode.SOLID_ONLY

Biome
-----------------------------------
.. class:: Biome

   

   .. method:: __init__( )

      

   .. method:: __repr__( )

      Returns a printable representation of this object.


      :rtype: str

   .. method:: getActions( )

      Returns a Python list


      :rtype: list

   .. method:: getOccurrences( realmSize)

      Returns a :class:`Range` of ints from 0 to 9999


      :param realmSize:  A :class:`RealmSize`


      :type realmSize: :class:`RealmSize`

      :rtype: :class:`RangeUint`

   .. method:: getPostActions( )

      Returns a Python list


      :rtype: list

   .. method:: getRules( )

      Returns a Python dictionary


      :rtype: dict

   .. method:: getStamps( remainingSpace)

      Returns a Python list


      :param remainingSpace:  Has no use


      :type remainingSpace: int

      :rtype: list

   .. method:: isCompatible( biome)

      True if biome is marked compatible, false otherwise


      :param biome:  A :class:`Biome`


      :type biome: :class:`Biome`

      :rtype: bool

   .. method:: reset( area)

      Currently has no effect


      :param area:  A :class:`TileRect`


      :type area: :class:`TileRect`

   .. attribute:: back1

       |      First background layer for parallax scrolling.


   .. attribute:: back2

       |      Second background layer for parallax scrolling.


   .. attribute:: back3

       |      Third background layer for parallax scrolling.


   .. attribute:: back4

       |      Fourth background layer for parallax scrolling.


   .. attribute:: frequency

       |      How often this :class:`Biome` will occur


   .. attribute:: height

       |      Height of the :class:`Biome`


   .. attribute:: layer

       |      The :class:`Layer` name


   .. attribute:: name

       |      The name of the :class:`Biome`


   .. attribute:: sky

       |      Name of the sky


   .. attribute:: width

       |      Width of the :class:`Biome`


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

      Set to true to allow flipping image on x axis


      :rtype: bool

   .. method:: canFlipY( )

      Set to true to allow flipping image on y axis


      :rtype: bool

   .. method:: get( x, y, size, flipX, flipY)

      Returns boolean value at x,y based on size


      :param x:  X coordinate


      :type x: int

      :param y:  Y coordinate


      :type y: int

      :param size:  :class:`TileVector` to scale by


      :type size: :class:`TileVector`

      :param flipX:  Set to true to flip on X axis


      :type flipX: bool

      :param flipY:  Set to true to flip on Y axis


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

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`ColorStamp`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: canFlipX( )

      Set to true to allow flipping image on x axis


      :rtype: bool

   .. method:: canFlipY( )

      Set to true to allow flipping image on y axis


      :rtype: bool

   .. method:: forceFlipX( )

      Return true if forced flipping is active, false otherwise


      :rtype: bool

   .. method:: get( x, y, size, flipX, flipY)

      Returns color value at x,y based on size


      :param x:  X coordinate


      :type x: int

      :param y:  Y coordinate


      :type y: int

      :param size:  :class:`TileVector` to scale by


      :type size: :class:`TileVector`

      :param flipX:  Set to true to flip on X axis


      :type flipX: bool

      :param flipY:  Set to true to flip on Y axis


      :type flipY: bool

      :rtype: int

   .. method:: getColor( color)

      If color is present in ColorMap return color value


      :param color:  :class:`Color`


      :type color: int

      :rtype: :class:`TileVectorList`

   .. method:: getSimple( x, y, flipX)

      Returns color value at x,y


      :param x:  X coordinate


      :type x: int

      :param y:  Y coordinate


      :type y: int

      :param flipX:  Set to true to flip on X axis


      :type flipX: bool

      :rtype: int

   .. method:: getSize( )

      Returns a :class:`TileVector` of the size of the ColorMap


      :rtype: :class:`TileVector`

   .. method:: has( color)

      Returns true if color is in this :class:`ColorStamp`


      :param color:  :class:`Color` to search for


      :type color: int

      :returns: A :class:`TileVectorList` of the color


      :rtype: bool

   .. method:: setForceFlipX( flipX)

      Changes force flipping behavior


      :param flipX:  Set to true to force flip the image on the x axis


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

      Change all tiles under area according to the stamp pattern


      :param stamp:  Pattern to use


      :type stamp: :class:`ColorStamp`

      :param position:  Target for change


      :type position: :class:`TileVector`

      :param rules:  Python dictionary of rules for changes


      :type rules: dict

      :param flipX:  Set to true to force flip stamp on x axis


      :type flipX: bool

      :param ground:  Ground layer to be changed


      :type ground: :class:`TileLayer`

      :param wall:  Wall layer to be changed


      :type wall: :class:`TileLayer`

      :param automata:  An instance of :class:`AutomataManager`


      :type automata: :class:`AutomataManager`

   .. staticmethod:: fillTiles( layer, area, tileId, fillMode)

      Change all tiles under area to tiles of tileId


      :param layer:  :class:`Layer` to change tiles in


      :type layer: :class:`TileLayer`

      :param area:  Coordinates to change


      :type area: :class:`TileRect`

      :param tileId:  Id to change to tiles to


      :type tileId: int

      :param fillMode:  Set to ALL to change any tiles.  Set to OPEN_ONLY to change only open tiles.  Set to SOLID_ONLY to change only solid tiles.


      :type fillMode: :class:`FillMode`

   .. staticmethod:: overlapsSurface( startX, y, width, threshold, realmSize)

      Returns true if surface overlaps threshold tolerance, false otherwise


      :param startX:  Starting x coordinate of surface


      :type startX: int

      :param y:  Y coordinate of surface


      :type y: int

      :param width:  Width of surface


      :type width: int

      :param threshold:  List of values from a populateAreaEmptyThreshold call


      :type threshold: list

      :param realmSize: 

      :type realmSize: :class:`RealmSize`

      :rtype: bool

   .. staticmethod:: placeTiles( arg1, area, layer, fillMode, stamp)

      Change all tiles under area according to the stamp pattern


      :param arg1: 

      :type arg1: int

      :param area:  Coordinates to change


      :type area: :class:`TileRect`

      :param layer:  :class:`Layer` to change tiles in


      :type layer: :class:`TileLayer`

      :param fillMode:  Set to ALL to change any tiles.  Set to OPEN_ONLY to change only open tiles.  Set to SOLID_ONLY to change only solid tiles. 


      :type fillMode: :class:`FillMode`

      :param stamp:   Pattern image to follow


      :type stamp: :class:`BoolStamp`

   .. staticmethod:: populateAreaEmptyThreshold( layer, area, tolerance, threshold)

      After calling Threshold stores a dictionary of x values mapped to their y values added to the threshold


      :param layer:  What layer area is inside


      :type layer: :class:`TileLayer`

      :param area:  Dimensions to change


      :type area: :class:`TileRect`

      :param tolerance:  How deep to dig


      :type tolerance: int

      :param threshold: 

      :type threshold: list

   .. staticmethod:: populateMapAutomataData( realm, data)

      Populate a realm using automata, storing values in data


      :param realm:  Which realm to target


      :type realm: :class:`Realm`

      :param data:  Where to store results


      :type data: list

   .. staticmethod:: populateMapData( realm, data, colors)

      Fill a list of color data from target realm


      :param realm:  Which realm to target


      :type realm: :class:`Realm`

      :param data:  Python list to fill with data


      :type data: list

      :param colors:  Python dictionary of colors


      :type colors: dict

