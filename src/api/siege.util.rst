.. _siege.util:

siege.util
==================

AssetCache
-----------------------------------
.. class:: AssetCache

   

   .. method:: __init__( )

      

   .. method:: clean( )

      

   .. method:: redirect( path)

      

      :param path: 

      :type path: object

      :rtype: str

   .. method:: redirection( from, to)

      

      :param from: 

      :type from: object

      :param to: 

      :type to: object

   .. staticmethod:: getFullPath( relative, contentPath)

      

      :param relative: 

      :type relative: object

      :param contentPath: 

      :type contentPath: object

      :rtype: str

ChunkRect
-----------------------------------
.. class:: ChunkRect

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkRect`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, width, height)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: __init__( position, size)

      

      :param position: 

      :type position: :class:`ChunkVector`

      :param size: 

      :type size: :class:`ChunkVector`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`sfIntRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`PixelRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SubtileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`TileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SegmentRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`ChunkRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`RegionRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkRect`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: adjust( x, y, width, heigth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param heigth: 

      :type heigth: int

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      

      :rtype: :class:`Rect`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      

      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`ChunkVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`ChunkRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`ChunkRect`

      :param intersection: 

      :type intersection: :class:`ChunkRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: move( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: resize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: toSfml( )

      

      :rtype: :class:`sfIntRect`

   .. attribute:: bottom

      

   .. attribute:: bottomLeft

      

   .. attribute:: bottomRight

      

   .. attribute:: height

      

   .. attribute:: left

      

   .. attribute:: position

      

   .. attribute:: right

      

   .. attribute:: size

      

   .. attribute:: top

      

   .. attribute:: topLeft

      

   .. attribute:: topRight

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

ChunkVector
-----------------------------------
.. class:: ChunkVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __cmp__( vector)

      

      :param vector: 

      :type vector: :class:`ChunkVector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      

      :rtype: :class:`TileVector`

   .. method:: asVector( )

      

      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True]])

      

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]]]])

      

      :param position: 

      :type position: :class:`ChunkVector`

      :param loopWidth: 

      :type loopWidth: int

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`ChunkVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0]])

      

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`ChunkVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: float

   .. method:: loop( loopWidth)

      

      :param loopWidth: 

      :type loopWidth: int

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: shouldLoop( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: toSfml( )

      

      :rtype: :class:`sfTileVector`

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

EventArg
-----------------------------------
.. class:: EventArg

   

   .. method:: __init__( value)

      

      :param value: 

      :type value: object

   .. attribute:: final

      

   .. attribute:: start

      

GameEvent
-----------------------------------
.. class:: GameEvent

   

   .. method:: __init__( )

      

   .. method:: clear( )

      

   .. method:: invoke( )

      

   .. method:: invoke( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: invoke( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: invoke( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: object

   .. method:: invoke( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: object

      :param arg5: 

      :type arg5: object

   .. method:: invoke( arg2, arg3, arg4, arg5, arg6)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: object

      :param arg5: 

      :type arg5: object

      :param arg6: 

      :type arg6: object

   .. method:: invoke( arg2, arg3, arg4, arg5, arg6, arg7)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: object

      :param arg5: 

      :type arg5: object

      :param arg6: 

      :type arg6: object

      :param arg7: 

      :type arg7: object

   .. method:: invoke( arg2, arg3, arg4, arg5, arg6, arg7, arg8)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: object

      :param arg5: 

      :type arg5: object

      :param arg6: 

      :type arg6: object

      :param arg7: 

      :type arg7: object

      :param arg8: 

      :type arg8: object

   .. method:: invoke( arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

      :param arg4: 

      :type arg4: object

      :param arg5: 

      :type arg5: object

      :param arg6: 

      :type arg6: object

      :param arg7: 

      :type arg7: object

      :param arg8: 

      :type arg8: object

      :param arg9: 

      :type arg9: object

   .. method:: invokeExpand( args, kargs)

      

      :param args: 

      :type args: list

      :param kargs: 

      :type kargs: dict

   .. method:: listen( listener)

      

      :param listener: 

      :type listener: object

   .. method:: remove( listener)

      

      :param listener: 

      :type listener: object

      :rtype: bool

ObjectMap
-----------------------------------
.. class:: ObjectMap

   

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

PixelRect
-----------------------------------
.. class:: PixelRect

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelRect`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, width, height)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: __init__( position, size)

      

      :param position: 

      :type position: :class:`PixelVector`

      :param size: 

      :type size: :class:`PixelVector`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`sfIntRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`PixelRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SubtileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`TileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SegmentRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`ChunkRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`RegionRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelRect`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: adjust( x, y, width, heigth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param heigth: 

      :type heigth: int

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      

      :rtype: :class:`Rect`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      

      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`PixelVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`PixelRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`PixelRect`

      :param intersection: 

      :type intersection: :class:`PixelRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: move( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: resize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: toSfml( )

      

      :rtype: :class:`sfIntRect`

   .. attribute:: bottom

      

   .. attribute:: bottomLeft

      

   .. attribute:: bottomRight

      

   .. attribute:: height

      

   .. attribute:: left

      

   .. attribute:: position

      

   .. attribute:: right

      

   .. attribute:: size

      

   .. attribute:: top

      

   .. attribute:: topLeft

      

   .. attribute:: topRight

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

PixelVector
-----------------------------------
.. class:: PixelVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __cmp__( vector)

      

      :param vector: 

      :type vector: :class:`PixelVector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      

      :rtype: :class:`TileVector`

   .. method:: asVector( )

      

      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True]])

      

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]]]])

      

      :param position: 

      :type position: :class:`PixelVector`

      :param loopWidth: 

      :type loopWidth: int

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`PixelVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0]])

      

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`PixelVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: float

   .. method:: loop( loopWidth)

      

      :param loopWidth: 

      :type loopWidth: int

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: shouldLoop( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: toSfml( )

      

      :rtype: :class:`sfTileVector`

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

Property
-----------------------------------
.. class:: Property

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: get( )

      

      :rtype: object

   .. method:: read( stream[, args=[]]])

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param args: 

      :type args: list

   .. method:: set( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: set( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: onChange

      

PropertyBool
-----------------------------------
.. class:: PropertyBool

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: get( )

      

      :rtype: bool

   .. method:: read( stream[, args=[]]])

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param args: 

      :type args: list

   .. method:: set( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: set( arg2, arg3)

      

      :param arg2: 

      :type arg2: bool

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: onChange

      

PropertyInt
-----------------------------------
.. class:: PropertyInt

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: get( )

      

      :rtype: int

   .. method:: read( stream[, args=[]]])

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param args: 

      :type args: list

   .. method:: set( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: set( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: onChange

      

PropertyStr
-----------------------------------
.. class:: PropertyStr

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: get( )

      

      :rtype: str

   .. method:: read( stream[, args=[]]])

      

      :param stream: 

      :type stream: :class:`DataStream`

      :param args: 

      :type args: list

   .. method:: set( arg2)

      

      :param arg2: 

      :type arg2: str

   .. method:: set( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      

      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: onChange

      

Random
-----------------------------------
.. class:: Random

   

   .. staticmethod:: get( arg1, arg2)

      

      :param arg1: 

      :type arg1: float

      :param arg2: 

      :type arg2: float

      :rtype: float

   .. staticmethod:: get( [max=2147483647]])

      

      :param max: 

      :type max: int

      :rtype: int

   .. staticmethod:: get( arg1, arg2)

      

      :param arg1: 

      :type arg1: int

      :param arg2: 

      :type arg2: int

      :rtype: int

   .. staticmethod:: get( arg1)

      

      :param arg1: 

      :type arg1: list

      :rtype: object

   .. staticmethod:: getBool( )

      

      :rtype: bool

   .. staticmethod:: getFloat( )

      

      :rtype: float

   .. staticmethod:: read( arg1)

      

      :param arg1: 

      :type arg1: :class:`DataStream`

   .. staticmethod:: seed( arg1)

      

      :param arg1: 

      :type arg1: int

   .. staticmethod:: write( arg1)

      

      :param arg1: 

      :type arg1: :class:`DataStream`

Range
-----------------------------------
.. class:: Range

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: object

   .. method:: getRandom( )

      

      :rtype: object

   .. attribute:: end

      

   .. attribute:: max

      

   .. attribute:: min

      

   .. attribute:: start

      

RangeColor
-----------------------------------
.. class:: RangeColor

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :param arg3: 

      :type arg3: :class:`Color`

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`Color`

   .. method:: getRandom( )

      

      :rtype: :class:`Color`

   .. attribute:: end

      

   .. attribute:: max

      

   .. attribute:: min

      

   .. attribute:: start

      

RangeFloat
-----------------------------------
.. class:: RangeFloat

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: float

   .. method:: getRandom( )

      

      :rtype: float

   .. attribute:: end

      

   .. attribute:: max

      

   .. attribute:: min

      

   .. attribute:: start

      

RangeInt
-----------------------------------
.. class:: RangeInt

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: int

   .. method:: getRandom( )

      

      :rtype: int

   .. attribute:: end

      

   .. attribute:: max

      

   .. attribute:: min

      

   .. attribute:: start

      

RangeTileVector
-----------------------------------
.. class:: RangeTileVector

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :param arg3: 

      :type arg3: :class:`TileVector`

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`TileVector`

   .. method:: getRandom( )

      

      :rtype: :class:`TileVector`

   .. attribute:: end

      

   .. attribute:: max

      

   .. attribute:: min

      

   .. attribute:: start

      

RangeUint
-----------------------------------
.. class:: RangeUint

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: int

   .. method:: getRandom( )

      

      :rtype: int

   .. attribute:: end

      

   .. attribute:: max

      

   .. attribute:: min

      

   .. attribute:: start

      

RangeVector
-----------------------------------
.. class:: RangeVector

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :param arg3: 

      :type arg3: :class:`Vector`

   .. method:: get( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`Vector`

   .. method:: getRandom( )

      

      :rtype: :class:`Vector`

   .. attribute:: end

      

   .. attribute:: max

      

   .. attribute:: min

      

   .. attribute:: start

      

Rect
-----------------------------------
.. class:: Rect

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Rect`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, width, height)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

      :param width: 

      :type width: float

      :param height: 

      :type height: float

   .. method:: __init__( position, size)

      

      :param position: 

      :type position: :class:`Vector`

      :param size: 

      :type size: :class:`Vector`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`sfRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`PixelRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SubtileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`TileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SegmentRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`ChunkRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`RegionRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Rect`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: adjust( x, y, width, heigth)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

      :param width: 

      :type width: float

      :param heigth: 

      :type heigth: float

   .. method:: asChunk( )

      

      :rtype: object

   .. method:: asPixel( )

      

      :rtype: :class:`Rect`

   .. method:: asRect( )

      

      :rtype: :class:`Rect`

   .. method:: asRegion( )

      

      :rtype: object

   .. method:: asSegment( )

      

      :rtype: object

   .. method:: asSubtile( )

      

      :rtype: object

   .. method:: asTile( )

      

      :rtype: object

   .. method:: contains( x, y[, loopWidth=0]])

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

      :param loopWidth: 

      :type loopWidth: float

      :rtype: bool

   .. method:: contains( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`Vector`

      :param loopWidth: 

      :type loopWidth: float

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`Rect`

      :param loopWidth: 

      :type loopWidth: float

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`Rect`

      :param intersection: 

      :type intersection: :class:`Rect`

      :param loopWidth: 

      :type loopWidth: float

      :rtype: bool

   .. method:: move( x, y)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

   .. method:: move( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: resize( width, height)

      

      :param width: 

      :type width: float

      :param height: 

      :type height: float

   .. method:: toSfml( )

      

      :rtype: :class:`sfRect`

   .. attribute:: bottom

      

   .. attribute:: bottomLeft

      

   .. attribute:: bottomRight

      

   .. attribute:: height

      

   .. attribute:: left

      

   .. attribute:: position

      

   .. attribute:: right

      

   .. attribute:: size

      

   .. attribute:: top

      

   .. attribute:: topLeft

      

   .. attribute:: topRight

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

RegionRect
-----------------------------------
.. class:: RegionRect

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionRect`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, width, height)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: __init__( position, size)

      

      :param position: 

      :type position: :class:`RegionVector`

      :param size: 

      :type size: :class:`RegionVector`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`sfIntRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`PixelRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SubtileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`TileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SegmentRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`ChunkRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`RegionRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionRect`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: adjust( x, y, width, heigth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param heigth: 

      :type heigth: int

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      

      :rtype: :class:`Rect`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      

      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`RegionVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`RegionRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`RegionRect`

      :param intersection: 

      :type intersection: :class:`RegionRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: move( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: resize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: toSfml( )

      

      :rtype: :class:`sfIntRect`

   .. attribute:: bottom

      

   .. attribute:: bottomLeft

      

   .. attribute:: bottomRight

      

   .. attribute:: height

      

   .. attribute:: left

      

   .. attribute:: position

      

   .. attribute:: right

      

   .. attribute:: size

      

   .. attribute:: top

      

   .. attribute:: topLeft

      

   .. attribute:: topRight

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

RegionVector
-----------------------------------
.. class:: RegionVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __cmp__( vector)

      

      :param vector: 

      :type vector: :class:`RegionVector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      

      :rtype: :class:`TileVector`

   .. method:: asVector( )

      

      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True]])

      

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]]]])

      

      :param position: 

      :type position: :class:`RegionVector`

      :param loopWidth: 

      :type loopWidth: int

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`RegionVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0]])

      

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`RegionVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: float

   .. method:: loop( loopWidth)

      

      :param loopWidth: 

      :type loopWidth: int

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: shouldLoop( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: toSfml( )

      

      :rtype: :class:`sfTileVector`

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

SegmentRect
-----------------------------------
.. class:: SegmentRect

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentRect`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, width, height)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: __init__( position, size)

      

      :param position: 

      :type position: :class:`SegmentVector`

      :param size: 

      :type size: :class:`SegmentVector`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`sfIntRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`PixelRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SubtileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`TileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SegmentRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`ChunkRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`RegionRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentRect`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: adjust( x, y, width, heigth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param heigth: 

      :type heigth: int

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      

      :rtype: :class:`Rect`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      

      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`SegmentVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`SegmentRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`SegmentRect`

      :param intersection: 

      :type intersection: :class:`SegmentRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: move( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: resize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: toSfml( )

      

      :rtype: :class:`sfIntRect`

   .. attribute:: bottom

      

   .. attribute:: bottomLeft

      

   .. attribute:: bottomRight

      

   .. attribute:: height

      

   .. attribute:: left

      

   .. attribute:: position

      

   .. attribute:: right

      

   .. attribute:: size

      

   .. attribute:: top

      

   .. attribute:: topLeft

      

   .. attribute:: topRight

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

SegmentVector
-----------------------------------
.. class:: SegmentVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __cmp__( vector)

      

      :param vector: 

      :type vector: :class:`SegmentVector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      

      :rtype: :class:`TileVector`

   .. method:: asVector( )

      

      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True]])

      

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]]]])

      

      :param position: 

      :type position: :class:`SegmentVector`

      :param loopWidth: 

      :type loopWidth: int

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`SegmentVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0]])

      

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`SegmentVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: float

   .. method:: loop( loopWidth)

      

      :param loopWidth: 

      :type loopWidth: int

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: shouldLoop( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: toSfml( )

      

      :rtype: :class:`sfTileVector`

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

Sizes
-----------------------------------
.. class:: Sizes

   

   .. attribute:: CHUNK

      

   .. attribute:: CHUNK_TILE

      

   .. attribute:: PIXEL

      

   .. attribute:: REGION

      

   .. attribute:: REGION_CHUNK

      

   .. attribute:: REGION_SEGMENT

      

   .. attribute:: REGION_SUBTILE

      

   .. attribute:: REGION_TILE

      

   .. attribute:: SEGMENT

      

   .. attribute:: SEGMENT_SUBTILE

      

   .. attribute:: SEGMENT_TILE

      

   .. attribute:: SUBTILE

      

   .. attribute:: TILE

      

   .. attribute:: TILE_SUBTILE

      

SpatialHash
-----------------------------------
.. class:: SpatialHash

   

   .. method:: __init__( size, realmSize)

      

      :param size: 

      :type size: int

      :param realmSize: 

      :type realmSize: :class:`RealmSize`

   .. method:: add( obj)

      

      :param obj: 

      :type obj: object

   .. method:: clear( )

      

   .. method:: clearSections( sections)

      

      :param sections: 

      :type sections: :class:`SegmentList`

   .. method:: get( sections)

      

      :param sections: 

      :type sections: :class:`SegmentList`

      :rtype: object

   .. method:: getAll( )

      

      :rtype: object

   .. method:: getNearby( area)

      

      :param area: 

      :type area: :class:`Rect`

      :rtype: object

   .. method:: getSection( point)

      

      :param point: 

      :type point: :class:`Vector`

      :rtype: int

   .. method:: getSections( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

      :rtype: :class:`SegmentList`

   .. method:: has( obj)

      

      :param obj: 

      :type obj: object

      :rtype: bool

   .. method:: remove( obj)

      

      :param obj: 

      :type obj: object

StringSet
-----------------------------------
.. class:: StringSet

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: str

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

      :type arg2: str

   .. method:: clear( )

      

   .. method:: has( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: str

SubtileRect
-----------------------------------
.. class:: SubtileRect

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileRect`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, width, height)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: __init__( position, size)

      

      :param position: 

      :type position: :class:`SubtileVector`

      :param size: 

      :type size: :class:`SubtileVector`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`sfIntRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`PixelRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SubtileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`TileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SegmentRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`ChunkRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`RegionRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileRect`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: adjust( x, y, width, heigth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param heigth: 

      :type heigth: int

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      

      :rtype: :class:`Rect`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      

      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`SubtileVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`SubtileRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`SubtileRect`

      :param intersection: 

      :type intersection: :class:`SubtileRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: move( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: resize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: toSfml( )

      

      :rtype: :class:`sfIntRect`

   .. attribute:: bottom

      

   .. attribute:: bottomLeft

      

   .. attribute:: bottomRight

      

   .. attribute:: height

      

   .. attribute:: left

      

   .. attribute:: position

      

   .. attribute:: right

      

   .. attribute:: size

      

   .. attribute:: top

      

   .. attribute:: topLeft

      

   .. attribute:: topRight

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

SubtileVector
-----------------------------------
.. class:: SubtileVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __cmp__( vector)

      

      :param vector: 

      :type vector: :class:`SubtileVector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      

      :rtype: :class:`TileVector`

   .. method:: asVector( )

      

      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True]])

      

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]]]])

      

      :param position: 

      :type position: :class:`SubtileVector`

      :param loopWidth: 

      :type loopWidth: int

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`SubtileVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0]])

      

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`SubtileVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: float

   .. method:: loop( loopWidth)

      

      :param loopWidth: 

      :type loopWidth: int

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: shouldLoop( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: toSfml( )

      

      :rtype: :class:`sfTileVector`

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

TileRect
-----------------------------------
.. class:: TileRect

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileRect`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, width, height)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: __init__( position, size)

      

      :param position: 

      :type position: :class:`TileVector`

      :param size: 

      :type size: :class:`TileVector`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`sfIntRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`PixelRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SubtileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`TileRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`SegmentRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`ChunkRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`RegionRect`

   .. method:: __init__( rect)

      

      :param rect: 

      :type rect: :class:`Rect`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileRect`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: adjust( x, y, width, heigth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param width: 

      :type width: int

      :param heigth: 

      :type heigth: int

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      

      :rtype: :class:`Rect`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      

      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`TileVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`TileRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0]])

      

      :param rect: 

      :type rect: :class:`TileRect`

      :param intersection: 

      :type intersection: :class:`TileRect`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: move( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: resize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: toSfml( )

      

      :rtype: :class:`sfIntRect`

   .. attribute:: bottom

      

   .. attribute:: bottomLeft

      

   .. attribute:: bottomRight

      

   .. attribute:: height

      

   .. attribute:: left

      

   .. attribute:: position

      

   .. attribute:: right

      

   .. attribute:: size

      

   .. attribute:: top

      

   .. attribute:: topLeft

      

   .. attribute:: topRight

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

TileVector
-----------------------------------
.. class:: TileVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __cmp__( vector)

      

      :param vector: 

      :type vector: :class:`TileVector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      

      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      

      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      

      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      

      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      

      :rtype: :class:`TileVector`

   .. method:: asVector( )

      

      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True]])

      

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]]]])

      

      :param position: 

      :type position: :class:`TileVector`

      :param loopWidth: 

      :type loopWidth: int

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`TileVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0]])

      

      :param x: 

      :type x: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0]])

      

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`TileVector`

      :param loopWidth: 

      :type loopWidth: int

      :rtype: float

   .. method:: loop( loopWidth)

      

      :param loopWidth: 

      :type loopWidth: int

   .. method:: move( x, y)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

   .. method:: shouldLoop( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: toSfml( )

      

      :rtype: :class:`sfTileVector`

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

Timer
-----------------------------------
.. class:: Timer

   

   .. method:: __iadd__( time)

      

      :param time: 

      :type time: int

      :rtype: :class:`Timer`

   .. method:: __init__( )

      

   .. method:: __init__( time)

      

      :param time: 

      :type time: int

   .. method:: __isub__( time)

      

      :param time: 

      :type time: int

      :rtype: :class:`Timer`

   .. method:: expired( )

      

      :rtype: bool

   .. method:: percentage( )

      

      :rtype: float

   .. method:: remaining( )

      

      :rtype: int

   .. method:: reset( [time=0]])

      

      :param time: 

      :type time: int

   .. method:: total( )

      

      :rtype: int

   .. method:: update( frameTime)

      

      :param frameTime: 

      :type frameTime: int

Uint32List
-----------------------------------
.. class:: Uint32List

   

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

Uint32Set
-----------------------------------
.. class:: Uint32Set

   

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: __contains__( arg2)

      

      :param arg2: 

      :type arg2: int

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

      :type arg2: int

   .. method:: clear( )

      

   .. method:: has( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: int

Vector
-----------------------------------
.. class:: Vector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __cmp__( vector)

      

      :param vector: 

      :type vector: :class:`Vector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`PixelVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SubtileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`TileVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`SegmentVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`ChunkVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`RegionVector`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: object

   .. method:: asPixel( )

      

      :rtype: :class:`Vector`

   .. method:: asRegion( )

      

      :rtype: object

   .. method:: asSegment( )

      

      :rtype: object

   .. method:: asSubtile( )

      

      :rtype: object

   .. method:: asTile( )

      

      :rtype: object

   .. method:: asVector( )

      

      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True]])

      

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]]]])

      

      :param position: 

      :type position: :class:`Vector`

      :param loopWidth: 

      :type loopWidth: float

      :param asDegrees: 

      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`Vector`

      :param loopWidth: 

      :type loopWidth: float

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0]])

      

      :param x: 

      :type x: float

      :param loopWidth: 

      :type loopWidth: float

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0]])

      

      :param y: 

      :type y: float

      :param loopWidth: 

      :type loopWidth: float

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0]])

      

      :param position: 

      :type position: :class:`Vector`

      :param loopWidth: 

      :type loopWidth: float

      :rtype: float

   .. method:: loop( loopWidth)

      

      :param loopWidth: 

      :type loopWidth: float

   .. method:: move( x, y)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

   .. method:: shouldLoop( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: bool

   .. method:: toSfml( )

      

      :rtype: :class:`sfVector`

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

Vector3
-----------------------------------
.. class:: Vector3

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: __idiv__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( x, y, z)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

      :param z: 

      :type z: float

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfVector3f`

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`Vector3`

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector3`

      :rtype: object

   .. method:: asChunk( )

      

      :rtype: object

   .. method:: asPixel( )

      

      :rtype: :class:`Vector3`

   .. method:: asRegion( )

      

      :rtype: object

   .. method:: asSegment( )

      

      :rtype: object

   .. method:: asSubtile( )

      

      :rtype: object

   .. method:: asTile( )

      

      :rtype: object

   .. method:: asVector( )

      

      :rtype: :class:`Vector3`

   .. method:: move( x, y, z)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

      :param z: 

      :type z: float

   .. method:: toSfml( )

      

      :rtype: :class:`sfVector3f`

   .. attribute:: x

      

   .. attribute:: y

      

   .. attribute:: z

      

WeightedRandomGenerator
-----------------------------------
.. class:: WeightedRandomGenerator

   

   .. method:: __call__( [useWorldRandom=False]])

      

      :param useWorldRandom: 

      :type useWorldRandom: bool

      :rtype: int

   .. method:: __call__( start, end[, useWorldRandom=False]])

      

      :param start: 

      :type start: int

      :param end: 

      :type end: int

      :param useWorldRandom: 

      :type useWorldRandom: bool

      :rtype: int

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: list

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Uint32List`

   .. method:: findIndex( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: int

   .. method:: hasWeights( )

      

      :rtype: bool

   .. method:: setWeights( arg2)

      

      :param arg2: 

      :type arg2: list

   .. method:: setWeights( arg2)

      

      :param arg2: 

      :type arg2: :class:`Uint32List`

   .. attribute:: totals

      

WorldRandom
-----------------------------------
.. class:: WorldRandom

   

   .. staticmethod:: get( arg1, arg2)

      

      :param arg1: 

      :type arg1: float

      :param arg2: 

      :type arg2: float

      :rtype: float

   .. staticmethod:: get( [max=2147483647]])

      

      :param max: 

      :type max: int

      :rtype: int

   .. staticmethod:: get( arg1, arg2)

      

      :param arg1: 

      :type arg1: int

      :param arg2: 

      :type arg2: int

      :rtype: int

   .. staticmethod:: get( arg1)

      

      :param arg1: 

      :type arg1: list

      :rtype: object

   .. staticmethod:: getBool( )

      

      :rtype: bool

   .. staticmethod:: getFloat( )

      

      :rtype: float

   .. staticmethod:: read( arg1)

      

      :param arg1: 

      :type arg1: :class:`DataStream`

   .. staticmethod:: seed( arg1)

      

      :param arg1: 

      :type arg1: int

   .. staticmethod:: write( arg1)

      

      :param arg1: 

      :type arg1: :class:`DataStream`

