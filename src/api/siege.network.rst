.. _siege.network:

siege.network
==================

Message
-----------------------------------
.. class:: Message

   

   .. data:: AUDIO_SYSTEM = siege.network.Message.AUDIO_SYSTEM

   .. data:: CHARACTER_CREATE = siege.network.Message.CHARACTER_CREATE

   .. data:: CHARACTER_DESTROY = siege.network.Message.CHARACTER_DESTROY

   .. data:: CHARACTER_GRABBED = siege.network.Message.CHARACTER_GRABBED

   .. data:: CHARACTER_INFO = siege.network.Message.CHARACTER_INFO

   .. data:: CHARACTER_INFO_LIST = siege.network.Message.CHARACTER_INFO_LIST

   .. data:: CHARACTER_MOVE = siege.network.Message.CHARACTER_MOVE

   .. data:: CHAT_PLAYER = siege.network.Message.CHAT_PLAYER

   .. data:: CHAT_SYSTEM = siege.network.Message.CHAT_SYSTEM

   .. data:: COMBAT_ATTACK = siege.network.Message.COMBAT_ATTACK

   .. data:: INVENTORY_CLOSE = siege.network.Message.INVENTORY_CLOSE

   .. data:: INVENTORY_INTERACT = siege.network.Message.INVENTORY_INTERACT

   .. data:: ITEM_ACTIVE_TOOLBAR = siege.network.Message.ITEM_ACTIVE_TOOLBAR

   .. data:: ITEM_CRAFT = siege.network.Message.ITEM_CRAFT

   .. data:: ITEM_DROP_GRAB = siege.network.Message.ITEM_DROP_GRAB

   .. data:: ITEM_INTERACT = siege.network.Message.ITEM_INTERACT

   .. data:: ITEM_INVENTORY_EQUIP = siege.network.Message.ITEM_INVENTORY_EQUIP

   .. data:: ITEM_RESEARCH = siege.network.Message.ITEM_RESEARCH

   .. data:: ITEM_RETURN_GRAB = siege.network.Message.ITEM_RETURN_GRAB

   .. data:: ITEM_SET_TOOLBAR = siege.network.Message.ITEM_SET_TOOLBAR

   .. data:: ITEM_SPLIT = siege.network.Message.ITEM_SPLIT

   .. data:: ITEM_SWAP_WITH_GRAB = siege.network.Message.ITEM_SWAP_WITH_GRAB

   .. data:: ITEM_UNEQUIP = siege.network.Message.ITEM_UNEQUIP

   .. data:: ITEM_USE = siege.network.Message.ITEM_USE

   .. data:: LOAD_COMPLETE = siege.network.Message.LOAD_COMPLETE

   .. data:: NPC_DISMISS = siege.network.Message.NPC_DISMISS

   .. data:: NPC_INTERACT = siege.network.Message.NPC_INTERACT

   .. data:: NPC_SHOW_HOME_UI = siege.network.Message.NPC_SHOW_HOME_UI

   .. data:: PARTICLE_SYSTEM = siege.network.Message.PARTICLE_SYSTEM

   .. data:: PLAYER_INPUT = siege.network.Message.PLAYER_INPUT

   .. data:: PLAYER_POSITION = siege.network.Message.PLAYER_POSITION

   .. data:: PLAYER_RESERVE = siege.network.Message.PLAYER_RESERVE

   .. data:: RESEARCH_DATA = siege.network.Message.RESEARCH_DATA

   .. data:: RESEARCH_INTERACT = siege.network.Message.RESEARCH_INTERACT

   .. data:: RESOLUTION_CHANGED = siege.network.Message.RESOLUTION_CHANGED

   .. data:: SHOW_COMBAT_NUMBER = siege.network.Message.SHOW_COMBAT_NUMBER

   .. data:: TALENT_PURCHASE_SKILL = siege.network.Message.TALENT_PURCHASE_SKILL

   .. data:: TRAVEL = siege.network.Message.TRAVEL

   .. data:: TRAVEL_ATTUNE = siege.network.Message.TRAVEL_ATTUNE

   .. data:: TRAVEL_SELECT = siege.network.Message.TRAVEL_SELECT

   .. data:: TRAVEL_SHOW_UI = siege.network.Message.TRAVEL_SHOW_UI

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

   .. data:: Reliable_ordered = siege.network.PacketReliability.Reliable_ordered

   .. data:: Reliable_ordered_receipt = siege.network.PacketReliability.Reliable_or...

   .. data:: Reliable_receipt = siege.network.PacketReliability.Reliable_receipt

   .. data:: Reliable_sequenced = siege.network.PacketReliability.Reliable_sequence...

   .. data:: Unreliable = siege.network.PacketReliability.Unreliable

   .. data:: Unreliable_receipt = siege.network.PacketReliability.Unreliable_receip...

   .. data:: Unreliable_sequenced = siege.network.PacketReliability.Unreliable_sequ...

MessageHandler
-----------------------------------
.. class:: MessageHandler

   

   .. method:: __call__( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :param arg3: 

      :type arg3: :class:`DataStream`

   .. staticmethod:: create( arg1)

      

      :param arg1: 

      :type arg1: object

      :rtype: :class:`MessageHandler`

NetworkConnection
-----------------------------------
.. class:: NetworkConnection

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: broadcast( packet[, channel=0[, reliability=siege.network.PacketReliability.Reliable[, priority=siege.network.PacketPriority.Medium]]])

      

      :param packet: 

      :type packet: :class:`DataStream`

      :param channel: 

      :type channel: int

      :param reliability: 

      :type reliability: :class:`PacketReliability`

      :param priority: 

      :type priority: :class:`PacketPriority`

      :rtype: int

   .. method:: receive( )

      

   .. method:: register( messageId, callback)

      

      :param messageId: 

      :type messageId: int

      :param callback: 

      :type callback: :class:`MessageHandler`

   .. method:: send( recipient, packet[, channel=0[, reliability=siege.network.PacketReliability.Reliable[, priority=siege.network.PacketPriority.Medium]]])

      

      :param recipient: 

      :type recipient: :class:`NetworkId`

      :param packet: 

      :type packet: :class:`DataStream`

      :param channel: 

      :type channel: int

      :param reliability: 

      :type reliability: :class:`PacketReliability`

      :param priority: 

      :type priority: :class:`PacketPriority`

      :rtype: int

   .. method:: unregister( messageId)

      

      :param messageId: 

      :type messageId: int

Client
-----------------------------------
.. class:: Client

   

   .. method:: send( packet[, channel=0[, reliability=siege.network.PacketReliability.Reliable[, priority=siege.network.PacketPriority.Medium]]])

      

      :param packet: 

      :type packet: :class:`DataStream`

      :param channel: 

      :type channel: int

      :param reliability: 

      :type reliability: :class:`PacketReliability`

      :param priority: 

      :type priority: :class:`PacketPriority`

      :rtype: int

Server
-----------------------------------
.. class:: Server

   

   .. method:: ban( arg2)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :rtype: str

   .. method:: ban( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: str

   .. method:: kick( arg2)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

   .. method:: unban( arg2)

      

      :param arg2: 

      :type arg2: str

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

   .. method:: getClient( )

      

      :rtype: :class:`Client`

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

      

   .. method:: setupServer( port, password)

      

      :param port: 

      :type port: int

      :param password: 

      :type password: str

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

   .. attribute:: onReset

      

