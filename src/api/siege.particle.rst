.. _siege.particle:

siege.particle
==================

Particle
-----------------------------------
.. class:: Particle

   

   .. method:: __init__( )

      

   .. attribute:: color

       |      :class:`Range` of values to color this :class:`Particle` based on lifetime


   .. attribute:: coord

       |      :class:`Texture` coordinates for this :class:`Particle`


   .. attribute:: lifetime

       |      :class:`Timer` that holds total life of this :class:`Particle`


   .. attribute:: position

       |      X,Y coordinates of this :class:`Particle`


   .. attribute:: scale

       |      :class:`Range` of values to scale this :class:`Particle` based on lifetime


   .. attribute:: velocity

       |      :class:`Vector` of this Particle's velocity to be added to the position each update


PhysicsParticle
-----------------------------------
.. class:: PhysicsParticle

   

ParticleEmitter
-----------------------------------
.. class:: ParticleEmitter

   

   .. method:: __init__( arg2, arg3, arg4, arg5, arg6)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :param arg4: 

      :type arg4: :class:`Vector`

      :param arg5: 

      :type arg5: int

      :param arg6: 

      :type arg6: int

   .. method:: attachTo( Entity)

      Attaches this :class:`ParticleEmitter` to an :class:`Entity`. Position is now relative to that :class:`Entity`


      :param Entity: 

      :type Entity: :class:`Entity`

   .. method:: createParticle( lifespan, position, color, velocity, rotation, scale)

      Returns a new :class:`Particle` with these arguments


      :param lifespan:  How long the Paritcle will live


      :type lifespan: int

      :param position:  X,Y coordinates of the :class:`Particle`


      :type position: :class:`Vector`

      :param color:  :class:`Range` of values to color this :class:`Particle`


      :type color: :class:`RangeColor`

      :param velocity:  :class:`Vector` of this Particle's velocity to be added to the position each update


      :type velocity: :class:`RangeVector`

      :param rotation:  :class:`Range` of values to rotate this :class:`Particle`


      :type rotation: :class:`RangeFloat`

      :param scale:  :class:`Range` of values to scale this :class:`Particle`


      :type scale: :class:`RangeVector`

      :rtype: :class:`Particle`

   .. method:: getCount( )

      Return the number of Particles this :class:`ParticleEmitter` tracks


      :rtype: int

   .. method:: getPosition( )

      If attached to an :class:`Entity`, return position relative to that :class:`Entity`.  Otherwise return Position


      :rtype: :class:`Vector`

   .. method:: render( window)

      Draw all Particles in this :class:`ParticleEmitter`


      :param window:  The window to draw on


      :type window: :class:`sfRenderTarget`

   .. method:: setPosition( position)

      Changes X,Y coordinates to position


      :param position:  X,Y coordinates to change to


      :type position: :class:`Vector`

   .. method:: setTexture( texture[, coords=[]])

      Change ParticleEmitter's :class:`Texture` and corresponding coordinates


      :param texture:  The :class:`Texture` to change to


      :type texture: :class:`Texture`

      :param coords:  List of coordinates to give to the :class:`Texture`


      :type coords: list

   .. method:: update( frameTime)

      Updates all Particles in this :class:`ParticleEmitter`


      :param frameTime:  elapsed time this frame


      :type frameTime: int

   .. method:: updateLife( frameTime)

      Updates only the lifetime and the lifetime of all Particles in this ParticleEmitter:param frameTime: elapsed time this frame


      :param frameTime: 

      :type frameTime: int

      :rtype: bool

   .. attribute:: amount

       |      Amount of Particles to create each spawn


   .. attribute:: colorEnd

       |      A :class:`Range` of Color's used for the end of the :class:`Range` for each :class:`Particle` color


   .. attribute:: colorStart

       |      A :class:`Range` of Color's used for the start of the :class:`Range` for each :class:`Particle` color


   .. attribute:: lastEmission

       |      :class:`Time` of last spawn


   .. attribute:: lifetime

       |      :class:`Timer` to track total life of this :class:`ParticleEmitter`


   .. attribute:: particleLife

       |      A :class:`Range` of lengths of time used for intial Paritcle life times


   .. attribute:: particlePosition

       |      A :class:`Range` of intial positions of each :class:`Particle` spawned


   .. attribute:: rate

       |      Elapsed time to pass before spawning more Particles


   .. attribute:: realmUid

      

   .. attribute:: rotationChange

       |      A :class:`Range` of values used to add to rotationStart for the end of the :class:`Range` for each :class:`Particle` rotation


   .. attribute:: rotationStart

       |      A :class:`Range` of values used for the start of the :class:`Range` for each :class:`Particle` rotation


   .. attribute:: scaleChange

       |      A :class:`Range` of values used to add to scaleStart for the end of the :class:`Range` for each :class:`Particle` scale


   .. attribute:: scaleStart

       |      A :class:`Range` of values used for the start of the :class:`Range` for each :class:`Particle` scale


   .. attribute:: texture

       |      :class:`Texture` to draw for each :class:`Particle`


   .. attribute:: velocityChange

       |      A :class:`Range` of Vectors used to add to velocityStart for the end of the :class:`Range` for each :class:`Particle` velocity


   .. attribute:: velocityStart

       |      A :class:`Range` of Vectors used for the start of the :class:`Range` for each :class:`Particle` velocity


PhysicsParticleEmitter
-----------------------------------
.. class:: PhysicsParticleEmitter

   

   .. method:: __init__( arg2, arg3, arg4, arg5, arg6)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: int

      :param arg4: 

      :type arg4: :class:`Vector`

      :param arg5: 

      :type arg5: int

      :param arg6: 

      :type arg6: int

   .. attribute:: fallCap

       |      Sets the fallcap :class:`Vector` for Particles in this emitter


   .. attribute:: friction

       |      Sets the friction :class:`Vector` for Particles in this emitter


   .. attribute:: gravity

       |      Sets the gravity :class:`Vector` for Particles in this emitter


   .. attribute:: restitution

       |      Sets the restitution :class:`Vector` for Particles in this emitter


Renderable)
-----------------------------------
.. class:: Renderable)

   

Renderable)
-----------------------------------
.. class:: Renderable)

   

