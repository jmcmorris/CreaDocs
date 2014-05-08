.. _siege.sfml:

siege.sfml
==================

BlendMode
-----------------------------------
.. class:: BlendMode

   

   .. data:: BlendAdd = siege.sfml.BlendMode.BlendAdd

   .. data:: BlendAlpha = siege.sfml.BlendMode.BlendAlpha

   .. data:: BlendMultiply = siege.sfml.BlendMode.BlendMultiply

   .. data:: BlendNone = siege.sfml.BlendMode.BlendNone

PrimitiveType
-----------------------------------
.. class:: PrimitiveType

   

   .. data:: Lines = siege.sfml.PrimitiveType.Lines

   .. data:: LinesStrip = siege.sfml.PrimitiveType.LinesStrip

   .. data:: Points = siege.sfml.PrimitiveType.Points

   .. data:: Quads = siege.sfml.PrimitiveType.Quads

   .. data:: Triangles = siege.sfml.PrimitiveType.Triangles

   .. data:: TrianglesFan = siege.sfml.PrimitiveType.TrianglesFan

   .. data:: TrianglesStrip = siege.sfml.PrimitiveType.TrianglesStrip

Drawable
-----------------------------------
.. class:: Drawable

   

   .. method:: draw( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`sfRenderTarget`

      :param arg3: 

      :type arg3: :class:`RenderStates`

   .. method:: draw( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`sfRenderTarget`

      :param arg3: 

      :type arg3: :class:`RenderStates`

VertexArray
-----------------------------------
.. class:: VertexArray

   

   .. method:: __init__( )

      

   .. method:: __init__( type[, vertexCount=0])

      

      :param type: 

      :type type: :class:`PrimitiveType`

      :param vertexCount: 

      :type vertexCount: int

   .. method:: append( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vertex`

   .. method:: clear( )

      

   .. method:: getBounds( )

      

      :rtype: :class:`sfRect`

   .. method:: getPrimitiveType( )

      

      :rtype: :class:`PrimitiveType`

   .. method:: getVertexCount( )

      

      :rtype: int

   .. method:: resize( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: setPrimitiveType( arg2)

      

      :param arg2: 

      :type arg2: :class:`PrimitiveType`

RenderStates
-----------------------------------
.. class:: RenderStates

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`BlendMode`

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Transform`

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTexture`

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Shader`

   .. method:: __init__( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: :class:`BlendMode`

      :param arg3: 

      :type arg3: :class:`Transform`

      :param arg4: 

      :type arg4: :class:`sfTexture`

      :param arg5: 

      :type arg5: :class:`Shader`

   .. attribute:: blendMode

      

   .. attribute:: shader

      

   .. attribute:: texture

      

   .. attribute:: transform

      

Shader
-----------------------------------
.. class:: Shader

   

   .. method:: __init__( )

      

   .. method:: isAvailable( )

      

      :rtype: bool

   .. method:: loadFromFile( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

      :rtype: bool

   .. method:: loadFromFile( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: str

      :rtype: bool

   .. method:: loadFromMemory( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

      :rtype: bool

   .. method:: loadFromMemory( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: str

      :rtype: bool

   .. method:: setParameter( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: float

   .. method:: setParameter( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: float

      :param arg4: 

      :type arg4: float

   .. method:: setParameter( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: float

      :param arg4: 

      :type arg4: float

      :param arg5: 

      :type arg5: float

   .. method:: setParameter( arg2, arg3, arg4, arg5, arg6)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: float

      :param arg4: 

      :type arg4: float

      :param arg5: 

      :type arg5: float

      :param arg6: 

      :type arg6: float

   .. method:: setParameter( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`sfVector`

   .. method:: setParameter( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`sfVector3f`

   .. method:: setParameter( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`Color`

   .. method:: setParameter( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`Transform`

   .. method:: setParameter( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`sfTexture`

SoundBuffer
-----------------------------------
.. class:: SoundBuffer

   

   .. method:: __init__( )

      

   .. method:: loadFromFile( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

SoundSource
-----------------------------------
.. class:: SoundSource

   

   .. method:: getAttenuation( )

      

      :rtype: float

   .. method:: getMinDistance( )

      

      :rtype: float

   .. method:: getPitch( )

      

      :rtype: float

   .. method:: getVolume( )

      

      :rtype: float

   .. method:: isRelativeToListener( )

      

      :rtype: bool

   .. method:: setAttenuation( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: setMinDistance( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: setPitch( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: setRelativeToListener( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: setVolume( arg2)

      

      :param arg2: 

      :type arg2: float

Music
-----------------------------------
.. class:: Music

   

   .. method:: __init__( )

      

   .. method:: getDuration( )

      

      :rtype: :class:`Time`

   .. method:: getLoop( )

      

      :rtype: bool

   .. method:: getPlayingOffset( )

      

      :rtype: :class:`Time`

   .. method:: getSampleRate( )

      

      :rtype: int

   .. method:: getStatus( )

      

      :rtype: :class:`SoundStatus`

   .. method:: openFromFile( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: pause( )

      

   .. method:: play( )

      

   .. method:: setLoop( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: setPlayingOffset( arg2)

      

      :param arg2: 

      :type arg2: :class:`Time`

   .. method:: stop( )

      

Sound
-----------------------------------
.. class:: Sound

   

   .. method:: __init__( )

      

   .. method:: getLoop( )

      

      :rtype: bool

   .. method:: getPlayingOffset( )

      

      :rtype: :class:`Time`

   .. method:: getStatus( )

      

      :rtype: :class:`SoundStatus`

   .. method:: pause( )

      

   .. method:: play( )

      

   .. method:: setBuffer( arg2)

      

      :param arg2: 

      :type arg2: :class:`SoundBuffer`

   .. method:: setLoop( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: stop( )

      

Transform
-----------------------------------
.. class:: Transform

   

   .. method:: __init__( )

      

   .. method:: combine( arg2)

      

      :param arg2: 

      :type arg2: :class:`Transform`

      :rtype: :class:`Transform`

   .. method:: getInverse( )

      

      :rtype: :class:`Transform`

   .. method:: rotate( arg2)

      

      :param arg2: 

      :type arg2: float

      :rtype: :class:`Transform`

   .. method:: rotate( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :param arg4: 

      :type arg4: float

      :rtype: :class:`Transform`

   .. method:: rotate( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: :class:`sfVector`

      :rtype: :class:`Transform`

   .. method:: scale( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :rtype: :class:`Transform`

   .. method:: scale( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :param arg4: 

      :type arg4: float

      :param arg5: 

      :type arg5: float

      :rtype: :class:`Transform`

   .. method:: scale( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: :class:`Transform`

   .. method:: scale( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :param arg3: 

      :type arg3: :class:`sfVector`

      :rtype: :class:`Transform`

   .. method:: transformPoint( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :rtype: :class:`sfVector`

   .. method:: transformPoint( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: :class:`sfVector`

   .. method:: transformRect( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfRect`

      :rtype: :class:`sfRect`

   .. method:: translate( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :rtype: :class:`Transform`

   .. method:: translate( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: :class:`Transform`

Transformable
-----------------------------------
.. class:: Transformable

   

   .. method:: __init__( )

      

   .. method:: getInverseTransform( )

      

      :rtype: :class:`Transform`

   .. method:: getOrigin( )

      

      :rtype: :class:`sfVector`

   .. method:: getPosition( )

      

      :rtype: :class:`sfVector`

   .. method:: getRotation( )

      

      :rtype: float

   .. method:: getScale( )

      

      :rtype: :class:`sfVector`

   .. method:: getTransform( )

      

      :rtype: :class:`Transform`

   .. method:: move( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: move( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

   .. method:: rotate( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: scale( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: scale( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

   .. method:: setOrigin( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: setOrigin( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

   .. method:: setPosition( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: setPosition( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

   .. method:: setRotation( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: setScale( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: setScale( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

Shape(Transformable, Drawable)
-----------------------------------
.. class:: Shape(Transformable, Drawable)

   

RectangleShape
-----------------------------------
.. class:: RectangleShape

   

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

   .. method:: getSize( )

      

      :rtype: :class:`sfVector`

   .. method:: setSize( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

Sprite(Transformable, Drawable)
-----------------------------------
.. class:: Sprite(Transformable, Drawable)

   

Vertex
-----------------------------------
.. class:: Vertex

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :param arg3: 

      :type arg3: :class:`Color`

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :param arg3: 

      :type arg3: :class:`sfVector`

   .. method:: __init__( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :param arg3: 

      :type arg3: :class:`Color`

      :param arg4: 

      :type arg4: :class:`sfVector`

   .. attribute:: color

      

   .. attribute:: position

      

   .. attribute:: texCoords

      

sfEvent
-----------------------------------
.. class:: sfEvent

   

   .. method:: __init__( )

      

   .. attribute:: joystickButton

      

   .. attribute:: joystickConnect

      

   .. attribute:: joystickMove

      

   .. attribute:: key

      

   .. attribute:: mouseButton

      

   .. attribute:: mouseMove

      

   .. attribute:: mouseWheel

      

   .. attribute:: size

      

   .. attribute:: text

      

   .. attribute:: type

      

   .. data:: Closed = siege.sfml.EventType.Closed

   .. data:: Count = siege.sfml.EventType.Count

   .. data:: EventType = <class 'siege.sfml.EventType'>

   .. data:: GainedFocus = siege.sfml.EventType.GainedFocus

   .. data:: JoystickButtonEvent = <class 'siege.sfml.JoystickButtonEvent'>

   .. data:: JoystickButtonPressed = siege.sfml.EventType.JoystickButtonPressed

   .. data:: JoystickButtonReleased = siege.sfml.EventType.JoystickButtonReleased

   .. data:: JoystickConnectEvent = <class 'siege.sfml.JoystickConnectEvent'>

   .. data:: JoystickConnected = siege.sfml.EventType.JoystickConnected

   .. data:: JoystickDisconnected = siege.sfml.EventType.JoystickDisconnected

   .. data:: JoystickMoveEvent = <class 'siege.sfml.JoystickMoveEvent'>

   .. data:: JoystickMoved = siege.sfml.EventType.JoystickMoved

   .. data:: KeyEvent = <class 'siege.sfml.KeyEvent'>

   .. data:: KeyPressed = siege.sfml.EventType.KeyPressed

   .. data:: KeyReleased = siege.sfml.EventType.KeyReleased

   .. data:: LostFocus = siege.sfml.EventType.LostFocus

   .. data:: MouseButtonEvent = <class 'siege.sfml.MouseButtonEvent'>

   .. data:: MouseButtonPressed = siege.sfml.EventType.MouseButtonPressed

   .. data:: MouseButtonReleased = siege.sfml.EventType.MouseButtonReleased

   .. data:: MouseEntered = siege.sfml.EventType.MouseEntered

   .. data:: MouseLeft = siege.sfml.EventType.MouseLeft

   .. data:: MouseMoveEvent = <class 'siege.sfml.MouseMoveEvent'>

   .. data:: MouseMoved = siege.sfml.EventType.MouseMoved

   .. data:: MouseWheelEvent = <class 'siege.sfml.MouseWheelEvent'>

   .. data:: MouseWheelMoved = siege.sfml.EventType.MouseWheelMoved

   .. data:: Resized = siege.sfml.EventType.Resized

   .. data:: SizeEvent = <class 'siege.sfml.SizeEvent'>

   .. data:: TextEntered = siege.sfml.EventType.TextEntered

   .. data:: TextEvent = <class 'siege.sfml.TextEvent'>

sfIntRect
-----------------------------------
.. class:: sfIntRect

   

   .. method:: __init__( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :param arg4: 

      :type arg4: int

      :param arg5: 

      :type arg5: int

   .. method:: __init__( )

      

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: contains( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. method:: contains( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTileVector`

      :rtype: bool

   .. method:: intersects( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfIntRect`

      :rtype: bool

   .. method:: intersects( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`sfIntRect`

      :param arg3: 

      :type arg3: :class:`sfIntRect`

      :rtype: bool

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

sfRect
-----------------------------------
.. class:: sfRect

   

   .. method:: __init__( arg2, arg3, arg4, arg5)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :param arg4: 

      :type arg4: float

      :param arg5: 

      :type arg5: float

   .. method:: __init__( )

      

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: contains( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :rtype: bool

   .. method:: contains( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: bool

   .. method:: intersects( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfRect`

      :rtype: bool

   .. method:: intersects( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`sfRect`

      :param arg3: 

      :type arg3: :class:`sfRect`

      :rtype: bool

   .. attribute:: height

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

sfTexture
-----------------------------------
.. class:: sfTexture

   

   .. method:: __init__( )

      

   .. method:: create( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. method:: getSize( )

      

      :rtype: object

   .. method:: loadFromFile( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: :class:`sfIntRect`

      :rtype: bool

   .. method:: loadFromImage( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: :class:`sfIntRect`

      :rtype: bool

   .. method:: loadFromMemory( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: int

      :param arg4: 

      :type arg4: :class:`sfIntRect`

      :rtype: bool

   .. method:: loadFromStream( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: :class:`sfIntRect`

      :rtype: bool

sfTileVector
-----------------------------------
.. class:: sfTileVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTileVector`

      :rtype: object

   .. method:: __cmp__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTileVector`

      :rtype: int

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTileVector`

      :rtype: object

   .. method:: __hash__( )

      

      :rtype: int

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTileVector`

      :rtype: object

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. method:: __init__( )

      

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTileVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfTileVector`

      :rtype: object

   .. attribute:: x

      

   .. attribute:: y

      

sfVector
-----------------------------------
.. class:: sfVector

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: object

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: object

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

   .. method:: __init__( )

      

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: object

   .. method:: __repr__( )

      

      :rtype: str

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector`

      :rtype: object

   .. attribute:: x

      

   .. attribute:: y

      

sfVector3f
-----------------------------------
.. class:: sfVector3f

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector3f`

      :rtype: object

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector3f`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector3f`

      :rtype: object

   .. method:: __init__( arg2, arg3, arg4)

      

      :param arg2: 

      :type arg2: float

      :param arg3: 

      :type arg3: float

      :param arg4: 

      :type arg4: float

   .. method:: __init__( )

      

   .. method:: __isub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector3f`

      :rtype: object

   .. method:: __sub__( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfVector3f`

      :rtype: object

   .. attribute:: x

      

   .. attribute:: y

      

   .. attribute:: z

      

