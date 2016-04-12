
.. _creating-npcs:

Creating NPCs
==============

Creating NPCs is an extension of creating :ref:`Basic Items <basic-items>`.
Getting started we'll want to create a .ce file in mods/core/npc/.
NPCs have their own :ref:`content template <content-template>` to simplify the creation.

The NPC template is fairly simple with only a few parameters.

.. py:function:: Npc(name, markerIcon='', gestureSound='', gestureSoundDelay=0, **kwargs)

    Sets up the content entity data of an NPC.

    :param str name: The name of the NPC. This should be the key used for :ref:`localizations <creating-localizations>`.
    :param str markerIcon: The path of the marker icon to use on maps to represent this NPC.
    :param str gestureSound: The path of the sound effect to use when this NPC gestures. Leave empty if no sound should be played.
    :param int gestureSoundDelay: The amount of time (ms) to delay playing the gesture sound after starting the gesture animation.
    :param kwargs: Keyword argument list that will be passed to the main template class.


NPCs typically should be interactable so it is important to provide a custom :py:func:`interact` function.
Below is a full example of an NPC content file.

.. code-block:: python

    from core.template.animation import Frame, Frames
    from core.template.npc import Npc

    from siege import game
    from siege.io import DataStream
    from siege.network import Message
    from siege.util import PixelVector

    merchant = Npc(
        name = "Merchant",
        markerIcon = 'mods/core/item/outfit/merchant_outfit.png',
        gestureSound = "mods/core/audio/sfx/npc/merchant_gesture.ogg",
        gestureSoundDelay = 100
    )


    @merchant.interact
    def interact(player, entity, position):
        packet = DataStream(Message.SHOW_UI)
        packet.writeString("shop")
        packet.writeUint32(entity.id)
        packet.writeString("merchant")
        game.network.getServer().send(player.networkId, packet)

    idle = merchant.getSpriteFrames(
        frames = [
            Frame(2, 2),
            Frame(33, 2),
            Frame(64, 2),
            Frame(95, 2),
            Frame(126, 2),
            Frame(2, 55),
            Frame(33, 55)
        ],
        size = PixelVector(31, 53),
        origin = PixelVector(14, 29)
    )

    animate = merchant.getSpriteFrames(
        frames = [
            Frame(64, 55),
            Frame(93, 55),
            Frame(122, 55),
            Frame(2, 117),
            Frame(31, 117),
            Frame(60, 117),
            Frame(89, 117)
        ],
        size = PixelVector(29, 62),
        origin = PixelVector(15, 38)
    )

    merchant.animations(
        start = 'idle',
        idle = Frames(idle(1)),
        gesture = (
            Frames(idle(2, 3, 4, 5, 6, 7, 6, 5, 4), time=100),
            Frames(idle(3), time=500),
            Frames(idle(4, 5, 6, 7, 6, 5, 4), time=100),
            Frames(idle(3), time=500),
            Frames(idle(4, 5, 6, 7, 6, 5, 4, 3, 2), time=100)
        ),
        animate = Frames(animate(), time=100),
        disableLooping = ['animate', 'gesture']
    )
