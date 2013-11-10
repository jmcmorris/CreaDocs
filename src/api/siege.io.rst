.. _siege.io:

siege.io
==================

ActionState
-----------------------------------
.. class:: ActionState

   

   .. method:: __init__( )

      

   .. attribute:: elapsed

      

   .. attribute:: inputs

      

   .. attribute:: isDisabled

      

   .. attribute:: isPressed

      

   .. attribute:: justPressed

      

   .. attribute:: justReleased

      

   .. attribute:: onChange

      

DataStream
-----------------------------------
.. class:: DataStream

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: append( data)

      

      :param data: 

      :type data: :class:`DataStream`

   .. method:: append( data, size)

      

      :param data: 

      :type data: object

      :param size: 

      :type size: int

   .. method:: begin( )

      

   .. method:: clear( )

      

   .. method:: compress( )

      

   .. method:: converge( )

      

   .. method:: decompress( )

      

   .. method:: diverge( )

      

   .. method:: end( )

      

   .. method:: partitionLength( )

      

      :rtype: int

   .. method:: readBool( )

      

      :rtype: bool

   .. method:: readColor( )

      

      :rtype: :class:`Color`

   .. method:: readDouble( )

      

      :rtype: float

   .. method:: readFloat( )

      

      :rtype: float

   .. method:: readInt16( )

      

      :rtype: int

   .. method:: readInt32( )

      

      :rtype: int

   .. method:: readInt8( )

      

      :rtype: int

   .. method:: readPixelRect( )

      

      :rtype: :class:`PixelRect`

   .. method:: readPixelVector( )

      

      :rtype: :class:`PixelVector`

   .. method:: readRect( )

      

      :rtype: :class:`Rect`

   .. method:: readString( )

      

      :rtype: str

   .. method:: readTileRect( )

      

      :rtype: :class:`TileRect`

   .. method:: readTileVector( )

      

      :rtype: :class:`TileVector`

   .. method:: readUint16( )

      

      :rtype: int

   .. method:: readUint32( )

      

      :rtype: int

   .. method:: readUint8( )

      

      :rtype: int

   .. method:: readVector( )

      

      :rtype: :class:`Vector`

   .. method:: readVector3( )

      

      :rtype: :class:`Vector3`

   .. method:: readWString( )

      

      :rtype: unicode

   .. method:: size( )

      

      :rtype: int

   .. method:: skip( )

      

   .. method:: writeBool( data)

      

      :param data: 

      :type data: bool

   .. method:: writeColor( data)

      

      :param data: 

      :type data: :class:`Color`

   .. method:: writeDouble( data)

      

      :param data: 

      :type data: float

   .. method:: writeFloat( data)

      

      :param data: 

      :type data: float

   .. method:: writeInt16( data)

      

      :param data: 

      :type data: int

   .. method:: writeInt32( data)

      

      :param data: 

      :type data: int

   .. method:: writeInt8( data)

      

      :param data: 

      :type data: int

   .. method:: writePixelRect( data)

      

      :param data: 

      :type data: :class:`PixelRect`

   .. method:: writePixelVector( data)

      

      :param data: 

      :type data: :class:`PixelVector`

   .. method:: writeRect( data)

      

      :param data: 

      :type data: :class:`Rect`

   .. method:: writeString( data)

      

      :param data: 

      :type data: str

   .. method:: writeTileRect( data)

      

      :param data: 

      :type data: :class:`TileRect`

   .. method:: writeTileVector( data)

      

      :param data: 

      :type data: :class:`TileVector`

   .. method:: writeUint16( data)

      

      :param data: 

      :type data: int

   .. method:: writeUint32( data)

      

      :param data: 

      :type data: int

   .. method:: writeUint8( data)

      

      :param data: 

      :type data: int

   .. method:: writeVector( data)

      

      :param data: 

      :type data: :class:`Vector`

   .. method:: writeVector3( data)

      

      :param data: 

      :type data: :class:`Vector3`

   .. method:: writeWString( data)

      

      :param data: 

      :type data: unicode

File
-----------------------------------
.. class:: File

   

   .. staticmethod:: load( filePath, data)

      

      :param filePath: 

      :type filePath: object

      :param data: 

      :type data: :class:`DataStream`

   .. staticmethod:: open( filePath)

      

      :param filePath: 

      :type filePath: object

      :rtype: :class:`File`

   .. staticmethod:: save( filePath, data)

      

      :param filePath: 

      :type filePath: object

      :param data: 

      :type data: :class:`DataStream`

FileManager
-----------------------------------
.. class:: FileManager

   

   .. method:: asyncRead( filePath, onComplete, isCreaFile)

      

      :param filePath: 

      :type filePath: object

      :param onComplete: 

      :type onComplete: object

      :param isCreaFile: 

      :type isCreaFile: bool

   .. method:: asyncWrite( filePath, stream)

      

      :param filePath: 

      :type filePath: object

      :param stream: 

      :type stream: :class:`DataStream`

GameInput
-----------------------------------
.. class:: GameInput

   

   .. method:: __init__( )

      

   .. method:: update( )

      

   .. attribute:: isPressed

      

JoyInput
-----------------------------------
.. class:: JoyInput

   

   .. method:: __init__( joyId, joyButton)

      

      :param joyId: 

      :type joyId: int

      :param joyButton: 

      :type joyButton: int

   .. attribute:: axis

      

   .. attribute:: button

      

   .. attribute:: delta

      

   .. attribute:: id

      

   .. attribute:: useAxis

      

   .. attribute:: useButton

      

KeyInput
-----------------------------------
.. class:: KeyInput

   

   .. method:: __init__( key)

      

      :param key: 

      :type key: Key

   .. attribute:: key

      

MouseInput
-----------------------------------
.. class:: MouseInput

   

   .. method:: __init__( button)

      

      :param button: 

      :type button: Button

   .. attribute:: button

      

GameInputList
-----------------------------------
.. class:: GameInputList

   

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

Input
-----------------------------------
.. class:: Input

   

   .. method:: __init__( )

      

   .. method:: createAction( )

      

      :rtype: :class:`ActionState`

   .. method:: removeAction( actionState)

      

      :param actionState: 

      :type actionState: :class:`ActionState`

   .. method:: update( frameTime)

      

      :param frameTime: 

      :type frameTime: int

   .. attribute:: actions

      

Joystick
-----------------------------------
.. class:: Joystick

   

   .. method:: __init__( )

      

   .. staticmethod:: getAxisPosition( joystick, axis)

      

      :param joystick: 

      :type joystick: int

      :param axis: 

      :type axis: Axis

      :rtype: float

   .. staticmethod:: getButtonCount( joystick)

      

      :param joystick: 

      :type joystick: int

      :rtype: int

   .. staticmethod:: hasAxis( joystick, axis)

      

      :param joystick: 

      :type joystick: int

      :param axis: 

      :type axis: Axis

      :rtype: bool

   .. staticmethod:: isButtonPressed( joystick, button)

      

      :param joystick: 

      :type joystick: int

      :param button: 

      :type button: int

      :rtype: bool

   .. staticmethod:: isConnected( joystick)

      

      :param joystick: 

      :type joystick: int

      :rtype: bool

   .. staticmethod:: update( )

      

   .. data:: Axis = <class 'siege.io.Axis'>

   .. data:: AxisCount = 8

   .. data:: ButtonCount = 32

   .. data:: Count = 8

   .. data:: PovX = siege.io.Axis.PovX

   .. data:: PovY = siege.io.Axis.PovY

   .. data:: R = siege.io.Axis.R

   .. data:: U = siege.io.Axis.U

   .. data:: V = siege.io.Axis.V

   .. data:: X = siege.io.Axis.X

   .. data:: Y = siege.io.Axis.Y

   .. data:: Z = siege.io.Axis.Z

Keyboard
-----------------------------------
.. class:: Keyboard

   

   .. method:: __init__( )

      

   .. staticmethod:: isKeyPressed( key)

      

      :param key: 

      :type key: Key

      :rtype: bool

   .. data:: A = siege.io.Key.A

   .. data:: Add = siege.io.Key.Add

   .. data:: B = siege.io.Key.B

   .. data:: BackSlash = siege.io.Key.BackSlash

   .. data:: BackSpace = siege.io.Key.BackSpace

   .. data:: C = siege.io.Key.C

   .. data:: Comma = siege.io.Key.Comma

   .. data:: D = siege.io.Key.D

   .. data:: Dash = siege.io.Key.Dash

   .. data:: Delete = siege.io.Key.Delete

   .. data:: Divide = siege.io.Key.Divide

   .. data:: Down = siege.io.Key.Down

   .. data:: E = siege.io.Key.E

   .. data:: End = siege.io.Key.End

   .. data:: Equal = siege.io.Key.Equal

   .. data:: Escape = siege.io.Key.Escape

   .. data:: F = siege.io.Key.F

   .. data:: F1 = siege.io.Key.F1

   .. data:: F10 = siege.io.Key.F10

   .. data:: F11 = siege.io.Key.F11

   .. data:: F12 = siege.io.Key.F12

   .. data:: F13 = siege.io.Key.F13

   .. data:: F14 = siege.io.Key.F14

   .. data:: F15 = siege.io.Key.F15

   .. data:: F2 = siege.io.Key.F2

   .. data:: F3 = siege.io.Key.F3

   .. data:: F4 = siege.io.Key.F4

   .. data:: F5 = siege.io.Key.F5

   .. data:: F6 = siege.io.Key.F6

   .. data:: F7 = siege.io.Key.F7

   .. data:: F8 = siege.io.Key.F8

   .. data:: F9 = siege.io.Key.F9

   .. data:: G = siege.io.Key.G

   .. data:: H = siege.io.Key.H

   .. data:: Home = siege.io.Key.Home

   .. data:: I = siege.io.Key.I

   .. data:: Insert = siege.io.Key.Insert

   .. data:: J = siege.io.Key.J

   .. data:: K = siege.io.Key.K

   .. data:: Key = <class 'siege.io.Key'>

   .. data:: KeyCount = siege.io.Key.KeyCount

   .. data:: L = siege.io.Key.L

   .. data:: LAlt = siege.io.Key.LAlt

   .. data:: LBracket = siege.io.Key.LBracket

   .. data:: LControl = siege.io.Key.LControl

   .. data:: LShift = siege.io.Key.LShift

   .. data:: LSystem = siege.io.Key.LSystem

   .. data:: Left = siege.io.Key.Left

   .. data:: M = siege.io.Key.M

   .. data:: Menu = siege.io.Key.Menu

   .. data:: Multiply = siege.io.Key.Multiply

   .. data:: N = siege.io.Key.N

   .. data:: Num0 = siege.io.Key.Num0

   .. data:: Num1 = siege.io.Key.Num1

   .. data:: Num2 = siege.io.Key.Num2

   .. data:: Num3 = siege.io.Key.Num3

   .. data:: Num4 = siege.io.Key.Num4

   .. data:: Num5 = siege.io.Key.Num5

   .. data:: Num6 = siege.io.Key.Num6

   .. data:: Num7 = siege.io.Key.Num7

   .. data:: Num8 = siege.io.Key.Num8

   .. data:: Num9 = siege.io.Key.Num9

   .. data:: Numpad0 = siege.io.Key.Numpad0

   .. data:: Numpad1 = siege.io.Key.Numpad1

   .. data:: Numpad2 = siege.io.Key.Numpad2

   .. data:: Numpad3 = siege.io.Key.Numpad3

   .. data:: Numpad4 = siege.io.Key.Numpad4

   .. data:: Numpad5 = siege.io.Key.Numpad5

   .. data:: Numpad6 = siege.io.Key.Numpad6

   .. data:: Numpad7 = siege.io.Key.Numpad7

   .. data:: Numpad8 = siege.io.Key.Numpad8

   .. data:: Numpad9 = siege.io.Key.Numpad9

   .. data:: O = siege.io.Key.O

   .. data:: P = siege.io.Key.P

   .. data:: PageDown = siege.io.Key.PageDown

   .. data:: PageUp = siege.io.Key.PageUp

   .. data:: Pause = siege.io.Key.Pause

   .. data:: Period = siege.io.Key.Period

   .. data:: Q = siege.io.Key.Q

   .. data:: Quote = siege.io.Key.Quote

   .. data:: R = siege.io.Key.R

   .. data:: RAlt = siege.io.Key.RAlt

   .. data:: RBracket = siege.io.Key.RBracket

   .. data:: RControl = siege.io.Key.RControl

   .. data:: RShift = siege.io.Key.RShift

   .. data:: RSystem = siege.io.Key.RSystem

   .. data:: Return = siege.io.Key.Return

   .. data:: Right = siege.io.Key.Right

   .. data:: S = siege.io.Key.S

   .. data:: SemiColon = siege.io.Key.SemiColon

   .. data:: Slash = siege.io.Key.Slash

   .. data:: Space = siege.io.Key.Space

   .. data:: Subtract = siege.io.Key.Subtract

   .. data:: T = siege.io.Key.T

   .. data:: Tab = siege.io.Key.Tab

   .. data:: Tilde = siege.io.Key.Tilde

   .. data:: U = siege.io.Key.U

   .. data:: Up = siege.io.Key.Up

   .. data:: V = siege.io.Key.V

   .. data:: W = siege.io.Key.W

   .. data:: X = siege.io.Key.X

   .. data:: Y = siege.io.Key.Y

   .. data:: Z = siege.io.Key.Z

Mouse
-----------------------------------
.. class:: Mouse

   

   .. method:: __init__( )

      

   .. staticmethod:: getPosition( )

      

      :rtype: :class:`sfTileVector`

   .. staticmethod:: getPosition( relativeTo)

      

      :param relativeTo: 

      :type relativeTo: object

      :rtype: :class:`sfTileVector`

   .. staticmethod:: isButtonPressed( button)

      

      :param button: 

      :type button: Button

      :rtype: bool

   .. staticmethod:: setPosition( position)

      

      :param position: 

      :type position: :class:`sfTileVector`

   .. staticmethod:: setPosition( position, relativeTo)

      

      :param position: 

      :type position: :class:`sfTileVector`

      :param relativeTo: 

      :type relativeTo: object

   .. data:: Button = <class 'siege.io.Button'>

   .. data:: ButtonCount = siege.io.Button.ButtonCount

   .. data:: Left = siege.io.Button.Left

   .. data:: Middle = siege.io.Button.Middle

   .. data:: Right = siege.io.Button.Right

   .. data:: XButton1 = siege.io.Button.XButton1

   .. data:: XButton2 = siege.io.Button.XButton2

