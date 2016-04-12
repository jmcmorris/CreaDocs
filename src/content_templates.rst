
.. _content-templates:

Content Templates
=================


.. _template-basics:

Template Basics
---------------

Content templates are used to help simplify creating new content. Templates are used for groups of similar content.
Such as there is a Sword template that is used for all swords since each sword is nearly the same.
This prevents having to repeat every detail of a sword such that it has an :mod:`ItemComponent`,
a :mod:`WeaponComponent` that is a sword type with the attack combos, an :mod:`EquipmentComponent` and so on.

All templates can be found in the mods/core/template/ directory.
Most content uses template that build off the base template class, ``core.template.template.Template``.


.. _understanding-templates:

Understanding Templates
-----------------------

There are many templates but they all build off of ``core.template.template.Template`` and have the same goal - to simplify content creation.
This is achieved by giving templates an easily readable interface and giving a great deal of flexibility to avoid repeating data.

The most important aspect of templates are their constructors since they typically take the bulk of the data.
In order to provide flexibility templates generally will have a few arguments, a few keyword arguments with default values and then a keyword argument list (``**kwargs``).
The ``**kwargs`` is used in many places such as passing it to the parent constructor and sometimes will be given default values.


.. _deeper-understanding:

Deeper Understanding
--------------------

There is a bit of black magic employed to achieve as simple of an interface as possible.
The entire job of templates is to add :ref:`components <creating-components>` to the entity.
To avoid having to manually add the component definition with ``template.add(Item())`` we use ``core.template.template.Template.__getattr__``.
With this the first time a component is accessed by name from the template it will automatically be added.

.. code-block:: python

   template.item.buyPrice = 100

Taking this a step further to compact the interface even more we use :py:func:`ComponentDefinition.set`.
With it we are able to use the provided ``*kwargs`` to set the values of a list of attributes.

.. code-block:: python

   attrs = ['paths', 'bodies', 'canEquip', 'onEquip', 'onUnequip', 'levelRequired', 'isAttached']
   self.equipment.set(attrs, kwargs)


.. _creating-templates:

Creating Templates
------------------

Anytime you find that you are repeating yourself while creating content then take that as a good hint that you should make a new template.
Templates should be placed in core/mymod/template/ inside of a .py file.

When creating a new template you will always want to at least inherit from the base Template.

.. note::

   Keep your template interface as simple as possible!

Here is the NPC template as an example. You can find many more examples in the mods/core/template/ directory.

.. code-block:: python

   class Npc(Template):
       def __init__(self, name, markerIcon='', gestureSound='', gestureSoundDelay=0, **kwargs):
           Template.__init__(self, name, **kwargs)
           self.placeable(floor_axis=Axis(animation="idle", area=PixelRect(0, 0, 22, 49)))
           self.event['collect'].listen(handleNpcCollect)
           self.hasMapMarker(markerType='npc', icon=markerIcon)
           self.gestureSound = gestureSound
           self.gestureSoundDelay = gestureSoundDelay
           self._onCreate = self.setupGestureTimer

       def interact(self, func):
           def _interact(func, player, entity, position):
               self.playGesture(entity)
               func(player, entity, position)
           self.event['interact'].listen(partial(_interact, func))

       def playGesture(self, entity):
           if entity.animation.getAnimationName() == 'idle':
               if self.gestureSound:
                   if self.gestureSoundDelay > 0:
                       callback = partial(game.audio.playAt, self.gestureSound, entity.realm.uid, entity.getPosition(), broadcast=True)
                       game.timer.add(self.gestureSoundDelay, callback, isPrecise=True)
                   else:
                       game.audio.playAt(self.gestureSound, entity.realm.uid, entity.getPosition(), broadcast=True)
               entity.animation.play('gesture')
               entity.animation.queue('idle')

       def setupGestureTimer(self, entity):
           def playAnimation():
               self.playGesture(entity)
               game.timer.add(minutes(Random.get(1.5, 2.5)), playAnimation)
           if not entity.isContentEntity():
               game.timer.add(minutes(Random.get(1, 2.5)), playAnimation)
