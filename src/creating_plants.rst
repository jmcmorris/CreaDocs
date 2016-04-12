
.. _plants:

Plants
======

Plants can be found throughout the world of Crea. They typically have multiple growth stages and provide some seed upon harvest.
However, plants can be quite flexible and be made to do nearly anything - some requiring more work than others.

.. _creating-plants:

Creating Plants
---------------

Creating new types of plants are slightly more involved than some other content.
Plants are usually given a few visual variations for each stage in its life.
A stage can be anything and merely represents the current state the plant is in.

Here is an outline of the plant template.

.. py:function:: Plant(name, spaceRequired=None, variations=1, stages=None, plantType=core.plant.Plant, **kwargs)

    Sets up the content entity data of a Plant.

    :param str name: The name of the plant. This should be the key used for :ref:`localizations <creating-localizations>`.
    :param PixelVector spaceRequired: The amount of space this plant requires in order to be planted.
    :param int variations: The number of visual variations this plant has. Total number of sprites is variations * stages.
    :param stages: The stages of this plant. More details on plant stages can be found below.
    :type stages: list of core.plant.PlantStage
    :param plantType: The class used to create the instance of the plant.
    :param kwargs: Keyword argument list that will be passed to the main template class.


.. code-block:: python

   from core.template.animation import Frame
   from core.template.item import Loot
   from core.template.plant import Plant, PlantStage, PlantStageTimer

   from siege.util import minutes, PixelVector, RangeInt

   plant = Plant(
       name = "AshberryPlant",
       growsOn = ["soot"],
       spaceRequired = PixelVector(32, 32),
       variations = 3,
       stages = [
           PlantStageTimer(duration=RangeInt(minutes(4), minutes(6))),
           PlantStageTimer(duration=RangeInt(minutes(4), minutes(6))),
           PlantStage(loot=Loot('ashberry', dropRates={2: 25, 3: 60, 4: 15}))
       ]
   )

   plant.stageAnimations(
       Frame(2, 2, size=(17, 21), origin=(6, 18)),
       Frame(21, 2, size=(24, 35), origin=(9, 32)),
       Frame(47, 2, size=(36, 40), origin=(15, 37)),
       Frame(85, 2, size=(13, 21), origin=(7, 18)),
       Frame(100, 2, size=(24, 27), origin=(8, 24)),
       Frame(126, 2, size=(34, 39), origin=(15, 36)),
       Frame(162, 2, size=(19, 20), origin=(9, 17)),
       Frame(183, 2, size=(23, 32), origin=(9, 29)),
       Frame(208, 2, size=(31, 41), origin=(19, 38))
   )


.. _advanced-plants:

Advanced Plants
---------------

Plants use :mod:`OrganicComponent` which holds an instance of the provided plantType (defaults to ``core.plant.Plant``).
This is accessible through ``entity.organic.instance``.

The current stage along with much more data is all stored in the instance.
Animations will automatically be played and the next stage set.
Custom stages can provide logic on when a stage should change as well as save/load any data.

Here is the base PlantStage class that all plant stages are derived from.

.. code-block:: python

   class PlantStage(object):
       # Animations is a dictionary of animation type to a list of variations of that animation type.
       def __init__(self, animations, harvestLoot, nextStage, plant):
           self.animations = animations
           self.harvestLoot = harvestLoot
           self.nextStage = nextStage
           plant.animation.play(self.animations['idle'].format(plant.variation))

       def expire(self):
           # Called when the stage is being exited
           pass

       def write(self, stream):
           # Called when the plant is being saved
           pass

       def read(self, stream):
           # Called when the plant is being loaded
           pass

Here is one of the plant stages that automatically changes to the next stage after some amount of time.
In it you can see that we use write and read functions to :ref:`persist data <persisting-data>` between play sessions.

.. code-block:: python

   class PlantStageTimer(PlantStage):
       def __init__(self, animations, harvestLoot, nextStage, time, plant):
           super(PlantStageTimer, self).__init__(animations, harvestLoot, nextStage, plant)
           self.plant = plant
           self.growJobId = game.timer.add(time.getRandom(), self.grow)

       def expire(self):
           game.timer.cancel(self.growJobId)
           self.plant = None

       def grow(self):
           self.plant.setStage(self.nextStage)

       def write(self, stream):
           stream.writeInt32(game.timer.getTime(self.growJobId))

       def read(self, stream):
           game.timer.cancel(self.growJobId)
           self.growJobId = game.timer.add(stream.readInt32(), self.grow)

Plant stages by default have their next stage set to the following stage but they do not have to be linear.
Such as the Lonis plant goes back and forth between two stages depending on the time of day using ``core.plant.PlantStageDayTime``.

.. code-block:: python

    lonis = Plant(
        name = "Lonis",
        growsOn = ["dirt"],
        spaceRequired = PixelVector(32, 36),
        variations = 3,
        stages = [
            PlantStageTimer(duration=RangeInt(minutes(4), minutes(6))),
            PlantStageDayTime(timeRange=RangeInt(4, 19), loot=Loot('lonis_seed', dropRates={1: 60, 2: 30, 3: 10})),
            PlantStageDayTime(timeRange=RangeInt(20, 3), nextStage=1, loot=Loot('lonis_seed', dropRates={1: 20, 2: 60, 3: 20}))
        ]
    )

.. _creating-trees:

Creating Trees
--------------

Trees are very similar to other plants. The defining difference is that trees use modular sprites.
This means that trees are made up of many parts allowing trees to look different and grow to variable sizes.

.. py:function:: Tree(name, seed='', spaceRequired=None, treeType=core.plant.tree.Tree, *, bases=[], trunks=[], crowns=[], saplings=[], biomes={})

    Sets up the content entity data of a Tree.

    :param str name: The name of the tree. This should be the key used for :ref:`localizations <creating-localizations>`.
    :param str seed: The content name of the seed this tree drops when harvested.
    :param PixelVector spaceRequired: The amount of space this plant requires in order to be planted.
    :param treeType: The class used to create the instance of the tree.
    :param bases: A list of the sprites that can be used as a base (bottom of the tree).
    :type bases: list of core.template.plant.TreeImage
    :param trunks: A list of the sprites that can be used as a trunk (middle part that can extend).
    :type trunks: list of core.template.plant.TreeImage
    :param crowns: A list of the sprites that can be used as a crown.
    :type crowns: list of core.template.plant.TreeImage
    :param saplings: A list of the sprites that can be used to represent a sapling.
    :type saplings: list of core.template.plant.TreeImage
    :param dict biomes: Mapping of biome name to core.helper.AttrDict that can contain image, bases, trunks, crowns or saplings.

Additionally, any of the class attributes can be provided as a keyword argument. Here are all of the class attributes and the default values.

.. code-block:: python

    loot = []
    # The content of the wood this tree drops
    wood = "wood"
    # How many pieces of wood the tree should drop per trunk
    woodQuantity = 1
    # The amount of time it takes for the tree to grow
    growthTimeMin = minutes(4)
    growthTimeMax = minutes(10)
    # How much time it takes to recover from a hit
    recoveryTime = seconds(10)
    # How much life the tree has. The power of the tool used.
    saplingHealth = 40
    health = 100
    # How many trunks the tree can have
    trunkRange = (2, 6)
    # The level of the tree used for determining gather talent point gain
    level = 1
    # The color of the chop particles
    particleColor = Color(146, 101, 70)
    # The amount to shake the tree when chopped
    shakeAmount = ShakeAmount.NORMAL

Here is an example of a tree. To see more examples check out mods/core/plant/tree/.

.. code-block:: python

    from core.helper import AttrDict
    from core.template.plant import Tree, TreeImage

    from siege.graphic import Color
    from siege.util import PixelRect, PixelVector

    Tree(
        name = "DeadTree",
        seed = 'dead_seed',
        spaceRequired = PixelVector(44, 80),
        trunkRange = (2, 4),
        saplings = [TreeImage(rect=PixelRect(114, 64, 29, 50))],
        bases = [
            TreeImage(rect=PixelRect(2, 64, 110, 19)),
            TreeImage(rect=PixelRect(114, 2, 110, 18)),
            TreeImage(rect=PixelRect(114, 43, 110, 19))
        ],
        trunks = [
            TreeImage(rect=PixelRect(2, 2, 110, 18)),
            TreeImage(rect=PixelRect(2, 22, 110, 19)),
            TreeImage(rect=PixelRect(114, 22, 110, 19)),
            TreeImage(rect=PixelRect(2, 43, 110, 19))
        ],
        crowns = [
            TreeImage(rect=PixelRect(2, 153, 110, 103)),
            TreeImage(rect=PixelRect(145, 64, 110, 87)),
            TreeImage(rect=PixelRect(114, 153, 110, 103))
        ],
        biomes = {
            'Mountain': AttrDict(
                image = 'dead_snow_tree.png',
                saplings = [
                    TreeImage(rect=PixelRect(114, 64, 29, 50)),
                ],
                bases = [
                    TreeImage(rect=PixelRect(2, 64, 110, 19)),
                    TreeImage(rect=PixelRect(114, 43, 110, 19)),
                    TreeImage(rect=PixelRect(2, 2, 110, 18))
                ],
                trunks = [
                    TreeImage(rect=PixelRect(114, 2, 110, 18)),
                    TreeImage(rect=PixelRect(114, 22, 110, 19)),
                    TreeImage(rect=PixelRect(2, 22, 110, 19)),
                    TreeImage(rect=PixelRect(2, 43, 110, 19))
                ],
                crowns = [
                    TreeImage(rect=PixelRect(2, 169, 110, 103)),
                    TreeImage(rect=PixelRect(114, 169, 110, 103)),
                    TreeImage(rect=PixelRect(145, 64, 110, 103))
                ]
            )
        },
        particleColor = Color(93, 73, 48)
    )

Creating Seeds
--------------

Seeds can be planted to grow more of a plant. Much like plants and trees, seeds have their own template.

.. py:function:: Tree(name, plant, preview, center=0, frame=None, allowUnderground=False, onCeiling=False, underwaterSupport=UnderwaterSupport.Disallow, customUse=False, **kwargs)

    Sets up the content entity data of a Tree.

    :param str name: The name of the tree. This should be the key used for :ref:`localizations <creating-localizations>`.
    :param str plant: The content name of the plant this seed creates when planted.
    :param str preview: The path to the image that will be used to show a preview of where the plant will go.
    :param int center: The visual x-offset used for the preview.
    :param core.template.animation.Frame frame: The frame data used for the preview otherwise the entire image is used.
    :param bool allowUnderground: Whether this seed is allowed to be planted underground.
    :param bool onCeiling: Whether this seed is must be planted on the ceiling.
    :param UnderwaterSupport underwaterSupport: Whether this seed can be planted underwater or not.
    :param bool customUse: Whether this seed provides it's own use event or not.

Here is an example of a seed content. See mods/core/item/seed directory for more examples.

.. code-block:: python

    from core.template.animation import Frame
    from core.template.plant import Seed

    Seed(
        name = "DeadSeed",
        plant = 'dead_tree',
        center = 10,
        frame = Frame(114, 64, size=(29, 50), origin=(10, 50)),
        preview = 'mods/core/plant/tree/dead/dead_tree.png',
        buyPrice = 100,
        sellPrice = 2,
    )
