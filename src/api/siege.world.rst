.. _siege.world:

siege.world
==================

PlayerList
-----------------------------------
.. class:: PlayerList

   

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

RealmLoader
-----------------------------------
.. class:: RealmLoader

   

   .. method:: getLoadedRegions( )

      

      :rtype: list

   .. method:: getSegments( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`SegmentList`

   .. method:: saveRegion( region[, shouldUnload=False, asynchronous])

      

      :param region: 

      :type region: int

      :param shouldUnload: 

      :type shouldUnload: bool

      :param asynchronous: 

      :type asynchronous: bool

   .. method:: saveRegions( asynchronous)

      

      :param asynchronous: 

      :type asynchronous: bool

   .. method:: unloadRegion( region)

      

      :param region: 

      :type region: int

   .. method:: updateRegion( region, handler)

      

      :param region: 

      :type region: int

      :param handler: 

      :type handler: object

   .. attribute:: onRegionLoad

      

   .. attribute:: onRegionUnload

      

SegmentList
-----------------------------------
.. class:: SegmentList

   

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

World
-----------------------------------
.. class:: World

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. method:: addPlayerDataHandlers( name, reader, writer)

      

      :param name: 

      :type name: str

      :param reader: 

      :type reader: object

      :param writer: 

      :type writer: object

   .. method:: getMousePosition( )

      

      :rtype: :class:`Vector`

   .. method:: getPlayer( )

      

      :rtype: :class:`Player`

   .. method:: getPlayer( client)

      

      :param client: 

      :type client: :class:`NetworkId`

      :rtype: :class:`Player`

   .. method:: getPlayer( entity)

      

      :param entity: 

      :type entity: :class:`Entity`

      :rtype: :class:`Player`

   .. method:: getPlayers( )

      

      :rtype: :class:`PlayerList`

   .. method:: getRealm( )

      

      :rtype: :class:`Realm`

   .. method:: getRealm( uid)

      

      :param uid: 

      :type uid: int

      :rtype: :class:`Realm`

   .. method:: getRealms( )

      

      :rtype: object

   .. method:: loadComplete( )

      

   .. method:: move( entity, realmUid, layer)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param realmUid: 

      :type realmUid: int

      :param layer: 

      :type layer: :class:`Layer`

   .. method:: move( entity, realm, layer)

      

      :param entity: 

      :type entity: :class:`Entity`

      :param realm: 

      :type realm: :class:`Realm`

      :param layer: 

      :type layer: :class:`Layer`

   .. method:: move( player, realm)

      

      :param player: 

      :type player: :class:`Player`

      :param realm: 

      :type realm: :class:`Realm`

   .. method:: requestRegion( realm, position, callback)

      

      :param realm: 

      :type realm: :class:`Realm`

      :param position: 

      :type position: :class:`Vector`

      :param callback: 

      :type callback: object

   .. method:: save( [asynchronous=True]])

      

      :param asynchronous: 

      :type asynchronous: bool

   .. method:: update( frameTime)

      

      :param frameTime: 

      :type frameTime: int

   .. staticmethod:: create( game, name, size, seed)

      Creates a new :class:`World` instance.


      :param game: 

      :type game: :class:`Game`

      :param name: 

      :type name: str

      :param size: 

      :type size: :class:`TileVector`

      :param seed: 

      :type seed: int

      :rtype: :class:`World`

   .. staticmethod:: get( )

      Retrieves the current :class:`World` instance.


      :rtype: :class:`World`

   .. staticmethod:: join( game, uid, name, realmInfos)

      

      :param game: 

      :type game: :class:`Game`

      :param uid: 

      :type uid: int

      :param name: 

      :type name: str

      :param realmInfos: 

      :type realmInfos: :class:`RealmInfoList`

      :rtype: :class:`World`

   .. staticmethod:: load( game, path)

      

      :param game: 

      :type game: :class:`Game`

      :param path: 

      :type path: object

      :rtype: :class:`World`

   .. staticmethod:: reset( )

      

   .. attribute:: name

      

   .. attribute:: path

      

   .. attribute:: player

      

   .. attribute:: playerData

      

   .. attribute:: players

      

   .. attribute:: realm

      

   .. attribute:: time

      

   .. attribute:: uid

      

WorldPlayerData
-----------------------------------
.. class:: WorldPlayerData

   

   .. method:: __init__( )

      

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. attribute:: homePoint

      

   .. attribute:: position

      

WorldPlayerDataList
-----------------------------------
.. class:: WorldPlayerDataList

   

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

WorldTime
-----------------------------------
.. class:: WorldTime

   

   .. method:: handleResize( width, height)

      

      :param width: 

      :type width: int

      :param height: 

      :type height: int

   .. method:: isDaytime( )

      

      :rtype: bool

   .. method:: isNight( )

      

      :rtype: bool

   .. method:: setSkyImage( path, transitionTime)

      

      :param path: 

      :type path: str

      :param transitionTime: 

      :type transitionTime: int

   .. attribute:: backgroundColor

      

   .. attribute:: days

      

   .. attribute:: hours

      

   .. attribute:: minutes

      

   .. attribute:: seconds

      

   .. data:: HOURS_IN_DAY = 24

   .. data:: MINUTES_IN_HOUR = 60

   .. data:: TIME_IN_MINUTE = 1000

