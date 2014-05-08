.. _siege.audio:

siege.audio
==================

SoundStatus
-----------------------------------
.. class:: SoundStatus

   

   .. data:: Paused = siege.audio.SoundStatus.Paused

   .. data:: Playing = siege.audio.SoundStatus.Playing

   .. data:: Stopped = siege.audio.SoundStatus.Stopped

SoundEffect
-----------------------------------
.. class:: SoundEffect

   

   .. method:: attachToEntity( entity[, stopWhenDestroyed=True])

      

      :param entity: 

      :type entity: :class:`Entity`

      :param stopWhenDestroyed: 

      :type stopWhenDestroyed: bool

   .. method:: getLoop( )

      

      :rtype: bool

   .. method:: getStatus( )

      

      :rtype: :class:`SoundStatus`

   .. method:: getVolume( )

      

      :rtype: int

   .. method:: inRealm( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. method:: pause( )

      

   .. method:: play( )

      

   .. method:: setLocation( arg2, arg3)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`Vector`

   .. method:: setLoop( arg2)

      

      :param arg2: 

      :type arg2: bool

   .. method:: setVolume( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: stop( )

      

AudioManager
-----------------------------------
.. class:: AudioManager

   

   .. method:: getTrackDuration( )

      

      :rtype: int

   .. method:: isPlayingTrack( )

      

      :rtype: bool

   .. method:: pauseTrack( )

      

   .. method:: play( name[, volume=100[, broadcast=False]])

      

      :param name: 

      :type name: str

      :param volume: 

      :type volume: int

      :param broadcast: 

      :type broadcast: bool

      :rtype: :class:`SoundEffect`

   .. method:: playAt( name, realmUid, position[, volume=100[, broadcast=False]])

      

      :param name: 

      :type name: str

      :param realmUid: 

      :type realmUid: int

      :param position: 

      :type position: :class:`Vector`

      :param volume: 

      :type volume: int

      :param broadcast: 

      :type broadcast: bool

      :rtype: :class:`SoundEffect`

   .. method:: playAttached( name, entity[, volume=100[, broadcast=False[, stopWhenDestroyed=True]]])

      

      :param name: 

      :type name: str

      :param entity: 

      :type entity: :class:`Entity`

      :param volume: 

      :type volume: int

      :param broadcast: 

      :type broadcast: bool

      :param stopWhenDestroyed: 

      :type stopWhenDestroyed: bool

      :rtype: :class:`SoundEffect`

   .. method:: playTrack( arg2, trackPath)

      

      :param arg2: 

      :type arg2: str

      :param trackPath: 

      :type trackPath: bool

   .. method:: resumeTrack( )

      

   .. method:: setTrackVolume( arg2)

      

      :param arg2: 

      :type arg2: float

   .. method:: stopTrack( )

      

   .. attribute:: masterVolume

      

   .. attribute:: musicVolume

      

   .. attribute:: sfxVolume

      

