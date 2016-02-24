.. _siege.achievement:

siege.achievement
==================

Achievement
-----------------------------------
.. class:: Achievement

   

   .. data:: AColdDish = siege.achievement.Achievement.AColdDish

   .. data:: Aerlike = siege.achievement.Achievement.Aerlike

   .. data:: AncestorDefiler = siege.achievement.Achievement.AncestorDefiler

   .. data:: AncestrialProtection = siege.achievement.Achievement.AncestrialProtect...

   .. data:: Assassination = siege.achievement.Achievement.Assassination

   .. data:: BarrierSmasher = siege.achievement.Achievement.BarrierSmasher

   .. data:: BloodSweatAndTears = siege.achievement.Achievement.BloodSweatAndTears

   .. data:: BreathOfChaosAer = siege.achievement.Achievement.BreathOfChaosAer

   .. data:: ChaosPatterns = siege.achievement.Achievement.ChaosPatterns

   .. data:: Clutch = siege.achievement.Achievement.Clutch

   .. data:: CorruptedDreams = siege.achievement.Achievement.CorruptedDreams

   .. data:: DreamEater = siege.achievement.Achievement.DreamEater

   .. data:: DressedToKill = siege.achievement.Achievement.DressedToKill

   .. data:: DungeonDelver = siege.achievement.Achievement.DungeonDelver

   .. data:: EndOfAJourney = siege.achievement.Achievement.EndOfAJourney

   .. data:: FallingWithStyle = siege.achievement.Achievement.FallingWithStyle

   .. data:: FourCornersOfCrea = siege.achievement.Achievement.FourCornersOfCrea

   .. data:: GatherNoMoss = siege.achievement.Achievement.GatherNoMoss

   .. data:: GetOverHere = siege.achievement.Achievement.GetOverHere

   .. data:: HighDive = siege.achievement.Achievement.HighDive

   .. data:: ImbuedRemnants = siege.achievement.Achievement.ImbuedRemnants

   .. data:: ImproveYourCore = siege.achievement.Achievement.ImproveYourCore

   .. data:: KnockingAtTheGate = siege.achievement.Achievement.KnockingAtTheGate

   .. data:: KnowItAll = siege.achievement.Achievement.KnowItAll

   .. data:: KnowledgeIsPower = siege.achievement.Achievement.KnowledgeIsPower

   .. data:: LootHoarder = siege.achievement.Achievement.LootHoarder

   .. data:: LoreHunter = siege.achievement.Achievement.LoreHunter

   .. data:: LostInTranslation = siege.achievement.Achievement.LostInTranslation

   .. data:: MouthFoamer = siege.achievement.Achievement.MouthFoamer

   .. data:: NeverAlone = siege.achievement.Achievement.NeverAlone

   .. data:: NoLongerAlone = siege.achievement.Achievement.NoLongerAlone

   .. data:: OneString = siege.achievement.Achievement.OneString

   .. data:: OnesShield = siege.achievement.Achievement.OnesShield

   .. data:: OnesSpear = siege.achievement.Achievement.OnesSpear

   .. data:: ParaGone = siege.achievement.Achievement.ParaGone

   .. data:: PerfectLanding = siege.achievement.Achievement.PerfectLanding

   .. data:: PerishWithTheSword = siege.achievement.Achievement.PerishWithTheSword

   .. data:: PowerOverwhelming = siege.achievement.Achievement.PowerOverwhelming

   .. data:: SleepingWithTheFishes = siege.achievement.Achievement.SleepingWithTheF...

   .. data:: Smithereens = siege.achievement.Achievement.Smithereens

   .. data:: Spellslinger = siege.achievement.Achievement.Spellslinger

   .. data:: Sylicmage = siege.achievement.Achievement.Sylicmage

   .. data:: TearDownThisWall = siege.achievement.Achievement.TearDownThisWall

   .. data:: TheJourneyBegins = siege.achievement.Achievement.TheJourneyBegins

   .. data:: TisAFleshWound = siege.achievement.Achievement.TisAFleshWound

   .. data:: ValiantEffort = siege.achievement.Achievement.ValiantEffort

   .. data:: WeaponMaster = siege.achievement.Achievement.WeaponMaster

   .. data:: WellDone = siege.achievement.Achievement.WellDone

   .. data:: WellPrepared = siege.achievement.Achievement.WellPrepared

   .. data:: Xenocide = siege.achievement.Achievement.Xenocide

AchievementSystem
-----------------------------------
.. class:: AchievementSystem

   

   .. method:: achieve( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Player`

      :param arg3: 

      :type arg3: :class:`Achievement`

   .. method:: disable( )

      

   .. method:: getStat( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: int

   .. method:: handleNetworkReset( server, client)

      If client is not the server then register the handler for this ParticleSystem


      :param server:  A :class:`Server` connection


      :type server: :class:`Server`

      :param client:  A :class:`Client` connection


      :type client: :class:`Client`

   .. method:: hasAchieved( arg2, arg3)

      

      :param arg2: 

      :type arg2: :class:`Player`

      :param arg3: 

      :type arg3: :class:`Achievement`

      :rtype: bool

   .. method:: incrementStat( arg2)

      

      :param arg2: 

      :type arg2: str

      :rtype: bool

   .. method:: isEnabled( )

      

      :rtype: bool

   .. method:: setStat( arg2, arg3)

      

      :param arg2: 

      :type arg2: str

      :param arg3: 

      :type arg3: int

      :rtype: bool

   .. attribute:: onAchieve

      

   .. attribute:: onReady

      

