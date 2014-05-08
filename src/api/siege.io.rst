.. _siege.io:

siege.io
==================

ActionState
-----------------------------------
.. class:: ActionState

   

   .. method:: __init__( )

      

   .. method:: clear( )

      Clears all added inputs.


   .. attribute:: elapsed

       |      Total time for current state


   .. attribute:: inputs

       |      List of GameInputs for this :class:`ActionState`


   .. attribute:: isDisabled

       |      Set to True to disable this :class:`ActionState` from checking input


   .. attribute:: isPressed

       |      Is True when input has been recieved


   .. attribute:: justPressed

       |      Is True on initial input. False when input is held down.


   .. attribute:: justReleased

       |      Is True on intial input release, False otherwise


   .. attribute:: onChange

       |      :class:`Event` to call on state change


DataStream
-----------------------------------
.. class:: DataStream

   

   .. method:: __init__( )

      

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: append( data)

      Adds data to the end of the buffer


      :param data:  :class:`DataStream` to add on to current buffer


      :type data: :class:`DataStream`

   .. method:: append( data, size)

      Adds size amount of data to the end of current buffer


      :param data:  data to add on to current buffer


      :type data: object

      :param size:  size of the data to add


      :type size: int

   .. method:: begin( )

      Reads a partition header and pushes it onto the stack


   .. method:: clear( )

      Removes all data from the buffer


   .. method:: compress( )

      Compresses the data in the buffer


   .. method:: converge( )

      Exits a partition scope and moves to the outer partition


   .. method:: decompress( )

      Decompresses the data in the buffer


   .. method:: diverge( )

      Creates a partition in the datastream that is prefixed with a size header


   .. method:: end( )

      Used to signal the stream that the current position should be at the end of a partition


   .. method:: partitionLength( )

      Returns length of the top of the partition stack


      :rtype: int

   .. method:: readBool( )

      Ret a boolean from the buffer and returns it


      :rtype: bool

   .. method:: readColor( )

      Read a :class:`Color` from the buffer and returns it


      :rtype: :class:`Color`

   .. method:: readDict( )

      Reads a Python dictionary from the buffer and returns it


      :rtype: dict

   .. method:: readDouble( )

      Read an double from the buffer and returns it


      :rtype: float

   .. method:: readFloat( )

      Read an float from the buffer and returns it


      :rtype: float

   .. method:: readInt16( )

      Read an integer from the buffer and returns it


      :rtype: int

   .. method:: readInt32( )

      Read an integer from the buffer and returns it


      :rtype: int

   .. method:: readInt8( )

      Read an integer from the buffer and returns it


      :rtype: int

   .. method:: readObject( )

      Reads a Python obejct from the buffer and returns it


      :rtype: object

   .. method:: readPixelRect( )

      Read a :class:`PixelRect` from the buffer and returns it


      :rtype: :class:`PixelRect`

   .. method:: readPixelVector( )

      Read a :class:`PixelVector` from the buffer and returns it


      :rtype: :class:`PixelVector`

   .. method:: readRect( )

      Read a :class:`Rect` from the buffer and returns it


      :rtype: :class:`Rect`

   .. method:: readString( )

      Read a string from the buffer and returns it


      :rtype: str

   .. method:: readTileRect( )

      Read a :class:`TileRect` from the buffer and returns it


      :rtype: :class:`TileRect`

   .. method:: readTileVector( )

      Read a :class:`TileVector` from the buffer and returns it


      :rtype: :class:`TileVector`

   .. method:: readUint16( )

      Read an integer from the buffer and returns it


      :rtype: int

   .. method:: readUint32( )

      Read an integer from the buffer and returns it


      :rtype: int

   .. method:: readUint8( )

      Read an integer from the buffer and returns it


      :rtype: int

   .. method:: readVector( )

      Read a :class:`Vector` from the buffer and returns it


      :rtype: :class:`Vector`

   .. method:: readVector3( )

      Read a :class:`Vector3` from the buffer and returns it


      :rtype: :class:`Vector3`

   .. method:: readWString( )

      Read an wide character string from the buffer and returns it


      :rtype: unicode

   .. method:: size( )

      Returns the size of the data in the buffer


      :rtype: int

   .. method:: skip( )

      Skips over the remainder of the current partition


   .. method:: writeBool( data)

      Appends data to the end of the current buffer data


      :param data:  Boolean to write to buffer


      :type data: bool

   .. method:: writeColor( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`Color` to write to buffer


      :type data: :class:`Color`

   .. method:: writeDict( data)

      Appends data to the end of the current buffer data


      :param data:  Python dictionary to write to buffer


      :type data: dict

   .. method:: writeDouble( data)

      Appends data to the end of the current buffer data


      :param data:  Double to write to buffer


      :type data: float

   .. method:: writeFloat( data)

      Appends data to the end of the current buffer data


      :param data:  Float to write to buffer


      :type data: float

   .. method:: writeInt16( data)

      Appends data to the end of the current buffer data


      :param data:  Int16 to write to buffer


      :type data: int

   .. method:: writeInt32( data)

      Appends data to the end of the current buffer data


      :param data:  Int32 to write to buffer


      :type data: int

   .. method:: writeInt8( data)

      Appends data to the end of the current buffer data


      :param data:  Int8 to write to buffer


      :type data: int

   .. method:: writeObject( data)

      Appends data to the end of the current buffer data


      :param data:  Python Object to write to buffer


      :type data: object

   .. method:: writePixelRect( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`PixelRect` to write to buffer


      :type data: :class:`PixelRect`

   .. method:: writePixelVector( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`PixelVector` to write to buffer


      :type data: :class:`PixelVector`

   .. method:: writeRect( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`Rect` to write to buffer


      :type data: :class:`Rect`

   .. method:: writeString( data)

      Appends data to the end of the current buffer data


      :param data:  String to write to buffer


      :type data: str

   .. method:: writeTileRect( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`TileRect` to write to buffer


      :type data: :class:`TileRect`

   .. method:: writeTileVector( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`TileVector` to write to buffer


      :type data: :class:`TileVector`

   .. method:: writeUint16( data)

      Appends data to the end of the current buffer data


      :param data:  Uint16 to write to buffer


      :type data: int

   .. method:: writeUint32( data)

      Appends data to the end of the current buffer data


      :param data:  Uint32 to write to buffer


      :type data: int

   .. method:: writeUint8( data)

      Appends data to the end of the current buffer data


      :param data:  Uint8 to write to buffer


      :type data: int

   .. method:: writeVector( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`Vector` to write to buffer


      :type data: :class:`Vector`

   .. method:: writeVector3( data)

      Appends data to the end of the current buffer data


      :param data:  :class:`Vector3` to write to buffer


      :type data: :class:`Vector3`

   .. method:: writeWString( data)

      Appends data to the end of the current buffer data


      :param data:  Wide String to write to buffer


      :type data: unicode

File
-----------------------------------
.. class:: File

   

   .. staticmethod:: getValidPath( filePath)

      Formats a string to remove invalid characters from a string ([\?\\/:\*<>\|"])


      :param filePath:  Path to the file


      :type filePath: str

      :returns: A formated string


      :rtype: str

   .. staticmethod:: load( filePath, data)

      Appends the file data to the :class:`DataStream`


      :param filePath:  Path to the file


      :type filePath: object

      :param data:  :class:`DataStream` to write to


      :type data: :class:`DataStream`

      :returns: Returns the file version number


      :rtype: int

   .. staticmethod:: open( filePath)

      Opens file at the path and reads into a buffer


      :param filePath:  Path to target file


      :type filePath: object

      :returns: If the file is valid it is returned


      :rtype: :class:`File`

   .. staticmethod:: save( filePath, data)

      Writes contents of data to the file at path


      :param filePath:  Path to file for writing


      :type filePath: object

      :param data:  Data to write to the file


      :type data: :class:`DataStream`

FileManager
-----------------------------------
.. class:: FileManager

   

   .. method:: asyncRead( filePath, onComplete, isCreaFile)

      Reads from a file using a new thread


      :param filePath:  Path to the file


      :type filePath: object

      :param onComplete:  Filer handler for a complete read


      :type onComplete: object

      :param isCreaFile:  Set to true to mark file as a Crea file, false otherwise


      :type isCreaFile: bool

   .. method:: asyncWrite( filePath, stream)

      Writes to a file using a new thread


      :param filePath:  Path to the file


      :type filePath: object

      :param stream:  :class:`DataStream` to write to


      :type stream: :class:`DataStream`

GameInput
-----------------------------------
.. class:: GameInput

   

   .. method:: __init__( )

      

   .. method:: update( )

      Updates each :class:`ActionState` in game


   .. attribute:: isPressed

       |      True if any input was recieved from the user


JoyInput
-----------------------------------
.. class:: JoyInput

   

   .. method:: __init__( joyId, joyButton)

      

      :param joyId: 

      :type joyId: int

      :param joyButton: 

      :type joyButton: int

   .. method:: __init__( joyId, joyAxis, axisDelta)

      

      :param joyId: 

      :type joyId: int

      :param joyAxis: 

      :type joyAxis: Axis

      :param axisDelta: 

      :type axisDelta: float

   .. attribute:: axis

       |      The joystick axis.  See sf::Joystick::Axis


   .. attribute:: button

       |      Which joystick button to use


   .. attribute:: delta

       |      Dead zone for axis input


   .. attribute:: id

       |      Index for this :class:`Joystick`


   .. attribute:: useAxis

       |      Set to True for a joystick axis


   .. attribute:: useButton

       |      Set to True for a joystick button


KeyInput
-----------------------------------
.. class:: KeyInput

   

   .. method:: __init__( key)

      

      :param key: 

      :type key: Key

   .. attribute:: key

       |      Which keyboard key to use


MouseInput
-----------------------------------
.. class:: MouseInput

   

   .. method:: __init__( button)

      

      :param button: 

      :type button: Button

   .. attribute:: button

       |      Which mouse button to use


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

      Returns a new :class:`ActionState`


      :rtype: :class:`ActionState`

   .. method:: removeAction( actionState)

      Removes target :class:`ActionState` from this :class:`Input`


      :param actionState:  The :class:`ActionState` to be removed


      :type actionState: :class:`ActionState`

   .. method:: update( frameTime)

      Updates all ActionStates that this has created


      :param frameTime:  elapsed time for the frame


      :type frameTime: int

   .. attribute:: actions

       |      List of ActionStates


Joystick
-----------------------------------
.. class:: Joystick

   

   .. method:: __init__( )

      

   .. staticmethod:: getAxisPosition( joystick, axis)

      Get the current position of a joystick axis


      :param joystick:  Index of the joystick


      :type joystick: int

      :param axis:  Axis to check


      :type axis: Axis

      :returns: Current position of the axis, in range [-100, 100]


      :rtype: float

   .. staticmethod:: getButtonCount( joystick)

      Return the number of buttons supported by a joystick.


      :param joystick:  Index of the joystick


      :type joystick: int

      :returns: Number of buttons supported by the joystick, or 0 if joystick is not connected


      :rtype: int

   .. staticmethod:: hasAxis( joystick, axis)

      Check if a joystick supports a given axis.


      :param joystick:  Indexof the joystick


      :type joystick: int

      :param axis:  Axis to check


      :type axis: Axis

      :returns: True if the joystick supports the axis, false otherwise


      :rtype: bool

   .. staticmethod:: isButtonPressed( joystick, button)

      Check if a joystick button is pressed. 


      :param joystick:  Index of joystick


      :type joystick: int

      :param button:  Button to check


      :type button: int

      :returns: True if the button is pressed, false otherwise


      :rtype: bool

   .. staticmethod:: isConnected( joystick)

      Check if a joystick is connected. 


      :param joystick:  Index of joystick to check


      :type joystick: int

      :returns: True if the joystick is connected, false otherwise


      :rtype: bool

   .. staticmethod:: update( )

      Update the states of all joysticks.


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

      Check if a key is pressed


      :param key:  The key to check


      :type key: Key

      :returns: True if key pressed, false otherwise


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

      Returns the current position of the mouse in desktop coordinates


      :rtype: :class:`sfTileVector`

   .. staticmethod:: getPosition( relativeTo)

      Get the current position of the mouse in window coordinate


      :param relativeTo:  Reference window


      :type relativeTo: object

      :returns: Current position of the mouse


      :rtype: :class:`sfTileVector`

   .. staticmethod:: isButtonPressed( button)

      Check if a mouse button is pressed


      :param button:  Button to check


      :type button: Button

      :returns: True if the button if pressed, false otherwise


      :rtype: bool

   .. staticmethod:: setPosition( position)

      Set the current position of the mouse in desktop coordinates. 


      :param position:  New position of the mouse


      :type position: :class:`sfTileVector`

   .. staticmethod:: setPosition( position, relativeTo)

      This function sets the current position of the mouse cursor, relative to the given window.


      :param position:  New position of the mouse


      :type position: :class:`sfTileVector`

      :param relativeTo:  Reference window


      :type relativeTo: object

   .. data:: Button = <class 'siege.io.Button'>

   .. data:: ButtonCount = siege.io.Button.ButtonCount

   .. data:: Left = siege.io.Button.Left

   .. data:: Middle = siege.io.Button.Middle

   .. data:: Right = siege.io.Button.Right

   .. data:: XButton1 = siege.io.Button.XButton1

   .. data:: XButton2 = siege.io.Button.XButton2

