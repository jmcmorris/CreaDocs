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

RealmList
-----------------------------------
.. class:: RealmList

   

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

RealmLoader
-----------------------------------
.. class:: RealmLoader

   

   .. method:: getLoadedRegions( )

      Returns a Python list of all currently loaded regions


      :rtype: list

   .. method:: getSegments( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: :class:`SegmentList`

   .. method:: isRegionLoaded( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: isSaving( )

      

      :rtype: bool

   .. method:: loadRegions( [callback=None])

      Load all regions in this realm and set call back if necessary


      :param callback:  Function to set as realm loaded callback


      :type callback: object

   .. method:: saveRegion( [shouldUnload=False, asynchronous)

      Saves a region to the file system


      :param shouldUnload:  Set to true force unloading of region before saving, false otherwise


      :type shouldUnload: int

      :param asynchronous:  Set to true to force asynchronous file writing, false otherwise


      :type asynchronous: bool

   .. method:: saveRegions( asynchronous)

      Save all regions in this realm to the file system


      :param asynchronous:  Set to true to force asynchronous file writing, false otherwise


      :type asynchronous: bool

   .. method:: unloadRegion( region)

      Unloads region, saves region and game


      :param region:  Id of the region to unload


      :type region: int

   .. method:: update( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: updateRegion( region, handler)

      Reloads a region


      :param region:  Id of the region to load


      :type region: int

      :param handler:  Function for region load


      :type handler: :class:`FileOnCompleteHandler`

   .. method:: updateSaving( )

      

   .. attribute:: onRegionLoad

       |      :class:`Event` for region loading


   .. attribute:: onRegionUnload

       |      :class:`Event` for region unloading


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

   

   .. method:: __setattr__( attr, value)

      Changes an attribute of this :class:`World`


      :param attr:  Attribute name


      :type attr: str

      :param value:  Value for attribute


      :type value: object

   .. method:: addPlayerDataHandlers( name, reader, writer)

      Sets player reader and writer functions to parameters


      :param name:  Text name for functions


      :type name: str

      :param reader:  Reading function


      :type reader: object

      :param writer:  Writing function


      :type writer: object

   .. method:: createRealm( name, size, groundLevel, options)

      Creates a new realm in this world


      :param name:  Text name for the new realm


      :type name: str

      :param size:  Dimensions for the new realm


      :type size: :class:`TileVector`

      :param groundLevel:  Ground level value for the new realm


      :type groundLevel: int

      :param options:  Python dictionary of options for realm creation


      :type options: dict

      :rtype: :class:`Realm`

   .. method:: finishSaving( )

      Finishes any current saving and disables asynchronous saving.


   .. method:: getMousePosition( )

      Returns mouse pointer coordinates


      :rtype: :class:`Vector`

   .. method:: getPlayer( )

      Returns a single player


      :rtype: :class:`Player`

   .. method:: getPlayer( client)

      Returns target client from this world


      :param client:  :class:`Player` to search for


      :type client: :class:`NetworkId`

      :rtype: :class:`Player`

   .. method:: getPlayer( uid)

      Returns target player with the matching UID for this world


      :param uid:  The player's uid to retrieve.


      :type uid: int

      :rtype: :class:`Player`

   .. method:: getPlayer( entity)

      Returns target entity from this world


      :param entity:  :class:`Player` to search for


      :type entity: :class:`Entity`

      :rtype: :class:`Player`

   .. method:: getPlayers( )

      Return a list of all players in this world


      :rtype: :class:`PlayerList`

   .. method:: getPositionFromWorld( arg2)

      Gets the screen position from the provided world position.


      :param arg2: 

      :type arg2: :class:`Vector`

      :rtype: :class:`PixelVector`

   .. method:: getRealm( )

      Return the realm single player is in


      :rtype: :class:`Realm`

   .. method:: getRealm( uid)

      Return target realm in this world


      :param uid:  Unique identifier for target realm


      :type uid: int

      :rtype: :class:`Realm`

   .. method:: getRealm( name)

      Return target realm in this world


      :param name:  Text name for target realm


      :type name: str

      :rtype: :class:`Realm`

   .. method:: getRealms( )

      Return a list of all realms in this world


      :rtype: :class:`RealmList`

   .. method:: isActivePlayer( arg2)

      Return True if provided player is the main player otherwise false.


      :param arg2: 

      :type arg2: :class:`Player`

      :rtype: bool

   .. method:: isActivePlayer( arg2)

      Return True if provided entity is the main player otherwise false.


      :param arg2: 

      :type arg2: :class:`Entity`

      :rtype: bool

   .. method:: isInitialized( )

      Returns True if the world is fully initialized and ready for full use otherwise False.


      :rtype: bool

   .. method:: loadComplete( )

      Handle completion of a world load


   .. method:: move( entity, realmUid, layer)

      Removes entity from current realm and puts into a new one


      :param entity:  Target entity to move


      :type entity: :class:`Entity`

      :param realmUid:  Unique identifier for target realm


      :type realmUid: int

      :param layer:  :class:`Layer` to place entity into


      :type layer: :class:`Layer`

   .. method:: move( entity, realm, layer)

      Removes entity from current realm and puts into a new one


      :param entity:  Target entity to move


      :type entity: :class:`Entity`

      :param realm:  new realm for entity


      :type realm: :class:`Realm`

      :param layer:  :class:`Layer` to place entity into


      :type layer: :class:`Layer`

   .. method:: move( player, realm)

      Removes player from current realm and puts into a new one


      :param player:  Target player to move


      :type player: :class:`Player`

      :param realm:  new realm for entity


      :type realm: :class:`Realm`

   .. method:: requestRegion( player, realm, position, callback)

      Loads the area around the position for the provided player and once available calls the callback.


      :param player:  :class:`Player` that needs the tile segments


      :type player: :class:`Player`

      :param realm:  Target realm to search


      :type realm: :class:`Realm`

      :param position:  Coordinates to load the area around


      :type position: :class:`Vector`

      :param callback:  Callback that is called once area is available. Signature takes no additional arguments.


      :type callback: object

   .. method:: save( [asynchronous=True[, isExiting=False]])

      Save this world to the file system


      :param asynchronous:  Set to true to force asynchronous file writing, false otherwise


      :type asynchronous: bool

      :param isExiting:  Flag which should be set to true if the game is exiting immediately after this save.


      :type isExiting: bool

   .. method:: saveCharacter( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`NetworkId`

      :param arg3: 

      :type arg3: :class:`DataStream`

   .. method:: setPlayersHomePoint( player, realm, position)

      Set players home position and realm


      :param player:  Which player to change


      :type player: :class:`Player`

      :param realm:  Which realm will be home


      :type realm: :class:`Realm`

      :param position:  Which position will be home


      :type position: :class:`Vector`

   .. method:: update( frameTime)

      Update all player and loaded realms in this world


      :param frameTime:  Elapsed time this frame


      :type frameTime: int

   .. staticmethod:: create( game, name, size[, seed=0[, hasServerSideCharacters=False]])

      Creates a new :class:`World` instance.


      :param game:  The game this world belongs in


      :type game: :class:`Game`

      :param name:  Text name for this world


      :type name: str

      :param size:  Dimensions of this world


      :type size: :class:`TileVector`

      :param seed:  :class:`Random` number seed for this world


      :type seed: int

      :param hasServerSideCharacters: 

      :type hasServerSideCharacters: bool

      :rtype: :class:`World`

   .. staticmethod:: get( )

      Retrieves the current :class:`World` instance.


      :rtype: :class:`World`

   .. staticmethod:: join( game, uid, name, realmInfos[, hasServerSideCharacters=False])

      Add all realms from realmInfos to this world


      :param game:  The game this world belongs in


      :type game: :class:`Game`

      :param uid:  Unique identifier for this world


      :type uid: int

      :param name:  Text name for this world


      :type name: str

      :param realmInfos:  List of realms to add


      :type realmInfos: :class:`RealmInfoList`

      :param hasServerSideCharacters:  Option to enforce characters to be created and saved on the server side.


      :type hasServerSideCharacters: bool

      :rtype: :class:`World`

   .. staticmethod:: load( game, path)

      Load the world from the provided file at path


      :param game:  The game this world belongs in


      :type game: :class:`Game`

      :param path:  Path to save file


      :type path: object

      :rtype: :class:`World`

   .. staticmethod:: reset( )

      Clear all sub systems and realms in this world


   .. attribute:: CONTENT_FILE_VERSION

      

   .. attribute:: DATA_FILE_VERSION

      

   .. attribute:: data

       |      (dict) Container for miscellaneous world data.


   .. attribute:: hasServerSideCharacters

       |      Tracks if characters are saved on the server side


   .. attribute:: name

       |      Text name of this world


   .. attribute:: path

       |      Path to save file


   .. attribute:: player

       |      :class:`Player` data


   .. attribute:: playerData

       |      Data for which world and realm players are in


   .. attribute:: players

       |      :class:`PlayerList` of all players


   .. attribute:: playtime

       |      Tracks playtime in seconds


   .. attribute:: realm

       |      Returns current realm


   .. attribute:: remnaLevel

       |      Worlds current remna level


   .. attribute:: time

       |      :class:`WorldTime` data


   .. attribute:: uid

       |      Unique identifier for this world


WorldInfo
-----------------------------------
.. class:: WorldInfo

   

   .. method:: load( worldPath)

      Reads the world information stored at <path>/info.


      :param worldPath:  (str) The world path.


      :type worldPath: object

   .. method:: packagesAvailable( contentStash)

      Returns true if all enabled packages are available in content stash otherwise false.


      :param contentStash: 

      :type contentStash: :class:`ContentStash`

      :rtype: bool

   .. method:: save( path, asynchronous)

      Saves the world information to disk.


      :param path:  (Path) The path of the world.


      :type path: object

      :param asynchronous: 

      :type asynchronous: bool

   .. staticmethod:: saveWorld( world, asynchronous)

      Saves the world information to disk.


      :param world:  The world to save information about.


      :type world: :class:`World`

      :param asynchronous:  Whether the save should be asynchronous or not.


      :type asynchronous: bool

   .. attribute:: FILE_VERSION

      

   .. attribute:: hasServerSideCharacters

       |      Tracks if characters are saved on the server side


   .. attribute:: name

       |      The name of the world.


   .. attribute:: packages

       |      The packages state for the world.


   .. attribute:: playtime

       |      The playtime for the world.


   .. attribute:: realms

       |      (:class:`RealmInfoList`) List of all :class:`RealmInfo` saved for the world.


   .. attribute:: uid

       |      The unique identifier for the world.


WorldPlayerData
-----------------------------------
.. class:: WorldPlayerData

   

   .. method:: __setattr__( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: object

   .. attribute:: homePoint

      

   .. attribute:: homeRealm

      

   .. attribute:: position

      

   .. attribute:: realmUid

      

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

   

   .. method:: getAmbientColor( hour)

      Gets the ambient light color for the provided time.


      :param hour:  (Int32) The time for the desired color.


      :type hour: int

      :rtype: :class:`Color`

   .. method:: getBackgroundColor( hour)

      Gets the background color for the provided time.


      :param hour:  (Int32) The time's hour to get the background for.


      :type hour: int

      :rtype: :class:`Color`

   .. method:: getHour( )

      Gets the current hour. Will return realm set time if defined.


      :rtype: int

   .. method:: getMinutes( )

      Gets the current minutes in the hour. Returns 0 if realm has a set time.


      :rtype: int

   .. method:: getNextHour( )

      Gets the next hour. Will use realm set time if defined.


      :rtype: int

   .. method:: handleResize( width, height)

      Recreate rendering context for window resize


      :param width:  New width


      :type width: int

      :param height:  New height


      :type height: int

   .. method:: isDaytime( )

      Returns true if hour > 4 and hour < 19, false otherwise


      :rtype: bool

   .. method:: isNight( )

      Returns true if hour <= 4 and hour >= 19, false otherwise


      :rtype: bool

   .. method:: setSkyImage( path, transitionTime)

      Set the sky image to one at path


      :param path:  Path to image file


      :type path: str

      :param transitionTime:  :class:`Time` in milliseconds until sky changes


      :type transitionTime: int

   .. attribute:: days

       |      Elapsed time in days


   .. attribute:: hours

       |      Elapsed time hours


   .. attribute:: minutes

       |      Elapsed time in minutes


   .. attribute:: seconds

       |      Elapsed time in milliseconds


   .. data:: HOURS_IN_DAY = 24

   .. data:: MINUTES_IN_HOUR = 60

   .. data:: TIME_IN_MINUTE = 1000

