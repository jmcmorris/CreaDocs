.. _siege.particle:

siege.particle
==================

Particle
-----------------------------------
.. class:: Particle

   

   .. method:: __init__( )

      

   .. attribute:: color

      

   .. attribute:: coord

      

   .. attribute:: lifetime

      

   .. attribute:: position

      

   .. attribute:: scale

      

   .. attribute:: velocity

      

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

   .. method:: attachTo( arg2)

      

      :param arg2: 

      :type arg2: :class:`Entity`

   .. method:: createParticle( arg2, arg3, arg4, arg5, arg6, arg7)

      

      :param arg2: 

      :type arg2: int

      :param arg3: 

      :type arg3: :class:`Vector`

      :param arg4: 

      :type arg4: :class:`RangeColor`

      :param arg5: 

      :type arg5: :class:`RangeVector`

      :param arg6: 

      :type arg6: :class:`RangeFloat`

      :param arg7: 

      :type arg7: :class:`RangeVector`

      :rtype: :class:`Particle`

   .. method:: getCount( )

      

      :rtype: int

   .. method:: getPosition( )

      

      :rtype: :class:`Vector`

   .. method:: render( arg2)

      

      :param arg2: 

      :type arg2: :class:`sfRenderTarget`

   .. method:: setPosition( arg2)

      

      :param arg2: 

      :type arg2: :class:`Vector`

   .. method:: setTexture( texture[, coords=[]]])

      

      :param texture: 

      :type texture: :class:`Texture`

      :param coords: 

      :type coords: list

   .. method:: update( arg2)

      

      :param arg2: 

      :type arg2: int

   .. method:: updateLife( arg2)

      

      :param arg2: 

      :type arg2: int

      :rtype: bool

   .. attribute:: amount

      

   .. attribute:: colorEnd

      

   .. attribute:: colorStart

      

   .. attribute:: lastEmission

      

   .. attribute:: lifetime

      

   .. attribute:: particleLife

      

   .. attribute:: particlePosition

      

   .. attribute:: rate

      

   .. attribute:: realmUid

      

   .. attribute:: rotationChange

      

   .. attribute:: rotationStart

      

   .. attribute:: scaleChange

      

   .. attribute:: scaleStart

      

   .. attribute:: texture

      

   .. attribute:: velocityChange

      

   .. attribute:: velocityStart

      

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

      

   .. attribute:: friction

      

   .. attribute:: gravity

      

   .. attribute:: restitution

      

ParticleSystem
-----------------------------------
.. class:: ParticleSystem

   

   .. method:: add( arg2, arg3])

      

      :param arg2: 

      :type arg2: :class:`ParticleEmitter`

      :param arg3]: 

      :type arg3]: int

   .. method:: clear( )

      

   .. method:: getCount( )

      

      :rtype: int

   .. method:: handleNetworkReset( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Server`

      :param arg3: 

      :type arg3: :class:`Client`

   .. method:: remove( arg2)

      

      :param arg2: 

      :type arg2: :class:`ParticleEmitter`

