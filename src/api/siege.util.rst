.. _siege.util:

siege.util
==================

AssetCache
-----------------------------------
.. class:: AssetCache

   

   .. method:: __init__( )

      

   .. method:: clean( )

      Clean up all redirections.


   .. method:: redirect( path)

      

      :param path: 

      :type path: object

      :returns: Returns the redirected path, if set. Otherwise returns the unchanged argument.


      :rtype: str

   .. method:: redirection( from, to)

      Set up a path redirection.


      :param from: 

      :type from: object

      :param to: 

      :type to: object

   .. staticmethod:: getFullPath( relative, contentPath)

      Returns full path to asset.


      :param relative: 

      :type relative: object

      :param contentPath: 

      :type contentPath: object

      :returns: :param relative: if already prefixed with mods/, else returns full path.


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

      A printable representation of this object.


      :rtype: str

   .. method:: adjust( x, y, width, height)

      Move by x,y then resize to width and height


      :param x:  Value to be added x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkRect`


      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelRect`


      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      Create a copy of this as a :class:`Rect`


      :rtype: :class:`Rect`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionRect`


      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentRect`


      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileRect`


      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileRect`


      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0])

      Return true if x,y are within this rectangle false otherwise


      :param x:  x position to check


      :type x: int

      :param y:  y position to check


      :type y: int

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0])

      Return true if positiion is within this rectangle false otherwise


      :param position:  x,y coordinates to check


      :type position: :class:`ChunkVector`

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise


      :param rect:  Rectangle to check against


      :type rect: :class:`ChunkRect`

      :param loopWidth:   How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise.  Saves overlapping coordinates to parameter intersection 


      :param rect:  Rectangle to check against


      :type rect: :class:`ChunkRect`

      :param intersection:  overlapping coordinates are stored here


      :type intersection: :class:`ChunkRect`

      :param loopWidth:  How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: move( position)

      Adds position to x,y coordinates


      :param position:  Value to be added to x,y coordinates


      :type position: :class:`ChunkVector`

   .. method:: resize( width, height)

      Expands width and height


      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfRect`


      :rtype: :class:`sfIntRect`

   .. staticmethod:: fromCenter( center, size)

      Create a new Rectangle from the center point.


      :param center: 

      :type center: :class:`ChunkVector`

      :param size: 

      :type size: :class:`ChunkVector`

      :rtype: :class:`ChunkRect`

   .. attribute:: bottom

       |      y + height


   .. attribute:: bottomLeft

       |      (:class:`Vector`) Bottom Left x,y coordinates.


   .. attribute:: bottomRight

       |      (:class:`Vector`) Bottom Right x,y coordinates.


   .. attribute:: center

       |      (:class:`Vector`) Center coordinates of Rectangle.


   .. attribute:: height

       |      Size from y to bottom.


   .. attribute:: left

       |      x coordinate


   .. attribute:: position

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: right

       |      x + width


   .. attribute:: size

       |      width * height


   .. attribute:: top

       |      y coordinate


   .. attribute:: topLeft

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: topRight

       |      (:class:`Vector`) Top Right x,y coordinates.


   .. attribute:: width

       |      Size from x to right.


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


ChunkVector
-----------------------------------
.. class:: ChunkVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __cmp__( vector)

      Compares this to another vector


      :param vector:  The vector to compare against


      :type vector: :class:`ChunkVector`

      :returns: 0 if vectors are the same, -1 if arg is greater, 1 if arg is less than


      :rtype: int

   .. method:: __div__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`ChunkVector`

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

   .. method:: __init__( x, y, loopWidth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position, loopWidth)

      

      :param position: 

      :type position: :class:`sfTileVector`

      :param loopWidth: 

      :type loopWidth: int

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

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`ChunkVector`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`ChunkVector`

      :rtype: object

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkVector`


      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelVector`


      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionVector`


      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentVector`


      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileVector`


      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileVector`


      :rtype: :class:`TileVector`

   .. method:: asVector( )

      Create a copy of this as a vector


      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True])

      Return the angle or direction of this vector


      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]])

      Return the angle or direction of position


      :param position:  The vector to convert


      :type position: :class:`ChunkVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0])

      Returns a unit vector in the direction of position


      :param position:  The :class:`Vector` to calculate direction from


      :type position: :class:`ChunkVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0])

      Returns direction towards x


      :param x:  X coordinate for direction calculation


      :type x: int

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0])

      Returns direction towards y


      :param y:  Y coordinate for direction calculation


      :type y: int

      :param loopWidth:  Currently has no effect


      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0])

      Returns the distance from position


      :param position:  The :class:`Vector` to calculate distance from


      :type position: :class:`ChunkVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: float

   .. method:: isDefault( )

      Returns true if x==0 and y==0, false otherwise


      :rtype: bool

   .. method:: loop( loopWidth)

      Adds loopWidth to x if x < 0.  Subtracts loopWidth from x if x >= loopWidth


      :param loopWidth:  Amount to adjust x coordinate


      :type loopWidth: int

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: shouldLoop( loopWidth)

      Returns True if x < 0 or x >= loopWidth


      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: bool

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfTileVector`


      :rtype: :class:`sfTileVector`

   .. attribute:: height

       |      y coordinate


   .. attribute:: width

       |      x coordinate


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


Clock
-----------------------------------
.. class:: Clock

   

   .. method:: __init__( )

      

   .. method:: getElapsedTime( )

      

      :rtype: :class:`Time`

   .. method:: restart( )

      

      :rtype: :class:`Time`

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

      Removes all listeners


   .. method:: invoke( )

      Calls all listener functions


   .. method:: invoke( arg)

      Calls all listener functions using 1 argument


      :param arg:  The argument for the listeners


      :type arg: object

   .. method:: invoke( arg1, arg2)

      Calls all listener functions using 2 argument


      :param arg1:  The first argument for the listeners


      :type arg1: object

      :param arg2:  The second argument for the listeners


      :type arg2: object

   .. method:: invoke( arg1, arg2, arg3)

      Calls all listener functions using 3 argument


      :param arg1:  The first argument for the listeners


      :type arg1: object

      :param arg2:  The second argument for the listeners


      :type arg2: object

      :param arg3:  The third argument for the listeners


      :type arg3: object

   .. method:: invoke( arg1, arg2, arg3, arg4)

      Calls all listener functions using 4 argument


      :param arg1:  The first argument for the listeners


      :type arg1: object

      :param arg2:  The second argument for the listeners


      :type arg2: object

      :param arg3:  The third argument for the listeners


      :type arg3: object

      :param arg4:  The fourth argument for the listeners


      :type arg4: object

   .. method:: invoke( arg1, arg2, arg3, arg4, arg5)

      Calls all listener functions using 5 argument


      :param arg1:  The first argument for the listeners


      :type arg1: object

      :param arg2:  The second argument for the listeners


      :type arg2: object

      :param arg3:  The third argument for the listeners


      :type arg3: object

      :param arg4:  The fourth argument for the listeners


      :type arg4: object

      :param arg5:  The fifth argument for the listeners


      :type arg5: object

   .. method:: invoke( arg1, arg2, arg3, arg4, arg5, arg6)

      Calls all listener functions using 6 argument


      :param arg1:  The first argument for the listeners


      :type arg1: object

      :param arg2:  The second argument for the listeners


      :type arg2: object

      :param arg3:  The third argument for the listeners


      :type arg3: object

      :param arg4:  The fourth argument for the listeners


      :type arg4: object

      :param arg5:  The fifth argument for the listeners


      :type arg5: object

      :param arg6:  The sixth argument for the listeners


      :type arg6: object

   .. method:: invoke( arg1, arg2, arg3, arg4, arg5, arg6, arg7)

      Calls all listener functions using 7 argument


      :param arg1:  The first argument for the listeners


      :type arg1: object

      :param arg2:  The second argument for the listeners


      :type arg2: object

      :param arg3:  The third argument for the listeners


      :type arg3: object

      :param arg4:  The fourth argument for the listeners


      :type arg4: object

      :param arg5:  The fifth argument for the listeners


      :type arg5: object

      :param arg6:  The sixth argument for the listeners


      :type arg6: object

      :param arg7:  The seventh argument for the listeners


      :type arg7: object

   .. method:: invoke( arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

      Calls all listener functions using 8 argument


      :param arg1:  The first argument for the listeners


      :type arg1: object

      :param arg2:  The second argument for the listeners


      :type arg2: object

      :param arg3:  The third argument for the listeners


      :type arg3: object

      :param arg4:  The fourth argument for the listeners


      :type arg4: object

      :param arg5:  The fifth argument for the listeners


      :type arg5: object

      :param arg6:  The sixth argument for the listeners


      :type arg6: object

      :param arg7:  The seventh argument for the listeners


      :type arg7: object

      :param arg8:  The eighth argument for the listeners


      :type arg8: object

   .. method:: invokeExpand( args, kargs)

      Calls all listener functions using arguments


      :param args:  List of arguments


      :type args: list

      :param kargs:  Dictionary of arguments


      :type kargs: dict

   .. method:: listen( listener)

      Adds a listener function to this event


      :param listener:  The function to add


      :type listener: object

   .. method:: remove( listener)

      Removes the listener from the :class:`GameEvent`


      :param listener:  The function to remove


      :type listener: object

      :returns: True if successfully removed, false otherwise


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

      A printable representation of this object.


      :rtype: str

   .. method:: adjust( x, y, width, height)

      Move by x,y then resize to width and height


      :param x:  Value to be added x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkRect`


      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelRect`


      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      Create a copy of this as a :class:`Rect`


      :rtype: :class:`Rect`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionRect`


      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentRect`


      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileRect`


      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileRect`


      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0])

      Return true if x,y are within this rectangle false otherwise


      :param x:  x position to check


      :type x: int

      :param y:  y position to check


      :type y: int

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0])

      Return true if positiion is within this rectangle false otherwise


      :param position:  x,y coordinates to check


      :type position: :class:`PixelVector`

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise


      :param rect:  Rectangle to check against


      :type rect: :class:`PixelRect`

      :param loopWidth:   How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise.  Saves overlapping coordinates to parameter intersection 


      :param rect:  Rectangle to check against


      :type rect: :class:`PixelRect`

      :param intersection:  overlapping coordinates are stored here


      :type intersection: :class:`PixelRect`

      :param loopWidth:  How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: move( position)

      Adds position to x,y coordinates


      :param position:  Value to be added to x,y coordinates


      :type position: :class:`PixelVector`

   .. method:: resize( width, height)

      Expands width and height


      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfRect`


      :rtype: :class:`sfIntRect`

   .. staticmethod:: fromCenter( center, size)

      Create a new Rectangle from the center point.


      :param center: 

      :type center: :class:`PixelVector`

      :param size: 

      :type size: :class:`PixelVector`

      :rtype: :class:`PixelRect`

   .. attribute:: bottom

       |      y + height


   .. attribute:: bottomLeft

       |      (:class:`Vector`) Bottom Left x,y coordinates.


   .. attribute:: bottomRight

       |      (:class:`Vector`) Bottom Right x,y coordinates.


   .. attribute:: center

       |      (:class:`Vector`) Center coordinates of Rectangle.


   .. attribute:: height

       |      Size from y to bottom.


   .. attribute:: left

       |      x coordinate


   .. attribute:: position

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: right

       |      x + width


   .. attribute:: size

       |      width * height


   .. attribute:: top

       |      y coordinate


   .. attribute:: topLeft

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: topRight

       |      (:class:`Vector`) Top Right x,y coordinates.


   .. attribute:: width

       |      Size from x to right.


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


PixelVector
-----------------------------------
.. class:: PixelVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __cmp__( vector)

      Compares this to another vector


      :param vector:  The vector to compare against


      :type vector: :class:`PixelVector`

      :returns: 0 if vectors are the same, -1 if arg is greater, 1 if arg is less than


      :rtype: int

   .. method:: __div__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`PixelVector`

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

   .. method:: __init__( x, y, loopWidth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position, loopWidth)

      

      :param position: 

      :type position: :class:`sfTileVector`

      :param loopWidth: 

      :type loopWidth: int

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

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`PixelVector`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`PixelVector`

      :rtype: object

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkVector`


      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelVector`


      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionVector`


      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentVector`


      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileVector`


      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileVector`


      :rtype: :class:`TileVector`

   .. method:: asVector( )

      Create a copy of this as a vector


      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True])

      Return the angle or direction of this vector


      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]])

      Return the angle or direction of position


      :param position:  The vector to convert


      :type position: :class:`PixelVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0])

      Returns a unit vector in the direction of position


      :param position:  The :class:`Vector` to calculate direction from


      :type position: :class:`PixelVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0])

      Returns direction towards x


      :param x:  X coordinate for direction calculation


      :type x: int

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0])

      Returns direction towards y


      :param y:  Y coordinate for direction calculation


      :type y: int

      :param loopWidth:  Currently has no effect


      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0])

      Returns the distance from position


      :param position:  The :class:`Vector` to calculate distance from


      :type position: :class:`PixelVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: float

   .. method:: isDefault( )

      Returns true if x==0 and y==0, false otherwise


      :rtype: bool

   .. method:: loop( loopWidth)

      Adds loopWidth to x if x < 0.  Subtracts loopWidth from x if x >= loopWidth


      :param loopWidth:  Amount to adjust x coordinate


      :type loopWidth: int

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: shouldLoop( loopWidth)

      Returns True if x < 0 or x >= loopWidth


      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: bool

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfTileVector`


      :rtype: :class:`sfTileVector`

   .. attribute:: height

       |      y coordinate


   .. attribute:: width

       |      x coordinate


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


Property
-----------------------------------
.. class:: Property

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: get( )

      Returns data


      :rtype: object

   .. method:: read( stream)

      Read this :class:`Property` from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

   .. method:: read( stream, args)

      Read this property from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

      :param args:  Additional arguments to pass to onChange event.


      :type args: list

   .. method:: set( arg2)

      Changes data to parameter


      :param arg2: 

      :type arg2: object

   .. method:: set( arg2, arg3)

      Changes data to parameter


      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      Write this :class:`Property` to a :class:`DataStream`.


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

      Returns data


      :rtype: bool

   .. method:: read( stream)

      Read this :class:`Property` from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

   .. method:: read( stream, args)

      Read this property from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

      :param args:  Additional arguments to pass to onChange event.


      :type args: list

   .. method:: set( arg2)

      Changes data to parameter


      :param arg2: 

      :type arg2: bool

   .. method:: set( arg2, arg3)

      Changes data to parameter


      :param arg2: 

      :type arg2: bool

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      Write this :class:`Property` to a :class:`DataStream`.


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

      Returns data


      :rtype: int

   .. method:: read( stream)

      Read this :class:`Property` from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

   .. method:: read( stream, args)

      Read this property from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

      :param args:  Additional arguments to pass to onChange event.


      :type args: list

   .. method:: set( arg2)

      Changes data to parameter


      :param arg2: 

      :type arg2: int

   .. method:: set( arg2, arg3)

      Changes data to parameter


      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      Write this :class:`Property` to a :class:`DataStream`.


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

      Returns data


      :rtype: str

   .. method:: read( stream)

      Read this :class:`Property` from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

   .. method:: read( stream, args)

      Read this property from a stream and invokes its onChange event.


      :param stream:  :class:`DataStream` to read from.


      :type stream: :class:`DataStream`

      :param args:  Additional arguments to pass to onChange event.


      :type args: list

   .. method:: set( arg2)

      Changes data to parameter


      :param arg2: 

      :type arg2: str

   .. method:: set( arg2, arg3)

      Changes data to parameter


      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: list

   .. method:: write( arg2)

      Write this :class:`Property` to a :class:`DataStream`.


      :param arg2: 

      :type arg2: :class:`DataStream`

   .. attribute:: onChange

      

Random
-----------------------------------
.. class:: Random

   

   .. staticmethod:: get( min, max)

      Return random float within min and max


      :param min:  minimum value in range


      :type min: float

      :param max:  maximum value in range


      :type max: float

      :rtype: float

   .. staticmethod:: get( [max=2147483647])

      Returns an integer from 0 to max


      :param max:  maximum value for range


      :type max: int

      :rtype: int

   .. staticmethod:: get( min, max)

      Return random integer within min and max


      :param min:  minimum value in range


      :type min: int

      :param max:  maximum value in range


      :type max: int

      :rtype: int

   .. staticmethod:: get( list)

      Returns a random element from passed in list


      :param list:  an element will be chosed at random from this


      :type list: list

      :rtype: object

   .. staticmethod:: getBool( )

      Returns true or false randomly


      :rtype: bool

   .. staticmethod:: getFloat( )

      Returns a random float from 0.0 to 1.0


      :rtype: float

   .. staticmethod:: read( stream)

      read current seed from stream


      :param stream:  where to read from


      :type stream: :class:`DataStream`

   .. staticmethod:: seed( seed)

      Sets the seed for generating numbers


      :param seed:  set seed to this value


      :type seed: int

   .. staticmethod:: write( stream)

      Write current seed to stream


      :param stream:  where to write to


      :type stream: :class:`DataStream`

Range
-----------------------------------
.. class:: Range

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: object

   .. method:: contains( arg2)

      Returns true if value is within range, false otherwise


      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: get( arg2)

      Retruns a value from within range based on percentage passed in


      :param arg2: 

      :type arg2: float

      :rtype: object

   .. method:: getRandom( )

      Returns a random value within range


      :rtype: object

   .. attribute:: end

       |      Returns maximum value in range


   .. attribute:: max

       |      Returns maximum value in range


   .. attribute:: min

       |      Returns minimum value in range


   .. attribute:: start

       |      Returns minimum value in range


RangeColor
-----------------------------------
.. class:: RangeColor

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :param arg3: 

      :type arg3: :class:`Color`

   .. method:: contains( arg2)

      Returns true if value is within range, false otherwise


      :param arg2: 

      :type arg2: :class:`Color`

      :rtype: bool

   .. method:: get( arg2)

      Retruns a value from within range based on percentage passed in


      :param arg2: 

      :type arg2: float

      :rtype: :class:`Color`

   .. method:: getRandom( )

      Returns a random value within range


      :rtype: :class:`Color`

   .. attribute:: end

       |      Returns maximum value in range


   .. attribute:: max

       |      Returns maximum value in range


   .. attribute:: min

       |      Returns minimum value in range


   .. attribute:: start

       |      Returns minimum value in range


RangeFloat
-----------------------------------
.. class:: RangeFloat

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: contains( arg2)

      Returns true if value is within range, false otherwise


      :param arg2: 

      :type arg2: float

      :rtype: bool

   .. method:: get( arg2)

      Retruns a value from within range based on percentage passed in


      :param arg2: 

      :type arg2: float

      :rtype: float

   .. method:: getRandom( )

      Returns a random value within range


      :rtype: float

   .. attribute:: end

       |      Returns maximum value in range


   .. attribute:: max

       |      Returns maximum value in range


   .. attribute:: min

       |      Returns minimum value in range


   .. attribute:: start

       |      Returns minimum value in range


RangeInt
-----------------------------------
.. class:: RangeInt

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: contains( arg2)

      Returns true if value is within range, false otherwise


      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: get( arg2)

      Retruns a value from within range based on percentage passed in


      :param arg2: 

      :type arg2: float

      :rtype: int

   .. method:: getRandom( )

      Returns a random value within range


      :rtype: int

   .. attribute:: end

       |      Returns maximum value in range


   .. attribute:: max

       |      Returns maximum value in range


   .. attribute:: min

       |      Returns minimum value in range


   .. attribute:: start

       |      Returns minimum value in range


RangeTileVector
-----------------------------------
.. class:: RangeTileVector

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :param arg3: 

      :type arg3: :class:`TileVector`

   .. method:: contains( arg2)

      Returns true if value is within range, false otherwise


      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: bool

   .. method:: get( arg2)

      Retruns a value from within range based on percentage passed in


      :param arg2: 

      :type arg2: float

      :rtype: :class:`TileVector`

   .. method:: getRandom( )

      Returns a random value within range


      :rtype: :class:`TileVector`

   .. attribute:: end

       |      Returns maximum value in range


   .. attribute:: max

       |      Returns maximum value in range


   .. attribute:: min

       |      Returns minimum value in range


   .. attribute:: start

       |      Returns minimum value in range


RangeUint
-----------------------------------
.. class:: RangeUint

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: contains( arg2)

      Returns true if value is within range, false otherwise


      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: get( arg2)

      Retruns a value from within range based on percentage passed in


      :param arg2: 

      :type arg2: float

      :rtype: int

   .. method:: getRandom( )

      Returns a random value within range


      :rtype: int

   .. attribute:: end

       |      Returns maximum value in range


   .. attribute:: max

       |      Returns maximum value in range


   .. attribute:: min

       |      Returns minimum value in range


   .. attribute:: start

       |      Returns minimum value in range


RangeVector
-----------------------------------
.. class:: RangeVector

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :param arg3: 

      :type arg3: :class:`Vector`

   .. method:: contains( arg2)

      Returns true if value is within range, false otherwise


      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: bool

   .. method:: get( arg2)

      Retruns a value from within range based on percentage passed in


      :param arg2: 

      :type arg2: float

      :rtype: :class:`Vector`

   .. method:: getRandom( )

      Returns a random value within range


      :rtype: :class:`Vector`

   .. attribute:: end

       |      Returns maximum value in range


   .. attribute:: max

       |      Returns maximum value in range


   .. attribute:: min

       |      Returns minimum value in range


   .. attribute:: start

       |      Returns minimum value in range


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

      A printable representation of this object.


      :rtype: str

   .. method:: adjust( x, y, width, height)

      Move by x,y then resize to width and height


      :param x:  Value to be added x coordinate


      :type x: float

      :param y:  Change in y coordinate


      :type y: float

      :param width:  Value to be added to width


      :type width: float

      :param height:  Value to be added to height


      :type height: float

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkRect`


      :rtype: object

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelRect`


      :rtype: :class:`Rect`

   .. method:: asRect( )

      Create a copy of this as a :class:`Rect`


      :rtype: :class:`Rect`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionRect`


      :rtype: object

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentRect`


      :rtype: object

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileRect`


      :rtype: object

   .. method:: asTile( )

      Create a copy of this as a :class:`TileRect`


      :rtype: object

   .. method:: contains( x, y[, loopWidth=0])

      Return true if x,y are within this rectangle false otherwise


      :param x:  x position to check


      :type x: float

      :param y:  y position to check


      :type y: float

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: float

      :rtype: bool

   .. method:: contains( position[, loopWidth=0])

      Return true if positiion is within this rectangle false otherwise


      :param position:  x,y coordinates to check


      :type position: :class:`Vector`

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: float

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise


      :param rect:  Rectangle to check against


      :type rect: :class:`Rect`

      :param loopWidth:   How far to check on the x axis from rect.x


      :type loopWidth: float

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise.  Saves overlapping coordinates to parameter intersection 


      :param rect:  Rectangle to check against


      :type rect: :class:`Rect`

      :param intersection:  overlapping coordinates are stored here


      :type intersection: :class:`Rect`

      :param loopWidth:  How far to check on the x axis from rect.x


      :type loopWidth: float

      :rtype: bool

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: float

      :param y:  Change in y coordinate


      :type y: float

   .. method:: move( position)

      Adds position to x,y coordinates


      :param position:  Value to be added to x,y coordinates


      :type position: :class:`Vector`

   .. method:: resize( width, height)

      Expands width and height


      :param width:  Value to be added to width


      :type width: float

      :param height:  Value to be added to height


      :type height: float

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfRect`


      :rtype: :class:`sfRect`

   .. staticmethod:: fromCenter( center, size)

      Create a new Rectangle from the center point.


      :param center: 

      :type center: :class:`Vector`

      :param size: 

      :type size: :class:`Vector`

      :rtype: :class:`Rect`

   .. attribute:: bottom

       |      y + height


   .. attribute:: bottomLeft

       |      (:class:`Vector`) Bottom Left x,y coordinates.


   .. attribute:: bottomRight

       |      (:class:`Vector`) Bottom Right x,y coordinates.


   .. attribute:: center

       |      (:class:`Vector`) Center coordinates of Rectangle.


   .. attribute:: height

       |      Size from y to bottom.


   .. attribute:: left

       |      x coordinate


   .. attribute:: position

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: right

       |      x + width


   .. attribute:: size

       |      width * height


   .. attribute:: top

       |      y coordinate


   .. attribute:: topLeft

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: topRight

       |      (:class:`Vector`) Top Right x,y coordinates.


   .. attribute:: width

       |      Size from x to right.


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


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

      A printable representation of this object.


      :rtype: str

   .. method:: adjust( x, y, width, height)

      Move by x,y then resize to width and height


      :param x:  Value to be added x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkRect`


      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelRect`


      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      Create a copy of this as a :class:`Rect`


      :rtype: :class:`Rect`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionRect`


      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentRect`


      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileRect`


      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileRect`


      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0])

      Return true if x,y are within this rectangle false otherwise


      :param x:  x position to check


      :type x: int

      :param y:  y position to check


      :type y: int

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0])

      Return true if positiion is within this rectangle false otherwise


      :param position:  x,y coordinates to check


      :type position: :class:`RegionVector`

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise


      :param rect:  Rectangle to check against


      :type rect: :class:`RegionRect`

      :param loopWidth:   How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise.  Saves overlapping coordinates to parameter intersection 


      :param rect:  Rectangle to check against


      :type rect: :class:`RegionRect`

      :param intersection:  overlapping coordinates are stored here


      :type intersection: :class:`RegionRect`

      :param loopWidth:  How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: move( position)

      Adds position to x,y coordinates


      :param position:  Value to be added to x,y coordinates


      :type position: :class:`RegionVector`

   .. method:: resize( width, height)

      Expands width and height


      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfRect`


      :rtype: :class:`sfIntRect`

   .. staticmethod:: fromCenter( center, size)

      Create a new Rectangle from the center point.


      :param center: 

      :type center: :class:`RegionVector`

      :param size: 

      :type size: :class:`RegionVector`

      :rtype: :class:`RegionRect`

   .. attribute:: bottom

       |      y + height


   .. attribute:: bottomLeft

       |      (:class:`Vector`) Bottom Left x,y coordinates.


   .. attribute:: bottomRight

       |      (:class:`Vector`) Bottom Right x,y coordinates.


   .. attribute:: center

       |      (:class:`Vector`) Center coordinates of Rectangle.


   .. attribute:: height

       |      Size from y to bottom.


   .. attribute:: left

       |      x coordinate


   .. attribute:: position

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: right

       |      x + width


   .. attribute:: size

       |      width * height


   .. attribute:: top

       |      y coordinate


   .. attribute:: topLeft

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: topRight

       |      (:class:`Vector`) Top Right x,y coordinates.


   .. attribute:: width

       |      Size from x to right.


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


RegionVector
-----------------------------------
.. class:: RegionVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __cmp__( vector)

      Compares this to another vector


      :param vector:  The vector to compare against


      :type vector: :class:`RegionVector`

      :returns: 0 if vectors are the same, -1 if arg is greater, 1 if arg is less than


      :rtype: int

   .. method:: __div__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`RegionVector`

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

   .. method:: __init__( x, y, loopWidth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position, loopWidth)

      

      :param position: 

      :type position: :class:`sfTileVector`

      :param loopWidth: 

      :type loopWidth: int

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

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`RegionVector`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`RegionVector`

      :rtype: object

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkVector`


      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelVector`


      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionVector`


      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentVector`


      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileVector`


      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileVector`


      :rtype: :class:`TileVector`

   .. method:: asVector( )

      Create a copy of this as a vector


      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True])

      Return the angle or direction of this vector


      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]])

      Return the angle or direction of position


      :param position:  The vector to convert


      :type position: :class:`RegionVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0])

      Returns a unit vector in the direction of position


      :param position:  The :class:`Vector` to calculate direction from


      :type position: :class:`RegionVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0])

      Returns direction towards x


      :param x:  X coordinate for direction calculation


      :type x: int

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0])

      Returns direction towards y


      :param y:  Y coordinate for direction calculation


      :type y: int

      :param loopWidth:  Currently has no effect


      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0])

      Returns the distance from position


      :param position:  The :class:`Vector` to calculate distance from


      :type position: :class:`RegionVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: float

   .. method:: isDefault( )

      Returns true if x==0 and y==0, false otherwise


      :rtype: bool

   .. method:: loop( loopWidth)

      Adds loopWidth to x if x < 0.  Subtracts loopWidth from x if x >= loopWidth


      :param loopWidth:  Amount to adjust x coordinate


      :type loopWidth: int

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: shouldLoop( loopWidth)

      Returns True if x < 0 or x >= loopWidth


      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: bool

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfTileVector`


      :rtype: :class:`sfTileVector`

   .. attribute:: height

       |      y coordinate


   .. attribute:: width

       |      x coordinate


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


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

      A printable representation of this object.


      :rtype: str

   .. method:: adjust( x, y, width, height)

      Move by x,y then resize to width and height


      :param x:  Value to be added x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkRect`


      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelRect`


      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      Create a copy of this as a :class:`Rect`


      :rtype: :class:`Rect`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionRect`


      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentRect`


      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileRect`


      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileRect`


      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0])

      Return true if x,y are within this rectangle false otherwise


      :param x:  x position to check


      :type x: int

      :param y:  y position to check


      :type y: int

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0])

      Return true if positiion is within this rectangle false otherwise


      :param position:  x,y coordinates to check


      :type position: :class:`SegmentVector`

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise


      :param rect:  Rectangle to check against


      :type rect: :class:`SegmentRect`

      :param loopWidth:   How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise.  Saves overlapping coordinates to parameter intersection 


      :param rect:  Rectangle to check against


      :type rect: :class:`SegmentRect`

      :param intersection:  overlapping coordinates are stored here


      :type intersection: :class:`SegmentRect`

      :param loopWidth:  How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: move( position)

      Adds position to x,y coordinates


      :param position:  Value to be added to x,y coordinates


      :type position: :class:`SegmentVector`

   .. method:: resize( width, height)

      Expands width and height


      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfRect`


      :rtype: :class:`sfIntRect`

   .. staticmethod:: fromCenter( center, size)

      Create a new Rectangle from the center point.


      :param center: 

      :type center: :class:`SegmentVector`

      :param size: 

      :type size: :class:`SegmentVector`

      :rtype: :class:`SegmentRect`

   .. attribute:: bottom

       |      y + height


   .. attribute:: bottomLeft

       |      (:class:`Vector`) Bottom Left x,y coordinates.


   .. attribute:: bottomRight

       |      (:class:`Vector`) Bottom Right x,y coordinates.


   .. attribute:: center

       |      (:class:`Vector`) Center coordinates of Rectangle.


   .. attribute:: height

       |      Size from y to bottom.


   .. attribute:: left

       |      x coordinate


   .. attribute:: position

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: right

       |      x + width


   .. attribute:: size

       |      width * height


   .. attribute:: top

       |      y coordinate


   .. attribute:: topLeft

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: topRight

       |      (:class:`Vector`) Top Right x,y coordinates.


   .. attribute:: width

       |      Size from x to right.


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


SegmentVector
-----------------------------------
.. class:: SegmentVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __cmp__( vector)

      Compares this to another vector


      :param vector:  The vector to compare against


      :type vector: :class:`SegmentVector`

      :returns: 0 if vectors are the same, -1 if arg is greater, 1 if arg is less than


      :rtype: int

   .. method:: __div__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`SegmentVector`

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

   .. method:: __init__( x, y, loopWidth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position, loopWidth)

      

      :param position: 

      :type position: :class:`sfTileVector`

      :param loopWidth: 

      :type loopWidth: int

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

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`SegmentVector`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SegmentVector`

      :rtype: object

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkVector`


      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelVector`


      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionVector`


      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentVector`


      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileVector`


      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileVector`


      :rtype: :class:`TileVector`

   .. method:: asVector( )

      Create a copy of this as a vector


      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True])

      Return the angle or direction of this vector


      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]])

      Return the angle or direction of position


      :param position:  The vector to convert


      :type position: :class:`SegmentVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0])

      Returns a unit vector in the direction of position


      :param position:  The :class:`Vector` to calculate direction from


      :type position: :class:`SegmentVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0])

      Returns direction towards x


      :param x:  X coordinate for direction calculation


      :type x: int

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0])

      Returns direction towards y


      :param y:  Y coordinate for direction calculation


      :type y: int

      :param loopWidth:  Currently has no effect


      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0])

      Returns the distance from position


      :param position:  The :class:`Vector` to calculate distance from


      :type position: :class:`SegmentVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: float

   .. method:: isDefault( )

      Returns true if x==0 and y==0, false otherwise


      :rtype: bool

   .. method:: loop( loopWidth)

      Adds loopWidth to x if x < 0.  Subtracts loopWidth from x if x >= loopWidth


      :param loopWidth:  Amount to adjust x coordinate


      :type loopWidth: int

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: shouldLoop( loopWidth)

      Returns True if x < 0 or x >= loopWidth


      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: bool

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfTileVector`


      :rtype: :class:`sfTileVector`

   .. attribute:: height

       |      y coordinate


   .. attribute:: width

       |      x coordinate


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


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

      Adds object to spatial hash


      :param obj:  object to store


      :type obj: object

   .. method:: clear( )

      Removes all objects and sections from spatial hash


   .. method:: clearSections( sections)

      Removes specified sections from spatial hash


      :param sections:  List of sections to be removed


      :type sections: :class:`SegmentList`

   .. method:: get( sections)

      Returns a set of objects that are within sections


      :param sections:  List of sections to search


      :type sections: :class:`SegmentList`

      :rtype: object

   .. method:: getAll( )

      Returns all objects in this spatial hash


      :rtype: object

   .. method:: getNearby( area)

      Returns a set of objects that are within area


      :param area:  The size of the area to search


      :type area: :class:`Rect`

      :rtype: object

   .. method:: getSection( point)

      Returns a section that contains point


      :param point:  The x,y coordinates to search for


      :type point: :class:`Vector`

      :rtype: int

   .. method:: getSections( rect)

      Returns a list of sections that contain rect


      :param rect:  Search for this area


      :type rect: :class:`Rect`

      :rtype: :class:`SegmentList`

   .. method:: has( obj)

      Returns true if obj is present in this space, false otherwise


      :param obj:  The object to search for


      :type obj: object

      :rtype: bool

   .. method:: remove( obj)

      Removes object from spatial hash


      :param obj:  this will be removed from spatial hash


      :type obj: object

StringMap
-----------------------------------
.. class:: StringMap

   

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

      A printable representation of this object.


      :rtype: str

   .. method:: adjust( x, y, width, height)

      Move by x,y then resize to width and height


      :param x:  Value to be added x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkRect`


      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelRect`


      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      Create a copy of this as a :class:`Rect`


      :rtype: :class:`Rect`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionRect`


      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentRect`


      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileRect`


      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileRect`


      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0])

      Return true if x,y are within this rectangle false otherwise


      :param x:  x position to check


      :type x: int

      :param y:  y position to check


      :type y: int

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0])

      Return true if positiion is within this rectangle false otherwise


      :param position:  x,y coordinates to check


      :type position: :class:`SubtileVector`

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise


      :param rect:  Rectangle to check against


      :type rect: :class:`SubtileRect`

      :param loopWidth:   How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise.  Saves overlapping coordinates to parameter intersection 


      :param rect:  Rectangle to check against


      :type rect: :class:`SubtileRect`

      :param intersection:  overlapping coordinates are stored here


      :type intersection: :class:`SubtileRect`

      :param loopWidth:  How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: move( position)

      Adds position to x,y coordinates


      :param position:  Value to be added to x,y coordinates


      :type position: :class:`SubtileVector`

   .. method:: resize( width, height)

      Expands width and height


      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfRect`


      :rtype: :class:`sfIntRect`

   .. staticmethod:: fromCenter( center, size)

      Create a new Rectangle from the center point.


      :param center: 

      :type center: :class:`SubtileVector`

      :param size: 

      :type size: :class:`SubtileVector`

      :rtype: :class:`SubtileRect`

   .. attribute:: bottom

       |      y + height


   .. attribute:: bottomLeft

       |      (:class:`Vector`) Bottom Left x,y coordinates.


   .. attribute:: bottomRight

       |      (:class:`Vector`) Bottom Right x,y coordinates.


   .. attribute:: center

       |      (:class:`Vector`) Center coordinates of Rectangle.


   .. attribute:: height

       |      Size from y to bottom.


   .. attribute:: left

       |      x coordinate


   .. attribute:: position

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: right

       |      x + width


   .. attribute:: size

       |      width * height


   .. attribute:: top

       |      y coordinate


   .. attribute:: topLeft

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: topRight

       |      (:class:`Vector`) Top Right x,y coordinates.


   .. attribute:: width

       |      Size from x to right.


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


SubtileVector
-----------------------------------
.. class:: SubtileVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __cmp__( vector)

      Compares this to another vector


      :param vector:  The vector to compare against


      :type vector: :class:`SubtileVector`

      :returns: 0 if vectors are the same, -1 if arg is greater, 1 if arg is less than


      :rtype: int

   .. method:: __div__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`SubtileVector`

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

   .. method:: __init__( x, y, loopWidth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position, loopWidth)

      

      :param position: 

      :type position: :class:`sfTileVector`

      :param loopWidth: 

      :type loopWidth: int

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

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`SubtileVector`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`SubtileVector`

      :rtype: object

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkVector`


      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelVector`


      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionVector`


      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentVector`


      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileVector`


      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileVector`


      :rtype: :class:`TileVector`

   .. method:: asVector( )

      Create a copy of this as a vector


      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True])

      Return the angle or direction of this vector


      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]])

      Return the angle or direction of position


      :param position:  The vector to convert


      :type position: :class:`SubtileVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0])

      Returns a unit vector in the direction of position


      :param position:  The :class:`Vector` to calculate direction from


      :type position: :class:`SubtileVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0])

      Returns direction towards x


      :param x:  X coordinate for direction calculation


      :type x: int

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0])

      Returns direction towards y


      :param y:  Y coordinate for direction calculation


      :type y: int

      :param loopWidth:  Currently has no effect


      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0])

      Returns the distance from position


      :param position:  The :class:`Vector` to calculate distance from


      :type position: :class:`SubtileVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: float

   .. method:: isDefault( )

      Returns true if x==0 and y==0, false otherwise


      :rtype: bool

   .. method:: loop( loopWidth)

      Adds loopWidth to x if x < 0.  Subtracts loopWidth from x if x >= loopWidth


      :param loopWidth:  Amount to adjust x coordinate


      :type loopWidth: int

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: shouldLoop( loopWidth)

      Returns True if x < 0 or x >= loopWidth


      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: bool

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfTileVector`


      :rtype: :class:`sfTileVector`

   .. attribute:: height

       |      y coordinate


   .. attribute:: width

       |      x coordinate


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


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

      A printable representation of this object.


      :rtype: str

   .. method:: adjust( x, y, width, height)

      Move by x,y then resize to width and height


      :param x:  Value to be added x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkRect`


      :rtype: :class:`ChunkRect`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelRect`


      :rtype: :class:`PixelRect`

   .. method:: asRect( )

      Create a copy of this as a :class:`Rect`


      :rtype: :class:`Rect`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionRect`


      :rtype: :class:`RegionRect`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentRect`


      :rtype: :class:`SegmentRect`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileRect`


      :rtype: :class:`SubtileRect`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileRect`


      :rtype: :class:`TileRect`

   .. method:: contains( x, y[, loopWidth=0])

      Return true if x,y are within this rectangle false otherwise


      :param x:  x position to check


      :type x: int

      :param y:  y position to check


      :type y: int

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: contains( position[, loopWidth=0])

      Return true if positiion is within this rectangle false otherwise


      :param position:  x,y coordinates to check


      :type position: :class:`TileVector`

      :param loopWidth:  How far to check on the x axis from param x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise


      :param rect:  Rectangle to check against


      :type rect: :class:`TileRect`

      :param loopWidth:   How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: intersects( rect, intersection[, loopWidth=0])

      Returns true if rect is overlapping this rectangle, false otherwise.  Saves overlapping coordinates to parameter intersection 


      :param rect:  Rectangle to check against


      :type rect: :class:`TileRect`

      :param intersection:  overlapping coordinates are stored here


      :type intersection: :class:`TileRect`

      :param loopWidth:  How far to check on the x axis from rect.x


      :type loopWidth: int

      :rtype: bool

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: move( position)

      Adds position to x,y coordinates


      :param position:  Value to be added to x,y coordinates


      :type position: :class:`TileVector`

   .. method:: resize( width, height)

      Expands width and height


      :param width:  Value to be added to width


      :type width: int

      :param height:  Value to be added to height


      :type height: int

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfRect`


      :rtype: :class:`sfIntRect`

   .. staticmethod:: fromCenter( center, size)

      Create a new Rectangle from the center point.


      :param center: 

      :type center: :class:`TileVector`

      :param size: 

      :type size: :class:`TileVector`

      :rtype: :class:`TileRect`

   .. attribute:: bottom

       |      y + height


   .. attribute:: bottomLeft

       |      (:class:`Vector`) Bottom Left x,y coordinates.


   .. attribute:: bottomRight

       |      (:class:`Vector`) Bottom Right x,y coordinates.


   .. attribute:: center

       |      (:class:`Vector`) Center coordinates of Rectangle.


   .. attribute:: height

       |      Size from y to bottom.


   .. attribute:: left

       |      x coordinate


   .. attribute:: position

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: right

       |      x + width


   .. attribute:: size

       |      width * height


   .. attribute:: top

       |      y coordinate


   .. attribute:: topLeft

       |      (:class:`Vector`) Top Left x,y coordinates.


   .. attribute:: topRight

       |      (:class:`Vector`) Top Right x,y coordinates.


   .. attribute:: width

       |      Size from x to right.


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


TileVector
-----------------------------------
.. class:: TileVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __cmp__( vector)

      Compares this to another vector


      :param vector:  The vector to compare against


      :type vector: :class:`TileVector`

      :returns: 0 if vectors are the same, -1 if arg is greater, 1 if arg is less than


      :rtype: int

   .. method:: __div__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`TileVector`

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

   .. method:: __init__( x, y, loopWidth)

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param loopWidth: 

      :type loopWidth: int

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. method:: __init__( position, loopWidth)

      

      :param position: 

      :type position: :class:`sfTileVector`

      :param loopWidth: 

      :type loopWidth: int

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

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`TileVector`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`TileVector`

      :rtype: object

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkVector`


      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelVector`


      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionVector`


      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentVector`


      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileVector`


      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileVector`


      :rtype: :class:`TileVector`

   .. method:: asVector( )

      Create a copy of this as a vector


      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True])

      Return the angle or direction of this vector


      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]])

      Return the angle or direction of position


      :param position:  The vector to convert


      :type position: :class:`TileVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0])

      Returns a unit vector in the direction of position


      :param position:  The :class:`Vector` to calculate direction from


      :type position: :class:`TileVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0])

      Returns direction towards x


      :param x:  X coordinate for direction calculation


      :type x: int

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0])

      Returns direction towards y


      :param y:  Y coordinate for direction calculation


      :type y: int

      :param loopWidth:  Currently has no effect


      :type loopWidth: int

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0])

      Returns the distance from position


      :param position:  The :class:`Vector` to calculate distance from


      :type position: :class:`TileVector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: float

   .. method:: isDefault( )

      Returns true if x==0 and y==0, false otherwise


      :rtype: bool

   .. method:: loop( loopWidth)

      Adds loopWidth to x if x < 0.  Subtracts loopWidth from x if x >= loopWidth


      :param loopWidth:  Amount to adjust x coordinate


      :type loopWidth: int

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: int

      :param y:  Change in y coordinate


      :type y: int

   .. method:: shouldLoop( loopWidth)

      Returns True if x < 0 or x >= loopWidth


      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: int

      :rtype: bool

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfTileVector`


      :rtype: :class:`sfTileVector`

   .. attribute:: height

       |      y coordinate


   .. attribute:: width

       |      x coordinate


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


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

Time
-----------------------------------
.. class:: Time

   

   .. method:: __init__( )

      

   .. method:: asMicroseconds( )

      

      :rtype: long

   .. method:: asMilliseconds( )

      

      :rtype: int

   .. method:: asSeconds( )

      

      :rtype: float

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

      Returns true if timer has no remaining time left, false otherwise


      :rtype: bool

   .. method:: percentage( )

      Return percentage of remaining time


      :rtype: float

   .. method:: remaining( )

      Returns the remaining time before timer expries


      :rtype: int

   .. method:: reset( [time=0])

      Resets timer to a new amount


      :param time:  :class:`Time` in milliseconds until timer expires


      :type time: int

   .. method:: total( )

      Return original total from last reset


      :rtype: int

   .. method:: update( frameTime)

      Subtracts frameTime from remaining time


      :param frameTime:  The amount of milliseconds to subtract from remaining time


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

      Compares this to another vector


      :param vector:  The vector to compare against


      :type vector: :class:`Vector`

      :returns: 0 if vectors are the same, -1 if arg is greater, 1 if arg is less than


      :rtype: int

   .. method:: __div__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`Vector`

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

   .. method:: __init__( x, y, loopWidth)

      

      :param x: 

      :type x: float

      :param y: 

      :type y: float

      :param loopWidth: 

      :type loopWidth: float

   .. method:: __init__( position)

      

      :param position: 

      :type position: :class:`sfVector`

   .. method:: __init__( position, loopWidth)

      

      :param position: 

      :type position: :class:`sfVector`

      :param loopWidth: 

      :type loopWidth: float

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

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`Vector`

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: __repr__( )

      A printable representation of this object.


      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: object

   .. method:: asChunk( )

      Create a copy of this as a :class:`ChunkVector`


      :rtype: :class:`ChunkVector`

   .. method:: asPixel( )

      Create a copy of this as a :class:`PixelVector`


      :rtype: :class:`PixelVector`

   .. method:: asRegion( )

      Create a copy of this as a :class:`RegionVector`


      :rtype: :class:`RegionVector`

   .. method:: asSegment( )

      Create a copy of this as a :class:`SegmentVector`


      :rtype: :class:`SegmentVector`

   .. method:: asSubtile( )

      Create a copy of this as a :class:`SubtileVector`


      :rtype: :class:`SubtileVector`

   .. method:: asTile( )

      Create a copy of this as a :class:`TileVector`


      :rtype: :class:`TileVector`

   .. method:: asVector( )

      Create a copy of this as a vector


      :rtype: :class:`Vector`

   .. method:: getAngle( [asDegrees=True])

      Return the angle or direction of this vector


      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getAngle( position[, loopWidth=0[, asDegrees=True]])

      Return the angle or direction of position


      :param position:  The vector to convert


      :type position: :class:`Vector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: float

      :param asDegrees:  If this is true return angle in degrees, else return angle in radians


      :type asDegrees: bool

      :rtype: float

   .. method:: getDirection( position[, loopWidth=0])

      Returns a unit vector in the direction of position


      :param position:  The :class:`Vector` to calculate direction from


      :type position: :class:`Vector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: float

      :rtype: :class:`PixelVector`

   .. method:: getDirectionX( x[, loopWidth=0])

      Returns direction towards x


      :param x:  X coordinate for direction calculation


      :type x: float

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: float

      :rtype: int

   .. method:: getDirectionY( y[, loopWidth=0])

      Returns direction towards y


      :param y:  Y coordinate for direction calculation


      :type y: float

      :param loopWidth:  Currently has no effect


      :type loopWidth: float

      :rtype: int

   .. method:: getDistance( position[, loopWidth=0])

      Returns the distance from position


      :param position:  The :class:`Vector` to calculate distance from


      :type position: :class:`Vector`

      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: float

      :rtype: float

   .. method:: isDefault( )

      Returns true if x==0 and y==0, false otherwise


      :rtype: bool

   .. method:: loop( loopWidth)

      Adds loopWidth to x if x < 0.  Subtracts loopWidth from x if x >= loopWidth


      :param loopWidth:  Amount to adjust x coordinate


      :type loopWidth: float

   .. method:: move( x, y)

      Adds arguments to current x,y values


      :param x:  Change in x coordinate


      :type x: float

      :param y:  Change in y coordinate


      :type y: float

   .. method:: shouldLoop( loopWidth)

      Returns True if x < 0 or x >= loopWidth


      :param loopWidth:  X coordinate for wrap around


      :type loopWidth: float

      :rtype: bool

   .. method:: toSfml( )

      Create a copy of this as a :class:`sfTileVector`


      :rtype: :class:`sfVector`

   .. attribute:: height

       |      y coordinate


   .. attribute:: width

       |      x coordinate


   .. attribute:: x

       |      x coordinate


   .. attribute:: y

       |      y coordinate


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

      

Vector3List
-----------------------------------
.. class:: Vector3List

   

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

WeightedRandomGenerator
-----------------------------------
.. class:: WeightedRandomGenerator

   

   .. method:: __call__( [useWorldRandom=False])

      Returns and index to one of the values randomly based on individual weight


      :param useWorldRandom:  if True then use :class:`World:class:`Random``() else use :class:`Random`()


      :type useWorldRandom: bool

      :rtype: int

   .. method:: __call__( start, end[, useWorldRandom=False])

      Restricts value to range of min, max weight. Returns and index to one of the values randomly based on individual weight


      :param start:  minimum value in range


      :type start: int

      :param end:  maximum value in range


      :type end: int

      :param useWorldRandom:  if True then use :class:`World:class:`Random``() else use :class:`Random`()


      :type useWorldRandom: bool

      :rtype: int

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: list

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Uint32List`

   .. method:: findIndex( target)

      Returns the index of the first weight that is greater than target


      :param target:  minimum weight of desired index


      :type target: int

      :rtype: int

   .. method:: hasWeights( )

      Returns true if initialization has occured


      :rtype: bool

   .. method:: setWeights( list)

      Intialize with a list of weights. Then adjust them to account for individual weight based off of total.


      :param list:  individual values to be totalled


      :type list: list

   .. method:: setWeights( list)

      Intialize with a list of weights. Then adjust them to account for individual weight based off of total.


      :param list:  individual values to be totalled


      :type list: :class:`Uint32List`

   .. attribute:: totals

       |      List of individual weights


WorldRandom
-----------------------------------
.. class:: WorldRandom

   

   .. staticmethod:: get( min, max)

      Return random float within min and max


      :param min:  minimum value in range


      :type min: float

      :param max:  maximum value in range


      :type max: float

      :rtype: float

   .. staticmethod:: get( [max=2147483647])

      Returns an integer from 0 to max


      :param max:  maximum value for range


      :type max: int

      :rtype: int

   .. staticmethod:: get( min, max)

      Return random integer within min and max


      :param min:  minimum value in range


      :type min: int

      :param max:  maximum value in range


      :type max: int

      :rtype: int

   .. staticmethod:: get( arg1)

      

      :param arg1: 

      :type arg1: list

      :rtype: object

   .. staticmethod:: getBool( )

      Returns true or false randomly


      :rtype: bool

   .. staticmethod:: getFloat( )

      Returns a random float from 0.0 to 1.0


      :rtype: float

   .. staticmethod:: read( stream)

      read current seed from stream


      :param stream:  where to read from


      :type stream: :class:`DataStream`

   .. staticmethod:: seed( seed)

      Sets the seed for generating numbers


      :param seed:  set seed to this value


      :type seed: int

   .. staticmethod:: write( stream)

      Write current seed to stream


      :param stream:  where to write to


      :type stream: :class:`DataStream`

