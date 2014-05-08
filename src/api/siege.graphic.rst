.. _siege.graphic:

siege.graphic
==================

AnimationMap
-----------------------------------
.. class:: AnimationMap

   

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

Color
-----------------------------------
.. class:: Color

   

   .. method:: __add__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :rtype: object

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :rtype: object

   .. method:: __iadd__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :rtype: object

   .. method:: __imul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( [red=0[, green=0[, blue=0[, alpha=255]]]])

      

      :param red: 

      :type red: int

      :param green: 

      :type green: int

      :param blue: 

      :type blue: int

      :param alpha: 

      :type alpha: int

   .. method:: __mul__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`Color`

      :rtype: object

   .. attribute:: a

      

   .. attribute:: b

      

   .. attribute:: g

      

   .. attribute:: r

      

DebugDrawSystem
-----------------------------------
.. class:: DebugDrawSystem

   

   .. method:: add( rect, color)

      

      :param rect: 

      :type rect: :class:`Rect`

      :param color: 

      :type color: :class:`Color`

   .. method:: add( position, radius, color)

      

      :param position: 

      :type position: :class:`Vector`

      :param radius: 

      :type radius: float

      :param color: 

      :type color: :class:`Color`

   .. method:: add( point1, point2, color)

      

      :param point1: 

      :type point1: :class:`Vector`

      :param point2: 

      :type point2: :class:`Vector`

      :param color: 

      :type color: :class:`Color`

   .. attribute:: enabled

      

DrawableText
-----------------------------------
.. class:: DrawableText

   

   .. method:: __init__( )

      

   .. method:: __init__( text, font, size])

      

      :param text: 

      :type text: str

      :param font: 

      :type font: str

      :param size]: 

      :type size]: int

   .. method:: getColor( )

      

      :rtype: :class:`Color`

   .. method:: getGlobalBounds( )

      

      :rtype: :class:`Rect`

   .. method:: getLocalBounds( )

      

      :rtype: :class:`Rect`

   .. method:: getPosition( )

      

      :rtype: :class:`Vector`

   .. method:: getSize( )

      

      :rtype: int

   .. method:: getString( )

      

      :rtype: str

   .. method:: render( target)

      

      :param target: 

      :type target: :class:`sfRenderTarget`

   .. method:: renderOutlined( target, outline)

      

      :param target: 

      :type target: :class:`sfRenderTarget`

      :param outline: 

      :type outline: :class:`Color`

   .. method:: renderShadowed( target, shadow)

      

      :param target: 

      :type target: :class:`sfRenderTarget`

      :param shadow: 

      :type shadow: :class:`Color`

   .. method:: setColor( color)

      

      :param color: 

      :type color: :class:`Color`

   .. method:: setFont( font)

      

      :param font: 

      :type font: str

   .. method:: setPosition( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: setSize( size)

      

      :param size: 

      :type size: int

   .. method:: setString( text)

      

      :param text: 

      :type text: str

   .. attribute:: isVisible

      

Frame
-----------------------------------
.. class:: Frame

   

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

   .. attribute:: delay

      

   .. attribute:: index

      

FrameVector
-----------------------------------
.. class:: FrameVector

   

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

PixelCheck
-----------------------------------
.. class:: PixelCheck

   

   .. staticmethod:: collision( arg1, arg2, arg3)

      

      :param arg1: 

      :type arg1: :class:`RenderComponent`

      :param arg2: 

      :type arg2: :class:`RenderComponent`

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. staticmethod:: collision( arg1, arg2, arg3)

      

      :param arg1: 

      :type arg1: :class:`RenderComponent`

      :param arg2: 

      :type arg2: :class:`ModularRenderSpriteList`

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. staticmethod:: collision( arg1, arg2, arg3)

      

      :param arg1: 

      :type arg1: :class:`ModularRenderSpriteList`

      :param arg2: 

      :type arg2: :class:`ModularRenderSpriteList`

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. staticmethod:: collision( arg1, arg2, arg3, arg4, arg5, arg6, arg7)

      

      :param arg1: 

      :type arg1: Sprite

      :param arg2: 

      :type arg2: Sprite

      :param arg3: 

      :type arg3: :class:`Texture`

      :param arg4: 

      :type arg4: :class:`Texture`

      :param arg5: 

      :type arg5: int

      :param arg6: 

      :type arg6: :class:`Transform`

      :param arg7: 

      :type arg7: :class:`Transform`

      :rtype: bool

   .. staticmethod:: contains( arg1, arg2, arg3)

      

      :param arg1: 

      :type arg1: :class:`RenderComponent`

      :param arg2: 

      :type arg2: :class:`Rect`

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. staticmethod:: contains( arg1, arg2, arg3)

      

      :param arg1: 

      :type arg1: :class:`ModularRenderSpriteList`

      :param arg2: 

      :type arg2: :class:`Rect`

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. staticmethod:: contains( arg1, arg2, arg3, arg4, arg5)

      

      :param arg1: 

      :type arg1: Sprite

      :param arg2: 

      :type arg2: :class:`Texture`

      :param arg3: 

      :type arg3: :class:`Rect`

      :param arg4: 

      :type arg4: int

      :param arg5: 

      :type arg5: :class:`Transform`

      :rtype: bool

Renderable
-----------------------------------
.. class:: Renderable

   

   .. method:: __init__( )

      

   .. method:: getView( )

      

      :rtype: :class:`sfView`

   .. method:: getViewport( )

      

      :rtype: :class:`Rect`

   .. method:: render( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfRenderTarget`

   .. method:: render( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfRenderTarget`

   .. method:: setViewCenter( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

   .. method:: updateView( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Vector`

      :param arg3: 

      :type arg3: float

   .. attribute:: attached

      

   .. attribute:: priority

      

   .. attribute:: scroll

      

   .. attribute:: view

      

SpriteAnimation
-----------------------------------
.. class:: SpriteAnimation

   

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: list

   .. attribute:: delay

      

   .. attribute:: frames

      

   .. attribute:: looped

      

   .. attribute:: name

      

SpriteData
-----------------------------------
.. class:: SpriteData

   

   .. method:: __init__( )

      

   .. method:: addAnimation( arg2)

      

      :param arg2: 

      :type arg2: :class:`SpriteAnimation`

   .. attribute:: animations

      

   .. attribute:: frames

      

SpriteFrame
-----------------------------------
.. class:: SpriteFrame

   

   .. method:: __init__( arg2, arg3, arg4, arg5, arg6])

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :param arg4: 

      :type arg4: int

      :param arg5: 

      :type arg5: int

      :param arg6]: 

      :type arg6]: :class:`Vector`

   .. attribute:: height

      

   .. attribute:: origin

      

   .. attribute:: width

      

   .. attribute:: x

      

   .. attribute:: y

      

Substitution
-----------------------------------
.. class:: Substitution

   

   .. method:: __init__( arg2, arg3, arg4])

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: str

      :param arg4]: 

      :type arg4]: :class:`Vector`

   .. method:: __nonzero__( )

      

      :rtype: bool

   .. method:: isHidden( )

      

      :rtype: bool

   .. attribute:: base

      

   .. attribute:: origin

      

   .. attribute:: replacement

      

SubstitutionMap
-----------------------------------
.. class:: SubstitutionMap

   

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

Texture
-----------------------------------
.. class:: Texture

   

   .. method:: get( )

      

      :rtype: :class:`sfTexture`

   .. method:: getPath( )

      

      :rtype: str

   .. method:: getSize( )

      

      :rtype: :class:`PixelVector`

   .. attribute:: height

      

   .. attribute:: width

      

VideoMode
-----------------------------------
.. class:: VideoMode

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`VideoMode`

      :rtype: object

   .. method:: __ge__( arg2)

      

      :param arg2: 

      :type arg2: :class:`VideoMode`

      :rtype: object

   .. method:: __gt__( arg2)

      

      :param arg2: 

      :type arg2: :class:`VideoMode`

      :rtype: object

   .. method:: __init__( )

      

   .. method:: __init__( width, height[, bitsPerPixel=32])

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

      :param bitsPerPixel: 

      :type bitsPerPixel: int

   .. method:: __le__( arg2)

      

      :param arg2: 

      :type arg2: :class:`VideoMode`

      :rtype: object

   .. method:: __lt__( arg2)

      

      :param arg2: 

      :type arg2: :class:`VideoMode`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`VideoMode`

      :rtype: object

   .. method:: isValid( )

      

      :rtype: bool

   .. staticmethod:: getDesktopMode( )

      

      :rtype: :class:`VideoMode`

   .. staticmethod:: getFullscreenModes( )

      

      :rtype: :class:`VideoModeList`

   .. attribute:: bitsPerPixel

      

   .. attribute:: height

      

   .. attribute:: width

      

VideoModeList
-----------------------------------
.. class:: VideoModeList

   

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

sfRenderTarget
-----------------------------------
.. class:: sfRenderTarget

   

   .. method:: draw( drawable[, states=<siege.sfml.RenderStates)

      

      :param drawable: 

      :type drawable: :class:`Drawable`

      :param states: 

      :type states: :class:`RenderStates`

sfView
-----------------------------------
.. class:: sfView

   

   .. method:: __init__( )

      

   .. method:: getCenter( )

      

      :rtype: :class:`sfVector`

   .. method:: getSize( )

      

      :rtype: :class:`sfVector`

TextureCache
-----------------------------------
.. class:: TextureCache

   

   .. staticmethod:: get( arg1)

      

      :param arg1: 

      :type arg1: object

      :rtype: :class:`Texture`

   .. staticmethod:: getAbsolute( arg1)

      

      :param arg1: 

      :type arg1: object

      :rtype: :class:`Texture`

   .. staticmethod:: instance( )

      

      :rtype: :class:`TextureCache`

