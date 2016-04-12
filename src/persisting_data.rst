
.. _persisting-data:

Persisting Data
===============

When creating more advanced mods you will find the need to persist data between play sessions.
This is easily done anywhere there are save and write functions provided.
Even when they are not there are means to ensure data is persisted.

Regardless of where the data is being saved and loaded you will always be working with a :mod:`DataStream`.
A DataStream works by saving/loading data piece by piece. Such as :py:func:`DataStream.writeUint32` is used to save a unsigned integer.

.. note::

    Always be sure to save and load the exact same data in the same order!

Here is an example of saving and loading some data.

.. code-block:: python

   def write(self, stream):
       stream.writeUint8(int(self.location))
       stream.writeUint32(self.entityId)
       stream.writeUint8(self.bagIndex)
       stream.writeUint8(self.index)
       stream.writeUint8(self.toolSlot)
       stream.writeString(self.slot)
       stream.writeString(self.reserve)
       stream.writeString(self.customLocation)

   def read(self, stream):
       self.location = stream.readUint8()
       self.entityId = stream.readUint32()
       self.bagIndex = stream.readUint8()
       self.index = stream.readUint8()
       self.toolSlot = stream.readUint8()
       self.slot = stream.readString()
       self.reserve = stream.readString()
       self.customLocation = stream.readString()

Persisting Means
----------------

World Saving/Loading
^^^^^^^^^^^^^^^^^^^^

There are several ways to persist data. :ref:`Components <creating-components>` and :ref:`plants <creating-plants>` provide read and write functions that are given a :mod:`DataStream`.

Sometimes you will want to save data outside of these. The :py:func:`world_saved` event can be listened to anytime you need to add a new :ref:`subsystem <creating-subsystems>` or :ref:`system <creating-systems>` to persist data.
Using the world_save will require you to create your own :mod:`DataStream` as well as save it with :py:func:`FileManager.asyncWrite` or :py:func:`File.save`. This will save the data into a new file.

Use the :py:func:`world_created` event to load this saved data. You should always check that the file exists with :py:func:`File.exists` and load it with :py:func:`File.load`.

.. note::

   Always be sure to save a version with the data to support backwards compability!

.. code-block:: python

   def _getPath(self, world):
       return os.path.join(world.path, "merchant")

   def _saveData(self, world, asynchronous):
       contentStash = game.content
       entityManager = game.entity
       stream = DataStream()
       stream.writeUint16(MerchantSystem.FILE_VERSION)
       self.wares.write(stream, contentStash, entityManager)
       self.daily.write(stream, contentStash, entityManager)
       if asynchronous:
           game.file.asyncWrite(self._getPath(world), FileOnCompleteHandler.create(), stream, useCompression=False)
       else:
           File.save(self._getPath(world), stream)

   def _loadData(self, world):
       if File.exists(self._getPath(world)):
           stream = DataStream()
           File.load(self._getPath(world), stream)
           version = stream.readUint16()
           contentStash = game.content
           entityManager = game.entity
           self.wares.read(stream, contentStash, entityManager)
           self.daily.read(stream, contentStash, entityManager)

   @staticmethod
   def register():
       merchant = MerchantSystem()
       game.registerSystem(MerchantSystem.NAME, merchant)
       if NetworkManager.isHost():
           # We only want to save the data on the host (server)
           game.events['world_saved'].listen(merchant._saveData)
           game.events['world_created'].listen(merchant._loadData)

   @staticmethod
   def unregister():
       if NetworkManager.isHost():
           game.events['world_saved'].remove(game.merchant._saveData)
           game.events['world_created'].remove(game.merchant._loadData)

.. note::

   This will work even without a system or subsystem.


Character Saving/Loading
^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you will want data to be saved with characters but not in a component.
This is accomplished using :py:func:`World.addPlayerDataHandlers`.
The provided reader and writer callbacks are called when a player is being saved or loaded.
Each reader/writer pair is associated with a key and if that key cannot be found when loading then it skips the saved data.

.. code-block:: python

   def testReader(player, stream):
      value = stream.readString()

   def testWriter(player, stream):
      stream.writeString("something")

   def register():
      World.get().addPlayerDataHandlers("test", testReader, testWriter)
