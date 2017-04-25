
.. _mod-registration:

Mod Registration
================

Mods that wish to provide callbacks to :ref:`events <game-events>` or provide new :ref:`subsystems <creating-subsystems>` and/or :ref:`components <creating-components>` can do so through mod registration.
Registration happens when a world is selected or a new world is created. Only the mods that are enabled for the world will be registered.
Use :py:func:`registration_finished` event to know when registration has finished.

Adding registration is easily done by creating a file such as mods/mymod/registration.py and inside of it provide a ``register()`` function.
It is important to be sure to fully unregister callbacks that you add during registration.
This can be achieved by ``game.onUnregistration.listen(systemUnregistration)`` and of course providing a ``systemUnregistration()``.
This is all setup and ready to use in the :ref:`mod template <mod-template>`.

Below is the core registration file, mods/core/registration.py, as an example.

.. code-block:: python

    from core.environment.sky import SkyRenderable
    import core.achievement
    import core.biome
    import core.component.registration
    import core.effect
    import core.events
    import core.item.armor.attribute
    import core.monster.affix
    import core.monster.boss
    import core.system.registration
    import core.terraform
    import core.terraform.world
    import core.terraform.dream_realm
    import core.terraform.forgotten_shrine
    import core.terraform.horde_realm
    import core.terraform.mighty_forest
    import core.terraform.throne_room
    import core.hit_tile

    from siege import game
    from siege.network import NetworkManager


    def register():
        game.onUnregistration.listen(systemUnregistration)
        game.events['world_loaded'].listen(SkyRenderable.handleWorldLoaded)
        game.events['registration_finished'].listen(core.terraform.world.addTemplate)
        game.events['registration_finished'].listen(core.terraform.forgotten_shrine.addTemplate)
        game.events['registration_finished'].listen(core.terraform.dream_realm.addTemplate)
        game.events['registration_finished'].listen(core.terraform.horde_realm.addTemplate)
        game.events['registration_finished'].listen(core.terraform.mighty_forest.addTemplate)
        game.events['registration_finished'].listen(core.terraform.throne_room.addTemplate)
        core.achievement.register()
        core.biome.register()
        core.component.registration.register()
        core.effect.register()
        core.events.register()
        core.item.armor.attribute.register()
        core.monster.affix.register()
        core.monster.boss.register()
        core.system.registration.register()
        core.terraform.register()
        if NetworkManager.isHost():
            core.hit_tile.register()


    def systemUnregistration():
        game.onUnregistration.remove(systemUnregistration)
        game.events['world_loaded'].remove(SkyRenderable.handleWorldLoaded)
        game.events['registration_finished'].remove(core.terraform.world.addTemplate)
        game.events['registration_finished'].remove(core.terraform.forgotten_shrine.addTemplate)
        game.events['registration_finished'].remove(core.terraform.dream_realm.addTemplate)
        game.events['registration_finished'].remove(core.terraform.horde_realm.addTemplate)
        game.events['registration_finished'].remove(core.terraform.mighty_forest.addTemplate)
        game.events['registration_finished'].remove(core.terraform.throne_room.addTemplate)
        core.achievement.unregister()
        core.biome.unregister()
        core.events.unregister()
        core.monster.boss.unregister()
        core.system.registration.unregister()
        core.terraform.unregister()
        if NetworkManager.isHost():
            core.hit_tile.unregister()
        return True
