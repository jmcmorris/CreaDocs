.. _siege.particle:

siege.particle
==================

Easing
-----------------------------------
.. class:: Easing

   

   .. data:: BackIn = siege.particle.Easing.BackIn

   .. data:: BackInOut = siege.particle.Easing.BackInOut

   .. data:: BackOut = siege.particle.Easing.BackOut

   .. data:: BounceIn = siege.particle.Easing.BounceIn

   .. data:: BounceInOut = siege.particle.Easing.BounceInOut

   .. data:: BounceOut = siege.particle.Easing.BounceOut

   .. data:: CircularIn = siege.particle.Easing.CircularIn

   .. data:: CircularInOut = siege.particle.Easing.CircularInOut

   .. data:: CircularOut = siege.particle.Easing.CircularOut

   .. data:: CubicIn = siege.particle.Easing.CubicIn

   .. data:: CubicInOut = siege.particle.Easing.CubicInOut

   .. data:: CubicOut = siege.particle.Easing.CubicOut

   .. data:: ElasticIn = siege.particle.Easing.ElasticIn

   .. data:: ElasticInOut = siege.particle.Easing.ElasticInOut

   .. data:: ElasticOut = siege.particle.Easing.ElasticOut

   .. data:: ExponentialIn = siege.particle.Easing.ExponentialIn

   .. data:: ExponentialInOut = siege.particle.Easing.ExponentialInOut

   .. data:: ExponentialOut = siege.particle.Easing.ExponentialOut

   .. data:: LinearIn = siege.particle.Easing.LinearIn

   .. data:: LinearInOut = siege.particle.Easing.LinearInOut

   .. data:: LinearOut = siege.particle.Easing.LinearOut

   .. data:: None = siege.particle.Easing.None

   .. data:: QuadraticIn = siege.particle.Easing.QuadraticIn

   .. data:: QuadraticInOut = siege.particle.Easing.QuadraticInOut

   .. data:: QuadraticOut = siege.particle.Easing.QuadraticOut

   .. data:: QuarticIn = siege.particle.Easing.QuarticIn

   .. data:: QuarticInOut = siege.particle.Easing.QuarticInOut

   .. data:: QuarticOut = siege.particle.Easing.QuarticOut

   .. data:: QuinticIn = siege.particle.Easing.QuinticIn

   .. data:: QuinticInOut = siege.particle.Easing.QuinticInOut

   .. data:: QuinticOut = siege.particle.Easing.QuinticOut

   .. data:: SineIn = siege.particle.Easing.SineIn

   .. data:: SineInOut = siege.particle.Easing.SineInOut

   .. data:: SineOut = siege.particle.Easing.SineOut

TweenType
-----------------------------------
.. class:: TweenType

   

   .. data:: List = siege.particle.TweenType.List

   .. data:: Ranged = siege.particle.TweenType.Ranged

   .. data:: Static = siege.particle.TweenType.Static

Particle
-----------------------------------
.. class:: Particle

   

   .. attribute:: alpha

       |      TweenProperty of this particle's alpha


   .. attribute:: color

       |      TweenProperty of this particle's color


   .. attribute:: coords

       |      :class:`Texture` coordinates for this :class:`Particle`


   .. attribute:: lifetime

       |      :class:`Timer` that holds total life of this :class:`Particle`


   .. attribute:: position

       |      X,Y coordinates of this :class:`Particle`


   .. attribute:: rotation

       |      TweenProperty of this particle's rotation


   .. attribute:: scale

       |      TweenProperty of this particle's scale


   .. attribute:: x

       |      TweenProperty of this particle's x velocity


   .. attribute:: y

       |      TweenProperty of this particle's y velocity


PhysicsParticle
-----------------------------------
.. class:: PhysicsParticle

   

Tween
-----------------------------------
.. class:: Tween

   

   .. method:: chain( value)

      

      :param value: 

      :type value: float

      :rtype: :class:`Tween`

   .. method:: chain( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: float

      :param end: 

      :type end: float

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`Tween`

   .. method:: chainList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`Tween`

   .. method:: chainList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`Tween`

   .. method:: chainRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeFloat`

      :rtype: :class:`Tween`

   .. method:: chainRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: :class:`RangeFloat`

      :param end: 

      :type end: :class:`RangeFloat`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`Tween`

   .. method:: delay( duration)

      Delays the start of this tween by provided milliseconds.


      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`Tween`

   .. method:: loop( [times=-1[, duration=0]])

      Loops the tween for the specified number of times or duration.


      :param times: 

      :type times: int

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`Tween`

   .. method:: set( value)

      

      :param value: 

      :type value: float

      :rtype: :class:`Tween`

   .. method:: set( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: float

      :param end: 

      :type end: float

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`Tween`

   .. method:: setList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`Tween`

   .. method:: setList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`Tween`

   .. method:: setRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeFloat`

      :rtype: :class:`Tween`

   .. method:: setRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: :class:`RangeFloat`

      :param end: 

      :type end: :class:`RangeFloat`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`Tween`

TweenColor
-----------------------------------
.. class:: TweenColor

   

   .. method:: chain( value)

      

      :param value: 

      :type value: :class:`Color`

      :rtype: :class:`TweenColor`

   .. method:: chain( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: :class:`Color`

      :param end: 

      :type end: :class:`Color`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenColor`

   .. method:: chainList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`TweenColor`

   .. method:: chainList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenColor`

   .. method:: chainRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeColor`

      :rtype: :class:`TweenColor`

   .. method:: chainRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: :class:`RangeColor`

      :param end: 

      :type end: :class:`RangeColor`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenColor`

   .. method:: delay( duration)

      Delays the start of this tween by provided milliseconds.


      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenColor`

   .. method:: loop( [times=-1[, duration=0]])

      Loops the tween for the specified number of times or duration.


      :param times: 

      :type times: int

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenColor`

   .. method:: set( value)

      

      :param value: 

      :type value: :class:`Color`

      :rtype: :class:`TweenColor`

   .. method:: set( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: :class:`Color`

      :param end: 

      :type end: :class:`Color`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenColor`

   .. method:: setList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`TweenColor`

   .. method:: setList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenColor`

   .. method:: setRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeColor`

      :rtype: :class:`TweenColor`

   .. method:: setRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: :class:`RangeColor`

      :param end: 

      :type end: :class:`RangeColor`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenColor`

TweenUint8
-----------------------------------
.. class:: TweenUint8

   

   .. method:: chain( value)

      

      :param value: 

      :type value: int

      :rtype: :class:`TweenUint8`

   .. method:: chain( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: int

      :param end: 

      :type end: int

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

   .. method:: chainList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`TweenUint8`

   .. method:: chainList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

   .. method:: chainRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeUint8`

      :rtype: :class:`TweenUint8`

   .. method:: chainRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: :class:`RangeUint8`

      :param end: 

      :type end: :class:`RangeUint8`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

   .. method:: delay( duration)

      Delays the start of this tween by provided milliseconds.


      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

   .. method:: loop( [times=-1[, duration=0]])

      Loops the tween for the specified number of times or duration.


      :param times: 

      :type times: int

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

   .. method:: set( value)

      

      :param value: 

      :type value: int

      :rtype: :class:`TweenUint8`

   .. method:: set( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: int

      :param end: 

      :type end: int

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

   .. method:: setList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`TweenUint8`

   .. method:: setList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

   .. method:: setRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeUint8`

      :rtype: :class:`TweenUint8`

   .. method:: setRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: :class:`RangeUint8`

      :param end: 

      :type end: :class:`RangeUint8`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenUint8`

TweenVector
-----------------------------------
.. class:: TweenVector

   

   .. method:: chain( value)

      

      :param value: 

      :type value: :class:`Vector`

      :rtype: :class:`TweenVector`

   .. method:: chain( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: :class:`Vector`

      :param end: 

      :type end: :class:`Vector`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenVector`

   .. method:: chainList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`TweenVector`

   .. method:: chainList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenVector`

   .. method:: chainRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeVector`

      :rtype: :class:`TweenVector`

   .. method:: chainRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0[, delay=0]]])

      

      :param start: 

      :type start: :class:`RangeVector`

      :param end: 

      :type end: :class:`RangeVector`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :param delay: 

      :type delay: :class:`RangeUint`

      :rtype: :class:`TweenVector`

   .. method:: delay( duration)

      Delays the start of this tween by provided milliseconds.


      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenVector`

   .. method:: loop( [times=-1[, duration=0]])

      Loops the tween for the specified number of times or duration.


      :param times: 

      :type times: int

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenVector`

   .. method:: set( value)

      

      :param value: 

      :type value: :class:`Vector`

      :rtype: :class:`TweenVector`

   .. method:: set( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: :class:`Vector`

      :param end: 

      :type end: :class:`Vector`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenVector`

   .. method:: setList( values)

      

      :param values: 

      :type values: list

      :rtype: :class:`TweenVector`

   .. method:: setList( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: list

      :param end: 

      :type end: list

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenVector`

   .. method:: setRange( valueRange)

      

      :param valueRange: 

      :type valueRange: :class:`RangeVector`

      :rtype: :class:`TweenVector`

   .. method:: setRange( start, end[, easing=siege.particle.Easing.LinearIn[, duration=0]])

      

      :param start: 

      :type start: :class:`RangeVector`

      :param end: 

      :type end: :class:`RangeVector`

      :param easing: 

      :type easing: :class:`Easing`

      :param duration: 

      :type duration: :class:`RangeUint`

      :rtype: :class:`TweenVector`

ParticleEmitter
-----------------------------------
.. class:: ParticleEmitter

   

   .. method:: __init__( realmUid, loopWidth, position[, lifetime=1[, rate=0[, amount=1[, texturePath='']]]])

      

      :param realmUid: 

      :type realmUid: int

      :param loopWidth: 

      :type loopWidth: int

      :param position: 

      :type position: :class:`Vector`

      :param lifetime: 

      :type lifetime: int

      :param rate: 

      :type rate: int

      :param amount: 

      :type amount: int

      :param texturePath: 

      :type texturePath: str

   .. method:: addLightSource( [intensity=128[, decay=0[, brightness=1[, color=<siege.graphic.Color[, size=1]]]]])

      

      :param intensity: 

      :type intensity: int

      :param decay: 

      :type decay: int

      :param brightness: 

      :type brightness: float

      :param color: 

      :type color: :class:`Color`

      :param size: 

      :type size: int

   .. method:: animate( frames[, loop=1])

      Animates the particles with the given frames and frame times.


      :param frames:  (tuple) A tuple in the following format (:class:`PixelRect`, int).


      :type frames: list

      :param loop:  Number of times to loop. Defaults to 1 with a special case of 0 which means infinite.


      :type loop: int

   .. method:: attachTo( Entity)

      Attaches this :class:`ParticleEmitter` to an :class:`Entity`. Position is now relative to that :class:`Entity`


      :param Entity: 

      :type Entity: :class:`Entity`

   .. method:: createParticle( )

      Returns a newly created :class:`Particle`.


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

   .. method:: setLightSource( arg2)

      

      :param arg2: 

      :type arg2: :class:`LightSourceData`

   .. method:: setParticleArea( arg2)

      

      :param arg2: 

      :type arg2: :class:`Rect`

   .. method:: setParticlePositions( arg2)

      

      :param arg2: 

      :type arg2: list

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

   .. attribute:: alpha

       |      (:class:`TweenUint8`) :class:`Tween` used to determine the color of particles.


   .. attribute:: amount

       |      Amount of Particles to create each spawn


   .. attribute:: color

       |      (:class:`TweenColor`) :class:`Tween` used to determine the color of particles.


   .. attribute:: lastEmission

       |      :class:`Time` of last spawn


   .. attribute:: lifetime

       |      :class:`Timer` to track total life of this :class:`ParticleEmitter`


   .. attribute:: particleLife

       |      A :class:`Range` of lengths of time used for initial :class:`Particle` life times


   .. attribute:: rate

       |      Elapsed time to pass before spawning more Particles


   .. attribute:: realmUid

      

   .. attribute:: rotation

       |      (:class:`Tween`) :class:`Tween` used to determine the rotation of particles.


   .. attribute:: scale

       |      (:class:`TweenVector`) :class:`Tween` used to determine the scale of particles.


   .. attribute:: texture

       |      :class:`Texture` to draw for each :class:`Particle`


   .. attribute:: x

       |      (:class:`Tween`) :class:`Tween` used to determine the x velocity of particles.


   .. attribute:: y

       |      (:class:`Tween`) :class:`Tween` used to determine the y velocity of particles.


PhysicsParticleEmitter
-----------------------------------
.. class:: PhysicsParticleEmitter

   

   .. method:: __init__( realmUid, loopWidth, position[, lifetime=1[, rate=0[, amount=1[, texturePath='']]]])

      

      :param realmUid: 

      :type realmUid: int

      :param loopWidth: 

      :type loopWidth: int

      :param position: 

      :type position: :class:`Vector`

      :param lifetime: 

      :type lifetime: int

      :param rate: 

      :type rate: int

      :param amount: 

      :type amount: int

      :param texturePath: 

      :type texturePath: str

   .. attribute:: destroyOnCollision

       |      Destroy the particles when they collide with something


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

   

