.. _siege.graphic.ui:

siege.graphic.ui
==================

GuiManager
-----------------------------------
.. class:: GuiManager

   

   .. method:: createView( name, area, >])

      

      :param name: 

      :type name: str

      :param area: 

      :type area: :class:`PixelRect`

      :param >]: 

      :type >]: eight=0

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

   .. method:: getView( name)

      

      :param name: 

      :type name: str

      :rtype: :class:`View`

   .. method:: handleResize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: reset( )

      

   .. method:: unfocusView( view)

      

      :param view: 

      :type view: :class:`View`

   .. attribute:: isReady

      

View
-----------------------------------
.. class:: View

   

   .. method:: clearCallbacks( )

      

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

      

