.. _siege.network:

siege.network
==================

Message
-----------------------------------
.. class:: Message

   

   .. data:: ACHIEVEMENT_SYSTEM = siege.network.Message.ACHIEVEMENT_SYSTEM

   .. data:: AUDIO_MUSIC = siege.network.Message.AUDIO_MUSIC

   .. data:: AUDIO_SYSTEM = siege.network.Message.AUDIO_SYSTEM

   .. data:: CARTOGRAPHY = siege.network.Message.CARTOGRAPHY

   .. data:: CHANGE_INPUT_STATE = siege.network.Message.CHANGE_INPUT_STATE

   .. data:: CHANGE_TOOL_STATE = siege.network.Message.CHANGE_TOOL_STATE

   .. data:: CHARACTER_CREATE = siege.network.Message.CHARACTER_CREATE

   .. data:: CHARACTER_DESTROY = siege.network.Message.CHARACTER_DESTROY

   .. data:: CHARACTER_GRABBED = siege.network.Message.CHARACTER_GRABBED

   .. data:: CHARACTER_INFO = siege.network.Message.CHARACTER_INFO

   .. data:: CHARACTER_INFO_LIST = siege.network.Message.CHARACTER_INFO_LIST

   .. data:: CHARACTER_INFUSION = siege.network.Message.CHARACTER_INFUSION

   .. data:: CHARACTER_MOVE = siege.network.Message.CHARACTER_MOVE

   .. data:: CHARACTER_SAVE = siege.network.Message.CHARACTER_SAVE

   .. data:: CHAT_PLAYER = siege.network.Message.CHAT_PLAYER

   .. data:: CHAT_SYSTEM = siege.network.Message.CHAT_SYSTEM

   .. data:: COMBAT_ATTACK = siege.network.Message.COMBAT_ATTACK

   .. data:: CONFLICT = siege.network.Message.CONFLICT

   .. data:: CONNECTION_LOST = siege.network.Message.CONNECTION_LOST

   .. data:: CONNECTION_REQUEST_ACCEPTED = siege.network.Message.CONNECTION_REQUEST...

   .. data:: DISCONNECTION_NOTIFICATION = siege.network.Message.DISCONNECTION_NOTIF...

   .. data:: DUNGEONEER = siege.network.Message.DUNGEONEER

   .. data:: DUNGEON_INFO = siege.network.Message.DUNGEON_INFO

   .. data:: ENTITY_RENAME = siege.network.Message.ENTITY_RENAME

   .. data:: GADGET_USE = siege.network.Message.GADGET_USE

   .. data:: HIDE_UI = siege.network.Message.HIDE_UI

   .. data:: INVALID_PASSWORD = siege.network.Message.INVALID_PASSWORD

   .. data:: INVENTORY_CLOSE = siege.network.Message.INVENTORY_CLOSE

   .. data:: INVENTORY_INTERACT = siege.network.Message.INVENTORY_INTERACT

   .. data:: ITEM_CLAIM = siege.network.Message.ITEM_CLAIM

   .. data:: ITEM_CRAFT = siege.network.Message.ITEM_CRAFT

   .. data:: ITEM_DROP = siege.network.Message.ITEM_DROP

   .. data:: ITEM_INTERACT = siege.network.Message.ITEM_INTERACT

   .. data:: ITEM_INVENTORY_EQUIP = siege.network.Message.ITEM_INVENTORY_EQUIP

   .. data:: ITEM_QUICK_SELECT = siege.network.Message.ITEM_QUICK_SELECT

   .. data:: ITEM_RESEARCH = siege.network.Message.ITEM_RESEARCH

   .. data:: ITEM_RETURN_GRAB = siege.network.Message.ITEM_RETURN_GRAB

   .. data:: ITEM_SET_TOOLBAR = siege.network.Message.ITEM_SET_TOOLBAR

   .. data:: ITEM_SPLIT = siege.network.Message.ITEM_SPLIT

   .. data:: ITEM_SWAP_ARMS = siege.network.Message.ITEM_SWAP_ARMS

   .. data:: ITEM_SWAP_WITH_GRAB = siege.network.Message.ITEM_SWAP_WITH_GRAB

   .. data:: ITEM_TRASH = siege.network.Message.ITEM_TRASH

   .. data:: ITEM_UNEQUIP = siege.network.Message.ITEM_UNEQUIP

   .. data:: ITEM_USE = siege.network.Message.ITEM_USE

   .. data:: MERCHANT_CHANGE = siege.network.Message.MERCHANT_CHANGE

   .. data:: NOTIFICATION_SYSTEM = siege.network.Message.NOTIFICATION_SYSTEM

   .. data:: NPC_DISMISS = siege.network.Message.NPC_DISMISS

   .. data:: NPC_INTERACT = siege.network.Message.NPC_INTERACT

   .. data:: PARTICLE_SYSTEM = siege.network.Message.PARTICLE_SYSTEM

   .. data:: PLAYER_ANIMATION = siege.network.Message.PLAYER_ANIMATION

   .. data:: PLAYER_CHANGE_MODE = siege.network.Message.PLAYER_CHANGE_MODE

   .. data:: PLAYER_FORCE = siege.network.Message.PLAYER_FORCE

   .. data:: PLAYER_INPUT = siege.network.Message.PLAYER_INPUT

   .. data:: PLAYER_POSITION = siege.network.Message.PLAYER_POSITION

   .. data:: PLAYER_READY = siege.network.Message.PLAYER_READY

   .. data:: PLAYER_RESERVE = siege.network.Message.PLAYER_RESERVE

   .. data:: PLAYER_RESPAWN = siege.network.Message.PLAYER_RESPAWN

   .. data:: PYTHON_MESSAGE = siege.network.Message.PYTHON_MESSAGE

   .. data:: QUICK_USE = siege.network.Message.QUICK_USE

   .. data:: RESEARCH_DATA = siege.network.Message.RESEARCH_DATA

   .. data:: RESEARCH_INTERACT = siege.network.Message.RESEARCH_INTERACT

   .. data:: RESOLUTION_CHANGED = siege.network.Message.RESOLUTION_CHANGED

   .. data:: SCAVENGER_CHANGE = siege.network.Message.SCAVENGER_CHANGE

   .. data:: SELL_ITEMS = siege.network.Message.SELL_ITEMS

   .. data:: SHOW_COMBAT_NUMBER = siege.network.Message.SHOW_COMBAT_NUMBER

   .. data:: SHOW_UI = siege.network.Message.SHOW_UI

   .. data:: SKILL_USE = siege.network.Message.SKILL_USE

   .. data:: TALENT_PURCHASE_SKILL = siege.network.Message.TALENT_PURCHASE_SKILL

   .. data:: TILE_INFO = siege.network.Message.TILE_INFO

   .. data:: TRAVEL = siege.network.Message.TRAVEL

   .. data:: TRAVEL_ATTUNE = siege.network.Message.TRAVEL_ATTUNE

   .. data:: TRAVEL_SELECT = siege.network.Message.TRAVEL_SELECT

   .. data:: TRAVEL_SHOW_UI = siege.network.Message.TRAVEL_SHOW_UI

   .. data:: VERSION_CHECK = siege.network.Message.VERSION_CHECK

   .. data:: WORLD_INFO = siege.network.Message.WORLD_INFO

PacketPriority
-----------------------------------
.. class:: PacketPriority

   

   .. data:: High = siege.network.PacketPriority.High

   .. data:: Immediate = siege.network.PacketPriority.Immediate

   .. data:: Low = siege.network.PacketPriority.Low

   .. data:: Medium = siege.network.PacketPriority.Medium

PacketReliability
-----------------------------------
.. class:: PacketReliability

   

   .. data:: Reliable = siege.network.PacketReliability.Reliable

   .. data:: ReliableOrdered = siege.network.PacketReliability.ReliableOrdered

   .. data:: ReliableOrderedReceipt = siege.network.PacketReliability.ReliableOrder...

   .. data:: ReliableReceipt = siege.network.PacketReliability.ReliableReceipt

   .. data:: ReliableSequenced = siege.network.PacketReliability.ReliableSequenced

   .. data:: Unreliable = siege.network.PacketReliability.Unreliable

   .. data:: UnreliableReceipt = siege.network.PacketReliability.UnreliableReceipt

   .. data:: UnreliableSequenced = siege.network.PacketReliability.UnreliableSequen...

MessageHandler
-----------------------------------
.. class:: MessageHandler

   

   .. method:: __call__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :param arg3: 

      :type arg3: :class:`DataStream`

   .. staticmethod:: create( [func=None])

      

      :param func: 

      :type func: object

      :rtype: :class:`MessageHandler`

NetworkConnection
-----------------------------------
.. class:: NetworkConnection

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: addMessageCallback( messageId, callback)

      

      :param messageId: 

      :type messageId: str

      :param callback: 

      :type callback: object

   .. method:: broadcast( packet[, channel=0[, reliability=siege.network.PacketReliability.Reliable[, priority=siege.network.PacketPriority.Medium]]])

      Broadcast a message to all available recipients.


      :param packet:  Data to be sent,


      :type packet: :class:`DataStream`

      :param channel:  What channel to send this packet on.


      :type channel: int

      :param reliability:  How reliably to send this data. 


      :type reliability: :class:`PacketReliability`

      :param priority:  What priority level to send with.


      :type priority: :class:`PacketPriority`

      :returns: 0 on bad input. Otherwise a number that identifies this message.


      :rtype: int


   .. method:: getMessageCallback( messageId)

      

      :param messageId: 

      :type messageId: str

      :rtype: object

   .. method:: receive( )

      Handle all queued incoming packets.


   .. method:: register( messageId, callback)

      Register a handler for a specific message.


      :param messageId:  :class:`Message` type to listen for.


      :type messageId: int

      :param callback:  (:class:`MessageHandler`) Handler to be used for processing the message.


      :type callback: :class:`MessageHandler`

   .. method:: send( recipient, packet[, channel=0[, reliability=siege.network.PacketReliability.Reliable[, priority=siege.network.PacketPriority.Medium]]])

      Sends a packet to the recipient.


      :param recipient: 

      :type recipient: :class:`NetworkId`

      :param packet:  Data to be sent,


      :type packet: :class:`DataStream`

      :param channel:  What channel to send this packet on.


      :type channel: int

      :param reliability:  How reliably to send this data. 


      :type reliability: :class:`PacketReliability`

      :param priority:  What priority level to send with.


      :type priority: :class:`PacketPriority`

      :returns: 0 on bad input. Otherwise a number that identifies this message.


      :rtype: int


   .. method:: unregister( messageId)

      Unregister the handler for a message, if present.


      :param messageId: 

      :type messageId:  Message


   .. method:: usingLobby( )

      

      :rtype: bool

Client
-----------------------------------
.. class:: Client

   

   .. method:: joinLobby( lobbyId)

      

      :param lobbyId: 

      :type lobbyId: long

      :rtype: bool

   .. method:: send( packet[, channel=0[, reliability=siege.network.PacketReliability.Reliable[, priority=siege.network.PacketPriority.Medium]]])

      Sends a packet to the server.


      :param packet:  Data to be sent,


      :type packet: :class:`DataStream`

      :param channel:  What channel to send this packet on.


      :type channel: int

      :param reliability:  How reliably to send this data. 


      :type reliability: :class:`PacketReliability`

      :param priority:  What priority level to send with.


      :type priority: :class:`PacketPriority`

      :returns: 0 on bad input. Otherwise a number that identifies this message.


      :rtype: int


Server
-----------------------------------
.. class:: Server

     Provides methods for kicking and banning clients.
  __Banlists are currently only valid for the current instance of the server__
  


   .. method:: ban( arg2)

      Bans a client from the server by ip.


      :param arg2: 

      :type arg2: str

   .. method:: getIp( arg2)

      Retrieves the IP for the client.:param target: (:class:`NetworkId`)


      :param arg2: 

      :type arg2: :class:`NetworkId`

      :rtype: str

   .. method:: hasPassword( )

      Returns if the server is password protected or not.


      :rtype: bool

   .. method:: kick( arg2)

      Kicks a client from the server.


      :param arg2: 

      :type arg2: :class:`NetworkId`

   .. method:: unban( arg2)

      Unbans a client from the server.


      :param arg2: 

      :type arg2: str

   .. attribute:: maxPlayers

      

   .. attribute:: name

      

   .. attribute:: playerCount

      

   .. attribute:: worldName

      

NetworkFriend
-----------------------------------
.. class:: NetworkFriend

   

   .. attribute:: lobby

      

   .. attribute:: name

      

   .. attribute:: usingPassword

      

NetworkFriendList
-----------------------------------
.. class:: NetworkFriendList

   

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

NetworkId
-----------------------------------
.. class:: NetworkId

   

   .. method:: __eq__( arg2)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :rtype: object

   .. method:: __gt__( arg2)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :rtype: object

   .. method:: __init__( arg2)

      

      :param arg2: 

      :type arg2: long

   .. method:: __lt__( arg2)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :rtype: object

   .. method:: __ne__( arg2)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :rtype: object

   .. staticmethod:: toUint32( arg1)

      

      :param arg1: 

      :type arg1: :class:`NetworkId`

      :rtype: int

NetworkManager
-----------------------------------
.. class:: NetworkManager

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: canUseLobby( )

      

      :rtype: bool

   .. method:: clearConnect( )

      

   .. method:: getClient( )

      

      :rtype: :class:`Client`

   .. method:: getFriendHosts( )

      

      :rtype: :class:`NetworkFriendList`

   .. method:: getId( )

      

      :rtype: :class:`NetworkId`

   .. method:: getServer( )

      

      :rtype: :class:`Server`

   .. method:: reset( )

      

   .. method:: setupClient( address, port, password)

      

      :param address: 

      :type address: str

      :param port: 

      :type port: int

      :param password: 

      :type password: str

   .. method:: setupPassthrough( )

      

   .. method:: setupServer( port, password[, hostAddress=''])

      

      :param port: 

      :type port: int

      :param password: 

      :type password: str

      :param hostAddress: 

      :type hostAddress: str

   .. method:: shouldConnect( )

      

      :rtype: bool

   .. method:: update( frameTime)

      

      :param frameTime: 

      :type frameTime: int

   .. staticmethod:: isHost( )

      

      :rtype: bool

   .. staticmethod:: isPassthrough( )

      

      :rtype: bool

   .. staticmethod:: isStandalone( )

      

      :rtype: bool

   .. staticmethod:: setStandalone( standalone)

      

      :param standalone: 

      :type standalone: bool

   .. attribute:: connectHasPassword

      

   .. attribute:: connectLobby

      

   .. attribute:: onReset

      

