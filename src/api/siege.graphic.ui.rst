.. _siege.graphic.ui:

siege.graphic.ui
==================

AwesomiumError
-----------------------------------
.. class:: AwesomiumError

   

   .. data:: kError_BadParameters = siege.graphic.ui.AwesomiumError.kError_BadParam...

   .. data:: kError_ConnectionGone = siege.graphic.ui.AwesomiumError.kError_Connect...

   .. data:: kError_Generic = siege.graphic.ui.AwesomiumError.kError_Generic

   .. data:: kError_None = siege.graphic.ui.AwesomiumError.kError_None

   .. data:: kError_ObjectGone = siege.graphic.ui.AwesomiumError.kError_ObjectGone

   .. data:: kError_TimedOut = siege.graphic.ui.AwesomiumError.kError_TimedOut

   .. data:: kError_WebViewGone = siege.graphic.ui.AwesomiumError.kError_WebViewGon...

JSObjectType
-----------------------------------
.. class:: JSObjectType

   

   .. data:: kJSObjectType_Local = siege.graphic.ui.JSObjectType.kJSObjectType_Loca...

   .. data:: kJSObjectType_Remote = siege.graphic.ui.JSObjectType.kJSObjectType_Rem...

   .. data:: kJSObjectType_RemoteGlobal = siege.graphic.ui.JSObjectType.kJSObjectTy...

GuiManager
-----------------------------------
.. class:: GuiManager

   

   .. method:: createView( name, area])

      

      :param name: 

      :type name: str

      :param area]: 

      :type area]: :class:`PixelRect`

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

   .. method:: handleResize( width, heigth)

      

      :param width: 

      :type width: int

      :param heigth: 

      :type heigth: int

   .. method:: reset( )

      

   .. method:: unfocusView( view)

      

      :param view: 

      :type view: :class:`View`

JSArray
-----------------------------------
.. class:: JSArray

   

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`JSValue`

   .. method:: __getitem__( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`JSValue`

   .. method:: __init__( )

      

   .. method:: at( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`JSValue`

   .. method:: at( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`JSValue`

   .. method:: capacity( )

      

      :rtype: int

   .. method:: clear( )

      

   .. method:: erase( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: insert( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`JSValue`

      :param arg3: 

      :type arg3: int

   .. method:: pop( )

      

   .. method:: push( arg2)

      

      :param arg2: 

      :type arg2: :class:`JSValue`

   .. method:: size( )

      

      :rtype: int

JSObject
-----------------------------------
.. class:: JSObject

   

   .. method:: __init__( )

      

   .. method:: getMethodNames( )

      

      :rtype: :class:`JSArray`

   .. method:: getProperty( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: :class:`JSValue`

   .. method:: getPropertyNames( )

      

      :rtype: :class:`JSArray`

   .. method:: hasMethod( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: hasProperty( arg2)

      

      :param arg2: 

      :type arg2: object

      :rtype: bool

   .. method:: invoke( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: :class:`JSArray`

      :rtype: :class:`JSValue`

   .. method:: lastError( )

      

      :rtype: :class:`AwesomiumError`

   .. method:: setCustomMethod( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: bool

   .. method:: setProperty( arg2, arg3)

      

      :param arg2: 

      :type arg2: object

      :param arg3: 

      :type arg3: :class:`JSValue`

   .. method:: toString( )

      

      :rtype: object

   .. method:: type( )

      

      :rtype: :class:`JSObjectType`

JSValue
-----------------------------------
.. class:: JSValue

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`JSObject`

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`JSArray`

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: :class:`JSValue`

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: object

   .. method:: isArray( )

      

      :rtype: bool

   .. method:: isBoolean( )

      

      :rtype: bool

   .. method:: isDouble( )

      

      :rtype: bool

   .. method:: isInteger( )

      

      :rtype: bool

   .. method:: isNull( )

      

      :rtype: bool

   .. method:: isNumber( )

      

      :rtype: bool

   .. method:: isObject( )

      

      :rtype: bool

   .. method:: isString( )

      

      :rtype: bool

   .. method:: isUndefined( )

      

      :rtype: bool

   .. method:: toArray( )

      

      :rtype: :class:`JSArray`

   .. method:: toArray( )

      

      :rtype: :class:`JSArray`

   .. method:: toBoolean( )

      

      :rtype: bool

   .. method:: toDouble( )

      

      :rtype: float

   .. method:: toInteger( )

      

      :rtype: int

   .. method:: toObject( )

      

      :rtype: :class:`JSObject`

   .. method:: toObject( )

      

      :rtype: :class:`JSObject`

   .. method:: toString( )

      

      :rtype: object

   .. staticmethod:: null( )

      

      :rtype: :class:`JSValue`

   .. staticmethod:: undefined( )

      

      :rtype: :class:`JSValue`

View
-----------------------------------
.. class:: View

   

   .. method:: chooseFiles( files, writeFiles)

      

      :param files: 

      :type files: list

      :param writeFiles: 

      :type writeFiles: bool

   .. method:: clearCallbacks( )

      

   .. method:: contains( x, y, ignoreTransparent])

      

      :param x: 

      :type x: int

      :param y: 

      :type y: int

      :param ignoreTransparent]: 

      :type ignoreTransparent]: bool

      :rtype: bool

   .. method:: execute( script[, xpathFrame=''])

      

      :param script: 

      :type script: str

      :param xpathFrame: 

      :type xpathFrame: str

   .. method:: execute( commands[, xpathFrame=''])

      

      :param commands: 

      :type commands: list

      :param xpathFrame: 

      :type xpathFrame: str

   .. method:: executeResult( script[, xpathFrame=''])

      

      :param script: 

      :type script: str

      :param xpathFrame: 

      :type xpathFrame: str

      :rtype: :class:`JSValue`

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

   .. method:: register( methodName, callback, hasReturn])

      

      :param methodName: 

      :type methodName: str

      :param callback: 

      :type callback: object

      :param hasReturn]: 

      :type hasReturn]: bool

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

      

   .. attribute:: name

      

   .. attribute:: onHide

      

   .. attribute:: onRender

      

   .. attribute:: onShow

      

