
.. _mod-debugging:

Mod Debugging
=============

When creating more advanced mods there likely be issues that arise. Here are a few ways to approach and resolve them.

.. _developer_mode:

Developer Mode
--------------

Turning on Developer mode in the settings file allows for many in-game tools to be used. Open the :ref:`settings file <directory-structure>` and set "developer_mode" to true.

**Game Commands**
    :ref:`Game commands <game-commands>` can be used to perform many tasks and can even be added onto.

**Toggle Lighting**
    Pressing F4 will toggle the lighting in game.

**Debug Rendering**
    Pressing F3 will toggle debug draws which can show bounding rectangles. New debug draws can be added with :mod:`DebugDrawSystem`.

.. code-block:: python

    game.debugRender.add(player.entity.render.getRect(), Color(255, 0, 255))

**UI Reloading**
    When editing UI files (*.html, *js, *.css) the UI will automatically reload with the changes.

.. _using-logs:

Writing to the Log
------------------

Using the :mod:`Log` is crucial to debugging issues. Logs can be used to simply track the code execution or contain useful information on the state of things.

.. code-block:: python

    from siege.log import Log
    Log.info("Logging Example")


Using Siege Module
------------------

Since the entire game engine has exposed to python it has been compiled to a binary module and is possible to import as a normal python module.
This means that it is possible to use the siege engine in python scripts and the python interpreter.
This can be very useful when testing code or writing a helper script such as generating dungeons.

To use the siege module just drop it into whatever folder you want to import it from. Typically you would want it next to the crea game binary.

**Download Siege Module**
 * `Windows 32-bit <https://www.dropbox.com/s/yg9k4mb36zzqngk/siege.pyd?dl=0>`_
 * `Windows 64-bit <https://www.dropbox.com/s/swxweg50trwndnl/siege.pyd?dl=0>`_
 * `OSX <https://www.dropbox.com/s/8w30dqmbu40li0s/siege.so?dl=0>`_
 * `Linux <https://www.dropbox.com/s/drbvzaccgjlmioc/siege.so?dl=0>`_

Debugging UI
------------

While developing UI it is extremely useful to inspect and change elements.
This can be done using the `Coherent UI Debugger <coherent-debugger>` which works exactly like the `Chrome Developmer Tools <https://developer.chrome.com/devtools>`_.
