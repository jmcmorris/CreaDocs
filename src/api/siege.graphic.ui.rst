.. _siege.graphic.ui:

siege.graphic.ui
==================

GuiManager
-----------------------------------
.. class:: GuiManager

   

   .. method:: createView( name, area, >[, fullscreen=False]])

      

      :param name: 

      :type name: str

      :param area: 

      :type area: :class:`PixelRect`

      :param >: 

      :type >: eight=0

      :param fullscreen: 

      :type fullscreen: bool

      :rtype: :class:`View`

   .. method:: destroyView( name)

      

      :param name: 

      :type name: str

   .. method:: focusView( name)

      

      :param name: 

      :type name: str

   .. method:: focusView( view)

      

      :param view: 

      :type view: :class:`View`

   .. method:: getFocused( )

      

      :rtype: :class:`View`

   .. method:: getScale( )

      

      :rtype: float

   .. method:: getView( name, area, >[, fullscreen=False]])

      

      :param name: 

      :type name: str

      :param area: 

      :type area: :class:`PixelRect`

      :param >: 

      :type >: eight=0

      :param fullscreen: 

      :type fullscreen: bool

      :rtype: :class:`View`

   .. method:: handleResize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: hasView( name)

      

      :param name: 

      :type name: str

      :rtype: bool

   .. method:: hideAll( )

      

   .. method:: isMousedOver( )

      

      :rtype: bool

   .. method:: setScale( zoom, scale)

      

      :param zoom: 

      :type zoom: float

      :param scale: 

      :type scale: float

   .. method:: unfocusView( view)

      

      :param view: 

      :type view: :class:`View`

   .. attribute:: isReady

      

   .. attribute:: onUiZoom

      

ToolbarUiHelper
-----------------------------------
.. class:: ToolbarUiHelper

   

   .. method:: __init__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`View`

      :param arg3: 

      :type arg3: :class:`Player`

   .. method:: update( )

      

View
-----------------------------------
.. class:: View

   

   .. method:: clearCallbacks( )

      

   .. method:: createImageData( renderSystem, name, width, height)

      

      :param renderSystem: 

      :type renderSystem: :class:`RenderSystem`

      :param name: 

      :type name: str

      :param width: 

      :type width: int

      :param height: 

      :type height: int

      :rtype: bool

   .. method:: execute( script)

      

      :param script: 

      :type script: str

   .. method:: execute( commands)

      

      :param commands: 

      :type commands: list

   .. method:: getPosition( )

      

      :rtype: :class:`Vector`

   .. method:: getSize( )

      

      :rtype: :class:`PixelVector`

   .. method:: handleEvent( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfEvent`

      :rtype: bool

   .. method:: hasFocus( )

      

      :rtype: bool

   .. method:: hasInputFocus( )

      

      :rtype: bool

   .. method:: hide( )

      

   .. method:: isModal( )

      

      :rtype: bool

   .. method:: isVisible( )

      

      :rtype: bool

   .. method:: load( path)

      

      :param path: 

      :type path: object

   .. method:: register( methodName, callback)

      

      :param methodName: 

      :type methodName: str

      :param callback: 

      :type callback: object

   .. method:: reload( ignoreCache)

      

      :param ignoreCache: 

      :type ignoreCache: bool

   .. method:: renderLoopedToImageData( name, render, position, loopWidth[, finalize=True])

      

      :param name: 

      :type name: str

      :param render: 

      :type render: :class:`RenderComponent`

      :param position: 

      :type position: :class:`Vector`

      :param loopWidth: 

      :type loopWidth: int

      :param finalize: 

      :type finalize: bool

   .. method:: renderToImageData( name, render[, finalize=True])

      

      :param name: 

      :type name: str

      :param render: 

      :type render: :class:`RenderComponent`

      :param finalize: 

      :type finalize: bool

   .. method:: resize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: setModal( isModal)

      

      :param isModal: 

      :type isModal: bool

   .. method:: setPosition( position)

      

      :param position: 

      :type position: :class:`Vector`

   .. method:: show( )

      

   .. method:: toggleVisibility( )

      

   .. method:: waitForRefresh( )

      

   .. attribute:: consumeMouseWheel

      

   .. attribute:: debugging

      

   .. attribute:: isLoaded

      

   .. attribute:: isReady

      

   .. attribute:: name

      

   .. attribute:: onHide

      

   .. attribute:: onReady

      

   .. attribute:: onRender

      

   .. attribute:: onShow

      

