
.. _game-events:

Game Events
===========

Crea uses an event system to allow for actions to be listened to and provide custom logic.
All events use the :mod:`GameEvent` interface which we will go over some below.

Event Types
-----------

While all events share the same interface, they are used in many places.

Global game events are used with game.events which is technically an :mod:`EventComponent`.
This allows for new events to be added easily and listened to by name.

.. code-block:: python

    game.events['player_respawn'].invoke(player)
    # elsewhere...
    game.events['player_respawn'].listen(player)

The EventComponent is an actual component that can be added to any :mod:`Entity` and consequently any entity can invoke and listen to events on itself.
This is used for many things such as when an entity is interacted with it uses the event 'interact'.

.. code-block:: python

    entity.event['interact'].listen(self.interact)

Sometimes a :mod:`GameEvent` is used directly. This is typically for when a system or component has a specific event it wants to invoke.
Such as in the ResearchComponent at mods/core/component/research.py we use a GameEvent for when a new item is discovered.

.. code-block:: python

    self.onDiscovered = GameEvent()
    # Elsewhere in ResearchComponent
    self.onDiscovered.invoke(content.id)

    # Somewhere completely different we can listen to this.
    entity.research.onDiscovered.listen(self.handleDiscovered)

Using Events
------------

The :mod:`GameEvent` interface is fairly straight-forward with :py:func:`GameEvent.listen` and :py:func:`GameEvent.invoke` being the two most important functions.

When listening to an event it is important to ensure the event handler signature properly matches the arguments that are provided to the event's invoke.

.. note::

    The return value from an event handler tells the GameEvent if it should remove the handler or not. Return True to remove the handler or return nothing to keep it.

.. code-block:: python

    def playerCreated(player):
        player.entity.inventory.addBag(0, PlayerTuning.STARTING_BAG_SIZE)

    def register():
        game.events["player_created"].listen(playerCreated)

    def unregister():
        game.events["player_created"].remove(playerCreated)

You'll see we also need to call :py:func:`GameEvent.remove` when we are done with it. This is especially important with global events when :py:func:`Game.onUnregistration` is invoked.

.. note::

    Always be sure to remove an event when it is no longer needed!


Global Game Events
------------------

.. py:function:: auri_tree_grown(entity)

   Called when an Auri tree becomes fully grown.

   :param Entity entity: The Auri tree entity.


.. py:function:: backup_saves(*paths)

   Called when saved file(s) need to be backed up. This only happens once per session when the game is exiting.

   :param paths: An arbitrary argument list of paths.


.. py:function:: character_saved(player)

   Called when a player character has been saved to disk.

   :param Player player: The player that was just saved.


.. py:function:: client_input_ready(client)

   Called when a player's input has been initialized. This can be used to manipulate the input such as adding new core.system.input.InputStateHandler.

   :param client: The client input that is now ready.
   :type client: core.system.input.ClientInput


.. py:function:: control_change(controllerType, name, controlCode)

   Called when a control input value is changed.

   :param controllerType: The
   :type controllerType: core.system.input.ControllerTypes
   :param str name: The name of the control that is changing. This is the key used in the controls in settings.
   :param controlCode: The new controller code that will be used.
   :type controlCode: Keyboard, Joy or JoyCombo


.. py:function:: create_realm(realm)

   Called when a realm has been created. This includes realms created during load.

   :param Realm realm: The newly created realm.


.. py:function:: create_talent(talent)

   Called when a talent is being created for a player.

   :param Talent talent: The newly created talent.


.. py:function:: crystal_activated(player, travelPlayer, self.crystals[uid])

   Called when a Way Crystal has been activated by a player.

   :param Player player: The player that activated the crystal.
   :param travelPlayer: The TravelPlayer that belongs to the player activating the crystal.
   :type travelPlayer: core.system.travel.TravelPlayer
   :param int crystalId: The entity ID of the activated crystal.


.. py:function:: damage_item(entity, isDestroyed)

   Called when a placed item has been damaged (being collected).

   :param Entity entity: The item being damaged.
   :param bool isDestroyed: Whether the item has been destroyed (turned to a drop item).


.. py:function:: dropped_collected(entity, item)

   Called when a player collects a dropped item.

   :param Entity entity: The Player entity that collected the dropped item.
   :para InventoryItem item: The dropped item that was collected.


.. py:function:: dropped_expired(realm, entity)

   Called when a dropped item has expired and will be removed.

   :param Realm realm: The realm the dropped item existed in.
   :param Entity entity: The entity of the dropped item.


.. py:function:: exit_game()

   Called when the game is being exited by the window being closed.


.. py:function:: gather_tile(player, tileComponent, entity, tilePosition)

   Called when a tile is being gathered by a player.

   :param Player player: The player gathering the tile.
   :param TileComponent tileComponent: The tile that is being gathered.
   :param Entity entity: The dropped item entity of the tile.
   :param TileVector tilePosition: The position of the gathered tile.


.. py:function:: hit_tile(entity, realm, tileComponent, tileLayer.type, tilePosition, brokeTile)

   Called when an entity hits a tile to harvest it.

   :param Entity entity: The entity that hit the tile. This can be a player or some other entity like a projectile.
   :param Realm realm: The realm the tile exists in.
   :param TileComponent tileComponent: The tile that is being hit.
   :param Layer layerType: The type of layer the tile belongs to.
   :param TileVector tilePosition: The position of the tile.
   :param bool brokeTile: Whether this tile was destroyed or not.


.. py:function:: load_biomes(biomes)

   Called when requesting all possible biomes to use during world generation. Append new biomes to the provided list.

   :param list biomes: Empty list for which :class:`Biome` instances should be added.


.. py:function:: merchant_wares(wares, daily)

   Called when the merchant wares have been setup. These lists may be modified but cannot exceed core.tuning.NpcTuning.MERCHANT.MAX_WARES and core.tuning.NpcTuning.MERCHANT.MAX_DAILY.

   :param wares: The default wares the merchant NPC has for sale.
   :type wares: list of :class:`InventoryItem`
   :param daily: The daily items the merchant NPC has for sale.
   :type daily: list of :class:`InventoryItem`


.. py:function:: npc_price_notice()

   Called when the NPC prices should be recalculated. NPC prices are calculated in mods.core.npc.getNpcPrice().


.. py:function:: obsidian_created(realm, tilePosition, waterAmount, lavaAmount)

   Called when obsidian is created by having water and lava mix.

   :param Realm realm: The realm that the obsidian was created in.
   :param TileVector tilePosition: The tile position that the obsidian was created in.
   :param int waterAmount: The amount of water that was in the cell when obsidian was created.
   :param int lavaAmount: The amount of lava that was in the cell when obsidian was created.

.. py:function:: pause_change(isPaused)

    Called when the game's paused state changes.

    :param bool isPaused: If the game is paused now or not.


.. py:function:: perform_physics(entities, timestepTime)

   Called when a physics step is about to be performed on a set of entities.

   :param EntitySet entities: The set of entities
   :param int timestepTime: The amount of time the physics simulation is set forward.


.. py:function:: placed_entity(entity)

   Called when an entity is placed down with :py:func:`PlacementHandler.createPlacement`.

   :param Entity entity: The entity that was just placed.


.. py:function:: player_created(player)

   Called when a new character has been created through character creation.

   :param Player player: The newly created player.


.. py:function:: player_joined(player)

   Called immediately when a player joins the world before the player has fully loaded.

   :param Player player: The player who just joined.


.. py:function:: player_left(player)

   Called when a player leaves the world.

   :param Player player: The player who just left.


.. py:function:: player_ready(player)

   Called on the server when it has been notified that the client has received all data for their character. This should be used when needing to send data to client's that is dependent on the player data.

   :param Player player: The player that has just joined and is ready.


.. py:function:: player_respawn(player)

   Called when a player has finished respawning at their attuned crystal.

   :param Player player: The player that has finished respawning.


.. py:function:: player_revive(player)

   Called when a player is revived at their fallen position.

   :param Player player: The player that was just revived.


.. py:function:: player_spawn(player)

   Called when a player has finished joining the game and has spawned in the world.

   :param Player player: The player that just joined.


.. py:function:: populate_treasure(player, chest, groups)

   Called when a treasure chest is about to be populated with loot.

   :param Player player: The player that is opening the treasure chest.
   :param str chest: The type of the chest that is being populated. This is generally the content name of the chest.
   :param groups: The loot groups that the treasure chest will be populated with.
   :type groups: list of core.system.treasure.TreasureActiveGroup


.. py:function:: registration_finished()

   Called after game registration has completely finished. This means all mods have registered and should be initialized.


.. py:function:: setup_body(template, identifier)

    Called when a body content is nearly finished being setup. This allows for manipulation on the body content before it is finalized.

    :param core.template.template.Template template: The body content :ref:`template <content-templates>`.
    :param str identifier: The unique body identifier that is being created.


.. py:function:: tick()

    Called when the game ticks is triggered. This occurs every 3 seconds.


.. py:function:: tile_changed(tileLayer, position, previousId, tileId)

   Called when a tile has changed.

   :param TileLayer tileLayer: The layer that the tile has changed on.
   :param TileVector position: The position of that changed tile.
   :param int previousId: The tile ID of the tile before it was changed.
   :param int tileId: The new tile ID of the changed tile.


.. py:function:: world_created(world)

   Called when the world has been created. This includes when a world is being loaded or connected to.

   :param World world: The created world.


.. py:function:: world_loaded(world)

   Called when the world has finished loading and all systems are ready.

   :param World world: The loaded world.


.. py:function:: world_saved(world, asynchronous)

   Called after the world has been saved. Handle this whenever you need to save some data unassociated.

   :param World world: The world that is being saved.
   :param bool asynchronous: If the world is being saved asynchronously.


.. py:function:: world_unloaded(world)

   Called when The world has been exited and is about to be fully unloaded.

   :param World world: The world being exited.


.. _call-events:

Call Events
-----------

Some events are invoked to support handlers changing the state of things. This is achieved with core.helper.callEvent() which provides a special interface for this.


.. py:function:: callEvent(eventName, player, *args, **kwargs)

    Invokes the named event for both the player entity (player.entity.events[eventName]) as well as a global event (game.event[eventName]).
    Any provided keyword arguments are automatically packed up into a core.helper.AttrDict (results) which is passed to the event handlers and returned.
    Values in results can be modified by other handlers so prefer it over the the provided argument unless you want to use the original value.

    The event handlers resulting signature is: handler(player, results, *args, **kwargs)

    :param str eventName: The name of the event to be invoked.
    :param player: The player to invoke the event on. None can be provided to only invoke a global event. None is still passed to the global event though.
    :type player: Player or None
    :param list args: Arbitrary argument list that the event will be invoked with.
    :param kwargs: Keyword arguments that will be packed in results and passed to the event handler.
    :return: The results that was passed to the event handlers containing the keyword arguments.
    :rtype: core.helper.AttrDict


.. note::

    Remember that all handlers need to include results in the signature!


.. py:function:: accuracy_check(player, attacker, target, accuracy=accuracy, evasion=evasion)

    Called to support accuracy and evasion being manipulated before the accuracy is fully calculated.

    :param Player player: Provided if attacker is a player otherwise None
    :param Entity attacker: The entity performing the attack.
    :param Entity target: The entity being targeted for this attack.
    :param int accuracy: The attacker's accuracy stat.
    :param int evasion: The target's evasion stat.


.. py:function:: apply_damage(player, target, origin, damage=damage, isCritical=isCritical, knockback=knockback)

    Called when damage is about to be applied to an entity.

    :param Player player: Provided if the target is a player otherwise None
    :param Entity target: The entity that will take damage.
    :param Vector origin: The positional origin of the attack.
    :param int damage: The amount of damage that will be taken.
    :param bool isCritical: Whether the damage is considered a critical hit or not.
    :Param int knockback: The amount of knockback the attack has.


.. py:function:: can_hit_tile(player, tileComponent, tilePosition, canHit=canHit)

    Called when checking to see if a player can hit a tile.

    :param Player player: The player trying to hit a tile.
    :param TileComponent tileComponent: The TileComponent of the tile.
    :param TileVector tilePosition: The position of the tile.
    :param bool canHit: Whether the tile can be hit or not.


.. py:function:: completed_dungeon(player, dungeon)

    Called when a player has completed exploring through an entire dungeon.

    :param Player player: The player whom completed the dungeon.
    :param dungeon: The completed dungeon.
    :type dungeon: core.dungeon.Dungeon


.. py:function:: craft_adjust_catalyst(player, chaosCraft, amount=amount)

    Called when the catalyst amount is being modified during chaos crafting.

    :param Player player: The player performing the chaos crafting.
    :param chaosCraft: The container of all chaos crafting data.
    :type chaosCraft: core.ui.craft.ChaosCraft
    :param int amount: The amount the catalysts will be changed by.


.. py:function:: craft_adjust_chaos(player, chaosCraft, amount=amount)

    Called when the chaos amount is being modified during chaos crafting.

    :param Player player: The player performing the chaos crafting.
    :param chaosCraft: The container of all chaos crafting data.
    :type chaosCraft: core.ui.craft.ChaosCraft
    :param int amount: The amount the chaos will be changed by.


.. py:function:: craft_adjust_quality(player, chaosCraft, amount=amount)

    Called when the quality amount is being modified during chaos crafting.

    :param Player player: The player performing the chaos crafting.
    :param chaosCraft: The container of all chaos crafting data.
    :type chaosCraft: core.ui.craft.ChaosCraft
    :param int amount: The amount the quality will be changed by.


.. py:function:: craft_finish(player, craft, quantity, result, item, remainder)

    Called when a player finishes crafting an item.

    :param Player player: The player crafting the item.
    :param CraftComponent craft: The craft component from the crafted item.
    :param int quantity: The quantity of the crafted item.
    :param CraftResult result: The CraftResult used for the crafted item.
    :param InventoryItem item: The crafted item.
    :param int remainder: The quantity of the item that could not fit into the player's inventory.


.. py:function:: craft_quality(player, craft, quality=quality, maxQuality=maxQuality)

    Called to support quality and max quality of crafting items to be manipulated.

    :param Player player: The player crafting the item.
    :param CraftComponent craft: The craft component of the item being crafted.
    :param int quality: The initial calculated quality.
    :param int maxQuality: The maximum value the quality can be. This defaults to 0.


.. py:function:: craft_start(player, craft, quantity, materials)

    Called when starting to craft an item.

    :param Player player: The player crafting the item.
    :param CraftComponent craft: The craft component of the item being crafted.
    :param int quantity: The quantity of the crafted item.
    :param materials: The materials being used to craft the item.
    :type materials: list of :class:`InventoryItem`


.. py:function:: deal_critical_damage(player, attacker, target, data, isCritical=isCritical, criticalFactor=criticalFactor)

    Called when calculating if an attack should be critical or not.

    :param Player player: Provided if attacker is a player otherwise None.
    :param Entity attacker: The entity performing the attack.
    :param Entity target: The entity being targeted for this attack.
    :param data: The data used for the attack.
    :type data: core.combat.AttackData
    :param bool isCritical: Whether the attack should be critical or not.
    :param criticalFactor: The multiplier used on the damage if the attack ends up being critical.


.. py:function:: deal_damage_end(player, attacker, target, data, isCritical, damage)

    Called at the end of calculations when the attacker about to deal damage to the target.

    :param Player player: Provided if attacker is a player otherwise None.
    :param Entity attacker: The entity performing the attack.
    :param Entity target: The entity being targeted for this attack.
    :param data: The data used for the attack.
    :type data: core.combat.AttackData
    :param bool isCritical: Whether the attack should be critical or not.
    :param int damage: The amount of damage that will be dealt.


.. py:function:: deal_damage_start(player, attacker, target, data)

    Called at the start of calculations when the attacker about to deal damage to the target.

    :param Player player: Provided if attacker is a player otherwise None.
    :param Entity attacker: The entity performing the attack.
    :param Entity target: The entity being targeted for this attack.
    :param data: The data used for the attack.
    :type data: core.combat.AttackData


.. py:function:: deal_damage(player, attacker, target, data, isCritical, damage=damage)

    Called towards the end of calculations when the attacker about to deal damage to the target. This supports the amount of damage being changed.

    :param Player player: Provided if attacker is a player otherwise None.
    :param Entity attacker: The entity performing the attack.
    :param Entity target: The entity being targeted for this attack.
    :param data: The data used for the attack.
    :type data: core.combat.AttackData
    :param bool isCritical: Whether the attack should be critical or not.
    :param int damage: The amount of damage that will be dealt.


.. py:function:: descent_damage(player, damage=damage)

    Called when a player will take fall damage.

    :param Player player: The player taking damage.
    :param int damage: The amount of damage the player will take.


.. py:function:: done_casting(player, talent, skillTuning, cost=cost)

    Called when a player finishes casting a skill.

    :param Player player: The player casting a skill.
    :param Talent talent: The talent the spell is from.
    :param skillTuning: The tuning data for the skill (See core.tuning.skill).
    :type skillTuning: core.helper.AttrDict
    :param int cost: The stamina that will be consumed from the skill.


.. py:function:: drop_rate_modifier(player, entity, modifier=modifier)

    Called when calculating the drop rate modifier for a defeated enemy.

    :param player: Always None.
    :param Entity entity: The defeated enemy.
    :param float modifier: The drop rate modifier - 1.0 is 100%.


.. py:function:: enter_dungeon(player, dungeon)

    Called when a player has entered a dungeon.

    :param Player player: The player who entered the dungeon.
    :param dungeon: The dungeon the player entered.
    :type dungeon: core.dungeon.Dungeon


.. py:function:: exit_dungeon(player, dungeon)

    Called when a dungeon is exited regardless of how.

    :param Player player: The player who exited the dungeon.
    :param dungeon: The dungeon the player exited.
    :type dungeon: core.dungeon.Dungeon


.. py:function:: gain_tp(player, talent, amount=amount)

    Called when a player will gain talent points.

    :param Player player: The player gaining the talent points.
    :param Talent talent: The talent the points will be gained for.
    :param int amount: The amount of talent points that will be gained.


.. py:function:: gain_xp(player, amount=amount)

    Called when a player will gain experience points.

    :param Player player: The player gaining the experience points.
    :param int amount: The amount of experience points that will be gained.


.. py:function:: get_research_level(player, craftLevel, bonus=bonus)

    Called when calculating the player's current research level.

    :param Player player: The player the research level is being calculated for.
    :param int craftLevel: The player's craft :class:`Talent` level.
    :param int bonus: The bonus levels that should be added to the research level.


.. py:function:: harvest_power(player, toolComponent, power=power)

    Called when calculating the player's harvest power.

    :param Player player: The player we're calculating the harvest power for.
    :param ToolComponent toolComponent: The component for the tool the player is using.
    :param int power: The amount of harvest power.


.. py:function:: heal_entity(player, user, target, amount=amount)

    Called when an entity is about to be healed.

    :param Player player: Provided if the target is a player otherwise None
    :param Entity user: The user who is healing the target.
    :param Entity target: The entity that will be healed.
    :param int amount: The amount the target will be healed for.


.. py:function:: get_hunter_level(player, skillTuning, level=level)

    Called to support changing the hunter skill level (Ore Hunter or Treasure Hunter).

    :param Player player: The player who is using the hunter skill.
    :param skillTuning: The tuning data for the skill (See core.tuning.skill).
    :type skillTuning: core.helper.AttrDict
    :param int level: The final hunter level that will determine which ore or treasure to reveal.


.. py:function:: kill_entity(player, attacker, target, data, damage, isCritical)

    Called when an entity is killed by an attack.

    :param Player player: Provided if attacker is a player otherwise None.
    :param Entity attacker: The entity performing the attack.
    :param Entity target: The entity that was killed.
    :param data: The data used for the attack.
    :type data: core.combat.AttackData
    :param int damage: The amount of damage that will be dealt.
    :param bool isCritical: Whether the attack should be critical or not.


.. py:function:: npc_price(player, npc, price=price)

    Called when calculating the price of an item an npc is selling.

    :param Player player: The player the item price is being calculated for.
    :param str npc: The content name ('merchant') of the NPC.
    :param int price: The price of the item being determined.


.. py:function:: on_block(player, attacker, target, shieldProficiency, reduction=reduction, threshold=threshold, staminaCost=staminaCost)

    Called when an entity blocks an attack.

    :param Player player: Provided if attacker is a player otherwise None.
    :param Entity attacker: The entity performing the attack.
    :param Entity target: The entity that is being attacked and is blocking.
    :param int shieldProficiency: The shield proficiency of the blocker.
    :param float reduction: The modifier used to reduce the damage - 1.0 is 100%.
    :param int threshold: The maximum amount of damage that can be blocked.
    :param int staminaCost: The amount of stamina to consume from blocking.


.. py:function:: on_jump(player, jumpSpeed=jumpSpeed)

    Called when a player jumps.

    :param Player player: The player that is jumping.
    :param float jumpSpeed: The speed at which the player is jumping.


.. py:function:: on_land(player)

    Called when the player lands on the ground.

    :param Player player: The player landing on the ground.


.. py:function:: on_roll(player, cost=cost)

    Called when a player performs a dodge roll.

    :param Player player: The player that is dodge rolling.
    :param int cost: The amount of stamina to consume from dodge rolling.


.. py:function:: on_sp_recovery(player, time=time)

    Called when a player stamina recovery timer will be reset. Upon expiration the player will begin recovering stamina.

    :param Player player: The player that will begin recovering stamina.
    :param int time: The amount of time (ms) until the player will begin recovering stamina.


.. py:function:: ore_drop(player, droppedPosition=droppedPosition, scavengeLevel=scavengeLevel)

    Called when a player has destroyed an ore tile using a tool.

    :param Player player: The player that destroyed the ore tile.
    :param Vector position: The position of the dropped item which is the center of the destroyed tile.
    :param int scavengeLevel: The level of the player's Scavenge skill.


.. py:function:: player_death(player, damageSource, message=message)

    Called when a player is killed.

    :param Player player: The dead player.
    :param damageSource: The source of the damage that killed the player.
    :type damageSource: core.util.DamageSource
    :param str message: The message that will be displayed.


.. py:function:: research_item_scraps(player, content, scrapAmount=scrapAmount)

    Called when the player researches an item using scraps.

    :param Player player: The player doing the researching.
    :param Content content: The content of the item that is being researched.
    :param int scrapAmount: The number of scraps that will be consumed.


.. py:function:: research_recipe(player, content)

    Called when a new recipe has been learned through researching.

    :param Player player: The player doing the researching.
    :param Content content: The content of the recipe that was researched.


.. py:function:: skill_interrupt(player, skillTuning, interrupt=interrupt)

    Called when the player skill casting will be interrupted.

    :param Player player: The player casting the skill.
    :param skillTuning: The tuning data for the skill (See core.tuning.skill).
    :type skillTuning: core.helper.AttrDict
    :param bool interrupt: Whether the skill should be interrupted or not. Defaults to True.


.. py:function:: start_chaos_craft(player, item, maxCatalysts=maxCatalysts, skills=skills, passives=passives)

    Called when a player starts chaos crafting.

    :param Player player: The player performing chaos crafting.
    :param InventoryItem item: The item that is being crafted.
    :param int maxCatalysts: The maximum number of catalysts that can be used.
    :param skills: List of chaos skills that will be available to the player during this chaos crafting.
    :type skills: list of core.talent.craft.CraftSkill
    :param passives: List of passives that are active during this chaos crafting.
    :type passives: list of core.template.surface.CraftSupportAttribute


.. py:function:: tool_power(player, toolComponent, power=power)

    Called when calculating a tool's power.

    :param Player player: The player we're calculating the tool power for.
    :param ToolComponent toolComponent: The component for the tool the player is using.
    :param int power: The tool's power.


.. py:function:: translate_scroll(player, content)

    Called when the player translates a recipe scroll.

    :param Player player: The player translating the scroll.
    :param Content content: The content of the scroll that is being translated.


.. py:function:: travel_cost(player, travelPlayer, travelCrystal, cost=cost)

    Called when calculating the Way Shard cost to travel to a Way Crystal.

    :param Player player: The player we are calculating the cost for.
    :param travelPlayer: The TravelPlayer that belongs to the player activating the crystal.
    :type travelPlayer: core.system.travel.TravelPlayer
    :param travelCrystal: The TravelCrystal that the cost is being calculated for.
    :type travelCrystal: core.system.travel.TravelCrystal
    :param int cost: The Way Shard cost being calculated to travel to the Way Crystal.


.. _entity-events:

Entity Events
-------------

Below is a list of entity events that are triggered if supported.


.. py:function:: can_collect(player, canCollect)

    When provided this will allow a placed item to provide logic on when it can or cannot be collected.

    :param Player player: The player that is attempting to collect the item.
    :param EventResult canCollect: Stores whether the item can be collected or not using canCollect.result.


.. py:function:: can_place_item(player, entity, item, canPerform)

    When provided this checks to see if an item can be place in or on an entity.

    :param Player player: The player attempting to place the item.
    :param Entity entity: The entity the player is attempting to place the item on.
    :param ToolItem item: The item the player is attempting to place. This is always an item and can be treated as an :class:`InventoryItem`.
    :param EventResult canPerform: Stores whether the item can be placed or not using canPerform.result.

.. py:function:: can_remove_support(entity, realm, tileLayer, tilePosition, shouldCancel)

    When provided this will be called when an attempt to remove a tile is made nearby the entity.

    :param Entity entity: The entity that is nearby the tile.
    :param Realm realm: The realm the entity and tile are in.
    :param TileLayer tileLayer: The layer the tile is being removed from.
    :param TileVector tilePosition: The position of the tile being removed.
    :param EventResult shouldCancel: Whether we should cancel the removal or not.


.. py:function:: close(player, entity)

    Called when an entity with inventory is closed such as a player closing a treasure chest.

    :param Player player: The player that is closing the inventory.
    :param Entity entity: The entity the inventory belongs to.


.. py:function:: clothe(player, entity, position)

    Called when an NPC outfit is being placed onto a mannequin.

    :param Player player: The player clothing the mannequin.
    :param Entity entity: The mannequin that the outfit is being placed on.
    :param Vector position: The cursor position where the player clicked.

.. py:function:: collect(player, entity, position)

    Called when a player attempts to collect an item. This is for special cases such as removing individual crafting station attachments.

    :param Player player: The player collecting the item.
    :param Entity entity: The entity the player is collecting.
    :param Vector position: The cursor position where the player clicked.


.. py:function:: interact(player, entity, position)

    Called when a player interacts with an entity.

    :param Player player: The player interacting with the entity.
    :param Entity entity: The entity the player is interacting with.
    :param Vector position: The cursor position where the player clicked.

.. py:function:: place_item(player, entity, position)

    Called when a player places an item in or on an entity. Use player.grabbed.item (:class:`ToolItem`) for the item being placed.

    :param Player player: The player placing the item.
    :param Entity entity: The entity the player is placing the item on.
    :param Vector position: The cursor position where the player clicked.


.. py:function:: remove_support(entity, realm, tileLayer, tilePosition, forced, shouldCancel)

    Called when the player is about to remove a tile that the entity is using as support.

    :param Entity entity: The entity that is nearby the tile.
    :param Realm realm: The realm the entity and tile are in.
    :param TileLayer tileLayer: The layer the tile is being removed from.
    :param TileVector tilePosition: The position of the tile being removed.
    :param bool forced: Whether the tile is being forcefully removed.
    :param EventResult shouldCancel: Whether we should cancel the removal or not. This is ignored if the removal is forced.


.. py:function:: use_gadget(player, realm, entity, position)

    Called when a player uses a gadget.

    :param Player player: The player using the gadget.
    :param Realm realm: The realm that the player is in.
    :param Entity entity: The entity of the gadget being used.
    :param Vector position: The cursor position where the player clicked.

Player Events
-------------

Below is a list of events that are directly called on the player's :class:`EventComponent`.

.. py:function:: cast_spell(spellTuning)

    Called when the player casts a spell.

    :param spellTuning: The tuning data for the spell (See core.tuning.skill).
    :type spellTuning: core.helper.AttrDict


.. py:function:: claim_imbue_output(item)

    Called when the player claims the output item from an imbuing chamber.

    :param InventoryItem item: The output item.


.. py:function:: completed_horde_realm(realm)

    Called when the player completes a horde realm.

    :param Realm realm: The horde realm that the player completed.


.. py:function:: deal_damage_invisible(target, data, isCritical, damage)

    Called when the player deals damage to a target while invisible.

    :param Entity target: The target of the player's attack.
    :param data: The data used for the attack.
    :type data: core.combat.AttackData
    :param bool isCritical: Whether the attack should be critical or not.
    :param int damage: The amount of damage that will be dealt.


.. py:function:: equip_craft_station(entity, unequippedItem, item)

    Called when the player equip an item on a crafting station.

    :param Entity entity: The crafting station entity that is being equipped.
    :param InventoryItem unequippedItem: The item that was unequipped from the crafting station. This will be empty if no item was equipped in the slot.
    :param GrabbedItem item: The item being equipped to the crafting station.


.. py:function:: expertise_level(level)

    Called when the player's Expertise skill level is changed.

    :param int level The current Expertise level.


.. py:function:: grabbed_enemy(player, hook, grapplerData, enemies)

    Called when the player grabs an entity with a grappling hook.

    :param Player player: The player grabbing the entity.
    :param Entity hook: The entity of the grappling hook that is being shot out.
    :param grapplerData: Container of all the grappler data. See core.template.grappler.Grappler for more details.
    :type grapplerData: core.helper.AttrDict
    :param enemies: The entities that were grabbed.
    :type enemies: List of Entity


.. py:function:: realm_change(player, previousRealm, realm)

    Called when the player traveling to another realm.

    :param Player player: The player traveling to another realm.
    :param Realm previousRealm: The realm the player is traveling from.
    :param Realm realm: The realm the player is traveling to.


.. py:function:: use_delay(itemEntity, delay)

    Called when the player uses an item and the player's use delay timer is about to be set.

    :param Entity itemEntity: The entity of the item being used.
    :param EventArg delay: The amount of time the use delay timer will be set to.


.. py:function:: used_item(itemEntity, quantity)

    Called when the player uses an item.

    :param Entity itemEntity: The entity of the item being used.
    :param int quantity: The current quantity of the item that is being used.



Equipment Events
----------------

Below is a list of events that are called on pieces of equipment. All equipment attributes can be found in core.item.armor.attribute module.


.. py:function:: charged(player, itemEntity, equipmentSlot, clientInput, inputType, position)

    Called on the item with a ChargedAttackAttribute when it is being charged.

    :param Player player: The player charging the item.
    :param Entity itemEntity: The entity of the item being used.
    :param str equipmentSlot: The equipment slot the item is in.
    :param clientInput: The input for the player.
    :type clientInput: core.system.input.ClientInput
    :param inputType: The type of input used.
    :type inputType: core.util.InputTypes
    :param Vector position: The cursor position of the player.


.. py:function:: final_combo(player, itemEntity)

    Called on the item when it performs the last attack in its attack combo.

    :param Player player: The player using the item.
    :param Entity itemEntity: The entity of the item being used.


.. py:function:: hit_ally(player, target, itemEntity, entity)

    Called when a wand projectile hits an ally.

    :param Player player: The player using the item.
    :param Entity target: The ally that was hit.
    :param Entity itemEntity: The entity of the item being used.
    :param Entity entity: The entity of the wand projectile.


.. py:function:: post_weapon_use(player, itemEntity)

    Called after a weapon is used.

    :param Player player: The player using the item.
    :param Entity itemEntity: The entity of the weapon used.


.. py:function:: projectile_fired(entity)

    Called when a projectile is fired from a bow or wand.

    :param Entity entity: The entity of the projectile shot.
