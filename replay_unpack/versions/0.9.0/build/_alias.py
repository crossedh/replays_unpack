g_aliasMap = {'BATTLE_LOGIC_STATE': ['FIXED_DICT', [('attentionMarkers', ['ARRAY', 'ATTENTION_MARKER_STATE']), ('clientAnimations', 'CLIENT_ANIMATION_STATE'), ('controlPoints', ['ARRAY', 'CONTROL_POINT_STATE']), ('entityStates', ['ARRAY', 'ENTITY_STATE_STATE']), ('expectedActions', 'EXPECTED_ACTION_STATE'), ('weather', 'WEATHER_STATE'), ('keyObjects', ['ARRAY', 'KEY_OBJECT_STATE']), ('missions', 'MISSIONS_STATE'), ('resources', ['ARRAY', 'RESOURCE_STATE']), ('successStoryProgress', ['ARRAY', 'SUCCESS_STORY_PROGRESS_STATE']), ('screenplayMessage', 'SCREENPLAY_MESSAGE_STATE'), ('tasks', ['ARRAY', 'TASKS_STATE']), ('minefields', ['ARRAY', 'MINEFIELD_STATE']), ('entities', ['ARRAY', 'BATTLE_LOGIC_ENTITY_STATE']), ('effects', ['ARRAY', 'EFFECT_STATE']), ('drop', 'DROP_STATE')], False], 'PLAYER_DIGEST': ['FIXED_DICT', [('dbId', 'DB_ID'), ('nickname', 'STRING'), ('accLevel', 'UINT8'), ('rankInfo', 'UINT32'), ('lastGameTime', 'UINT32'), ('dogTag', 'STRING'), ('isTeamKiller', 'UINT8'), ('masterId', 'UINT8'), ('suspended', 'UINT8')], False], 'PLAYER_ID': 'INT32', 'MODULE_ID': 'STRING', 'PLANE_PROJECTILE': ['FIXED_DICT', [('shotID', 'UINT16'), ('impactPoint', 'VECTOR3')], False], 'INDIVIDUAL_TASK_DEF': ['FIXED_DICT', [('entityId', 'ENTITY_ID'), ('paramsId', 'GAMEPARAMS_ID')], False], 'TEAM_SCORE': ['FIXED_DICT', [('teamId', 'TEAM_ID'), ('score', 'UINT16')], False], 'COUNTDOWN_INFO': ['ARRAY', 'INT32', 2], 'MASTER_ID': 'UINT32', 'PLANE_WAYPOINT': ['FIXED_DICT', [('position', 'VECTOR3'), ('yaw', 'FLOAT'), ('pitch', 'INT8'), ('time', 'INT16'), ('type', 'INT8')], False], 'TEAMS_DEF': ['FIXED_DICT', [('detonation', 'BOOL'), ('friendlyFire', 'BOOL'), ('teams', ['ARRAY', 'TEAM_INFO'])], False], 'CLIENT_STAT_INFO': ['FIXED_DICT', [('average', 'FLOAT'), ('minimal', 'FLOAT'), ('maximal', 'FLOAT'), ('tenpercent', 'FLOAT'), ('median', 'FLOAT'), ('ninetypercent', 'FLOAT'), ('peakram', 'UINT32'), ('graphpreset', 'UINT8'), ('graphpresetname', 'STRING'), ('msaamode', 'UINT8'), ('renderpipeline', 'UINT8'), ('shadowsquality', 'UINT8'), ('lightingquality', 'UINT8'), ('particlequality', 'UINT8'), ('seareflectionquality', 'UINT8'), ('texturequality', 'UINT8'), ('texturecompression', 'UINT8'), ('texturefiltering', 'UINT8'), ('soundpreset', 'UINT8'), ('particlepreset', 'UINT8'), ('softparticles', 'UINT8'), ('gamelogicpreset', 'UINT8'), ('lowqualitygui', 'UINT8'), ('miscsetting', 'UINT8'), ('terrainlod', 'UINT8'), ('terrainmeshresolution', 'UINT8'), ('terrainlightingquality', 'UINT8'), ('decalsquality', 'UINT8'), ('postprocessing', 'UINT8'), ('fxaaquality', 'UINT8'), ('volumetricclouds', 'UINT8'), ('farplane', 'UINT8'), ('seasimulationquality', 'UINT8'), ('flagsquality', 'UINT8'), ('forestquality', 'UINT8'), ('objectlod', 'UINT8'), ('windowed', 'UINT8'), ('resolution', 'STRING')], False], 'DB_ID': 'INT64', 'TORPEDOES_PACK': ['FIXED_DICT', [('paramsID', 'GAMEPARAMS_ID'), ('ownerID', 'PLAYER_ID'), ('salvoID', 'INT32'), ('skinID', 'GAMEPARAMS_ID'), ('torpedoes', ['ARRAY', 'TORPEDO'])], False], 'AIR_DEFENCE_AURA': ['FIXED_DICT', [('id', 'INT8'), ('enabled', 'BOOL')], False], 'PLAYER_MODE': ['FIXED_DICT', [('playerModeType', 'UINT8'), ('observedTeamId', 'TEAM_ID')], False], 'PRE_BATTLE_SENDER_DEF': ['FIXED_DICT', [('senderName', 'STRING'), ('senderId', 'PLAYER_ID'), ('senderDBID', 'DB_ID'), ('senderLevel', 'UINT32'), ('senderRankInfo', 'UINT32'), ('isAbuser', 'BOOL'), ('clanID', 'DB_ID'), ('clanTag', 'UNICODE_STRING'), ('clanColor', 'UINT32')], True], 'PRIVATE_BATTLE_LOGIC_STATE': ['FIXED_DICT', [('individualTasks', ['ARRAY', 'INDIVIDUAL_TASK_STATE']), ('modifiers', ['ARRAY', 'MODIFIER_STATE']), ('screenplayMessage', 'SCREENPLAY_MESSAGE_STATE')], False], 'DAMAGES': ['FIXED_DICT', [('vehicleID', 'ENTITY_ID'), ('damage', 'FLOAT')], False], 'TEAMSLIST': ['ARRAY', 'PLAYERS_DEFS'], 'EFFECT_STATE': ['FIXED_DICT', [('id', 'INT16'), ('name', 'STRING'), ('position', 'VECTOR3'), ('yaw', 'FLOAT')], False], 'EXPECTED_ACTION_STATE': ['FIXED_DICT', [('actionId', 'STRING')], True], 'GLOBAL_WEATHER_STATE': ['FIXED_DICT', [('param', 'GAMEPARAMS_ID'), ('item', 'GLOBAL_WEATHER_ITEM'), ('notification', 'GLOBAL_WEATHER_NOTIFICATION')], False], 'WEATHER_STATE': ['FIXED_DICT', [('mainWeather', 'GAMEPARAMS_ID'), ('globalWeather', 'GLOBAL_WEATHER_STATE'), ('localWeather', ['ARRAY', 'LOCAL_WEATHER_STATE'])], False], 'BATTLE_LOGIC_DEBUG_TEXT': ['FIXED_DICT', [('layer', 'STRING'), ('channels', ['ARRAY', 'BATTLE_LOGIC_DEBUG_CHANNEL'])], False], 'ARENA_STATE': ['FIXED_DICT', [('arenaUniqueId', 'INT64'), ('teamBuildTypeId', 'INT8'), ('preBattlesInfo', 'BLOB'), ('playersStates', 'BLOB'), ('buildingsInfo', 'BLOB')], False], 'SUPPRESS_BUILDING_MISSION_STATE': ['FIXED_DICT', [('reward', 'INT16'), ('penalty', 'INT16'), ('buildingType', 'STRING')], False], 'VISIBILITY_BY_CLIENTS': ['ARRAY', 'AVATAR_ID'], 'PLAYER_CLAN_INFO': ['FIXED_DICT', [('clanID', 'DB_ID'), ('clanTag', 'UNICODE_STRING'), ('clanColor', 'UINT32')], True], 'PLANE_PROJECTILE_PACK': ['FIXED_DICT', [('bombParamsId', 'GAMEPARAMS_ID'), ('squadronId', 'PLANE_ID'), ('squadronToTarget', 'VECTOR3'), ('fallTime', 'FLOAT'), ('projectiles', ['ARRAY', 'PLANE_PROJECTILE'])], False], 'KEY_OBJECT_STATE': ['FIXED_DICT', [('name', 'STRING'), ('type', 'UINT8'), ('ownerId', 'ENTITY_ID'), ('maxValue', 'FLOAT'), ('curValue', 'FLOAT')], True], 'BACKUPED_PROPERTY': ['FIXED_DICT', [('data', 'PYTHON')], False], 'RESOURCE_STATE': ['FIXED_DICT', [('resourceType', 'UINT8'), ('amountByEntities', ['ARRAY', 'RESOURCE_RECORD'])], True], 'CLIENT_ANIMATION_STATE': ['FIXED_DICT', [('type', 'INT8'), ('targetType', 'INT8'), ('ids', ['ARRAY', 'ENTITY_ID']), ('indexes', ['ARRAY', 'UINT16'])], True], 'DIVISION_SEEKER_DEF': ['FIXED_DICT', [('dbid', 'DB_ID'), ('name', 'STRING'), ('level', 'UINT32'), ('rankInfo', 'UINT32'), ('isAbuser', 'BOOL'), ('regionID', 'STRING'), ('comment', 'STRING'), ('clanInfo', 'PLAYER_CLAN_INFO'), ('dogTag', ['ARRAY', 'GAMEPARAMS_ID'])], False], 'TRAINING_ROOM_PROPERTIES': ['FIXED_DICT', [('mapId', 'INT32'), ('scenario', 'UNICODE_STRING'), ('teamSize', 'INT32'), ('weatherId', 'INT32'), ('duration', 'INT32'), ('commandersManagement', 'BOOL'), ('isClosed', 'BOOL'), ('description', 'UNICODE_STRING'), ('shipRestrictions', 'SHIP_RESTRICTIONS'), ('hideShips', 'BOOL'), ('passwordAction', 'INT8'), ('password', 'UNICODE_STRING'), ('observersAvailable', 'BOOL')], False], 'DROP_PLANE_STATE': ['FIXED_DICT', [('direction', 'VECTOR2'), ('params', 'GAMEPARAMS_ID'), ('height', 'FLOAT')], True], 'EXPLOSION': ['FIXED_DICT', [('pos', 'VECTOR3'), ('paramsID', 'GAMEPARAMS_ID'), ('hitType', 'UINT8')], False], 'KILL_SPECIFIC_SHIP_MISSION_STATE': ['FIXED_DICT', [('reward', 'INT16'), ('penalty', 'INT16'), ('shipType', 'STRING')], False], 'MSGPACK_BLOB': 'USER_TYPE', 'RANK_BATTLES_PLAYER_INFO': ['FIXED_DICT', [('seasonId', 'UINT16'), ('stars', 'UINT8'), ('rank', 'UINT8'), ('rankBest', 'UINT8'), ('league', 'UINT8'), ('stage', 'UINT8'), ('startRank', 'UINT8')], False], 'ZONE_TARGET_PRIORITY_INFO': ['FIXED_DICT', [('zoneCenter', 'VECTOR3'), ('zoneRadius', 'FLOAT')], False], 'REPLAY_DATA': ['FIXED_DICT', [('battleID', 'ARENA_UNIQUE_ID'), ('permitDBIDs', ['ARRAY', 'DB_ID']), ('metadata', 'MSGPACK_BLOB'), ('readyReplay', 'BLOB')], False], 'BUBBLE': ['FIXED_DICT', [('position', 'VECTOR3'), ('activationDelay', 'FLOAT')], False], 'VISION': ['ARRAY', 'ENTITY_ID'], 'MAP_BORDER': ['FIXED_DICT', [('paramsId', 'GAMEPARAMS_ID'), ('position', 'VECTOR3')], True], 'MINE_STATE': ['FIXED_DICT', [('position', 'VECTOR2'), ('id', 'UINT32')], False], 'MODIFIER_STATE': ['FIXED_DICT', [('paramsId', 'GAMEPARAMS_ID'), ('level', 'INT8'), ('startTime', 'INT16'), ('endTime', 'INT16')], False], 'PRE_BATTLE_INVITE_DEF': ['FIXED_DICT', [('preBattleId', 'OBJECT_ID'), ('preBattleType', 'INT8'), ('inviteType', 'INT8'), ('expirationTime', 'UINT32'), ('creatorInfo', 'PRE_BATTLE_CREATOR_DEF'), ('senderInfo', 'PRE_BATTLE_SENDER_DEF'), ('state', 'STRING'), ('regionID', 'STRING')], False], 'TARGET_ID': 'INT64', 'LINKAGE_FRAGMENTS': ['FIXED_DICT', [('serviceName', 'STRING'), ('mailBoxes', ['ARRAY', 'MAILBOX'])], True], 'WEAPON_TYPE': 'UINT8', 'ENTITY_EFFECT_STATE': ['FIXED_DICT', [('id', 'INT16'), ('name', 'STRING'), ('node', 'STRING')], False], 'GENERIC_MESSENGER_ARGS': ['FIXED_DICT', [('int32Arg1', 'INT32'), ('int64Arg1', 'INT64'), ('strArg1', 'STRING'), ('int64ListArg1', 'DB_ID_LIST')], False], 'SHIP_CONFIG': ['FIXED_DICT', [('shipId', 'SHIP_ID'), ('cd', 'BLOB')], True], 'EVALUATION_DEF': ['FIXED_DICT', [('userDBID', 'DB_ID'), ('createTS', 'INT32'), ('subjectDBID', 'DB_ID'), ('evaluationType', 'INT8'), ('topic', 'INT8'), ('subjectKind', 'INT8'), ('arenaUniqueID', 'DB_ID'), ('clusterID', 'MASTER_ID')], False], 'REPLAY_METADATA_LIST': ['ARRAY', 'REPLAY_METADATA'], 'INDIVIDUAL_TASK_STATE': ['FIXED_DICT', [('status', 'UINT8'), ('paramsId', 'GAMEPARAMS_ID'), ('currentValues', ['ARRAY', 'UINT8']), ('attentionMarkers', ['ARRAY', 'ATTENTION_MARKER_STATE'])], False], 'AIR_THREAT': ['FIXED_DICT', [('squadronID', 'INT32'), ('planeParamsID', 'GAMEPARAMS_ID')], False], 'SHIP_RESTRICTIONS': ['FIXED_DICT', [('totalShips', 'INT32'), ('minShips', 'INT32'), ('concreteShips', ['ARRAY', 'INT32']), ('concreteOnly', 'BOOL'), ('excludeShips', ['ARRAY', 'INT32']), ('shipTypes', ['ARRAY', 'INT8']), ('shipLevels', ['ARRAY', 'INT8']), ('nations', ['ARRAY', 'INT8']), ('shipClassesForFilters', ['ARRAY', 'INT32']), ('minLimitsForFilters', ['ARRAY', 'INT32']), ('maxLimitsForFilters', ['ARRAY', 'INT32'])], True], 'CAPTURE_LOGIC_STATE': ['FIXED_DICT', [('captureProgress', 'FLOAT'), ('timeLeft', 'FLOAT'), ('teamId', 'TEAM_ID')], True], 'CAMPAIGN_TASK_ID': 'UINT32', 'ENTITY_STATE_STATE': ['FIXED_DICT', [('ownerId', 'ENTITY_ID'), ('name', 'UINT8'), ('status', 'UINT8'), ('info', 'STRING')], True], 'LOCAL_WEATHER_STATE': ['FIXED_DICT', [('name', 'STRING'), ('position', 'VECTOR2'), ('radius', 'FLOAT'), ('paramsId', 'UINT32')], False], 'SCREENPLAY_MESSAGE_STATE': ['FIXED_DICT', [('message', 'STRING'), ('flag', 'UINT8')], True], 'CAPTURE_CONTROL_POINT_MISSION_STATE': ['FIXED_DICT', [('reward', 'INT16'), ('penalty', 'INT16'), ('cpIndices', ['ARRAY', 'UINT8'])], False], 'COLLISION_INFO_BASE': ['FIXED_DICT', [('where', 'UINT8'), ('hitPos', 'VECTOR3'), ('hitDir', 'VECTOR3'), ('normal', 'VECTOR3'), ('isAlive', 'BOOL'), ('entityId', 'ENTITY_ID'), ('matId', 'INT32'), ('isInside', 'BOOL')], False], 'DROP_STATE': ['FIXED_DICT', [('dropItems', ['ARRAY', 'DROP_ITEM_STATE']), ('plane', 'DROP_PLANE_STATE')], True], 'TEAM_INFO': ['FIXED_DICT', [('teamId', 'TEAM_ID'), ('detonation', 'BOOL'), ('friendlyFire', 'BOOL')], False], 'REPLAY_METADATA': ['FIXED_DICT', [('replayId', 'STRING'), ('mapName', 'UINT16'), ('gameType', 'INT8'), ('gameMode', 'INT8'), ('dateTime', 'UINT32'), ('version', 'STRING'), ('networkInterface', 'STRING')], False], 'PRE_BATTLE_DEF': ['FIXED_DICT', [('id', 'OBJECT_ID'), ('creatorDBID', 'DB_ID'), ('ownerId', 'PLAYER_ID'), ('ownerName', 'STRING'), ('ownerClanID', 'DB_ID'), ('description', 'UNICODE_STRING'), ('battleDef', 'BATTLE_DEF'), ('playersLimit', 'INT8'), ('playersCount', 'INT8'), ('invitedCount', 'UINT16'), ('preBattleType', 'INT8'), ('isLocked', 'BOOL'), ('isInBattle', 'BOOL'), ('selectedQueueType', 'INT32'), ('nonClanMembersCount', 'INT8'), ('clanSquadId', 'INT8'), ('extraInfo', 'PYTHON')], True], 'ORDER_DEF': ['FIXED_DICT', [('id', 'UINT8'), ('uniqueID', 'UINT8'), ('primaryGoal', 'GOAL_DEF'), ('secondaryGoal', 'GOAL_DEF')], False], 'HOLD_CONTROL_POINT_MISSION_STATE': ['FIXED_DICT', [('reward', 'INT16'), ('penalty', 'INT16'), ('cpIndices', ['ARRAY', 'UINT8']), ('period', 'INT16')], False], 'SHOTS_PACK': ['FIXED_DICT', [('paramsID', 'GAMEPARAMS_ID'), ('ownerID', 'PLAYER_ID'), ('salvoID', 'INT32'), ('shots', ['ARRAY', 'SHOT'])], False], 'SUCCESS_STORY_PROGRESS_STATE': ['FIXED_DICT', [('name', 'STRING'), ('enabled', 'BOOL'), ('type', 'UINT8'), ('progress', 'UINT8'), ('targetProgress', 'UINT8'), ('state', 'UINT8'), ('invadersNumber', 'UINT8'), ('defendersNumber', 'UINT8'), ('watchedShipId', 'ENTITY_ID'), ('watchedTaskName', 'STRING')], True], 'ATTENTION_MARKER_STATE': ['FIXED_DICT', [('name', 'STRING'), ('markerType', 'UINT8'), ('subType', 'UINT8'), ('caption', 'STRING'), ('position', ['FIXED_DICT', [('x', 'FLOAT'), ('z', 'FLOAT')], True]), ('ownerType', 'UINT8'), ('ownerId', 'ENTITY_ID'), ('linkedTaskName', 'STRING')], True], 'MINIMAPINFO': ['ARRAY', 'MINIMAP_USER_INFO'], 'TASKS_STATE': ['FIXED_DICT', [('category', 'UINT8'), ('name', 'STRING'), ('status', 'UINT8'), ('startTime', 'UINT32'), ('currentValue', 'UINT16'), ('targetValue', 'UINT16'), ('type', 'UINT8'), ('targetValueAchieved', 'UINT8'), ('closeTime', 'UINT8'), ('taskPool', 'STRING'), ('showOnHUD', 'BOOL')], True], 'PLAYERS_MBS': ['ARRAY', 'MAILBOX'], 'CREW_MODIFIERS_COMPACT_PARAMS': ['FIXED_DICT', [('effectiveness', 'FLOAT'), ('learnedSkills', 'UINT64'), ('paramsId', 'UINT32')], False], 'DEPTHCHARGESHOT': ['FIXED_DICT', [('paramsID', 'GAMEPARAMS_ID'), ('pos', 'VECTOR3'), ('dir', 'VECTOR3'), ('ownerID', 'PLAYER_ID'), ('salvoID', 'INT32'), ('shotID', 'UINT16'), ('serverTimeLeft', 'FLOAT')], False], 'VISIBILITY_BY_TEAM': ['ARRAY', 'TEAM_ID'], 'BUBBLE_PACK': ['FIXED_DICT', [('auraId', 'INT8'), ('bubbles', ['ARRAY', 'BUBBLE'])], False], 'PRE_BATTLE_CREATOR_DEF': ['FIXED_DICT', [('id', 'DB_ID'), ('info', 'PYTHON')], True], 'DROP_ITEM_STATE': ['FIXED_DICT', [('id', 'INT8'), ('paramsId', 'GAMEPARAMS_ID'), ('zoneName', 'STRING'), ('startTime', 'INT16'), ('isContested', 'BOOL'), ('captureLogicState', 'CAPTURE_LOGIC_STATE'), ('dropVisualId', 'GAMEPARAMS_ID')], False], 'SHOTKILLS_PACK': ['FIXED_DICT', [('ownerID', 'PLAYER_ID'), ('hitType', 'UINT8'), ('kills', ['ARRAY', 'SHOTKILL'])], False], 'SHOTKILL': ['FIXED_DICT', [('pos', 'VECTOR3'), ('shotID', 'UINT16')], False], 'BATTLE_LOGIC_ENTITY_STATE': ['FIXED_DICT', [('id', 'ENTITY_ID'), ('className', 'STRING'), ('name', 'STRING'), ('teamId', 'TEAM_ID')], False], 'ATBA_TARGETS': ['ARRAY', 'UINT32'], 'GAMEPARAMS_ID': 'UINT32', 'PREREQUISITE_SHIP_DATA': ['FIXED_DICT', [('shipParamsId', 'GAMEPARAMS_ID'), ('maxUpgrades', 'BOOL'), ('camoParamsId', 'GAMEPARAMS_ID')], False], 'RESTART_INFO': 'USER_TYPE', 'MISSIONS_STATE': ['FIXED_DICT', [('hold', ['ARRAY', 'HOLD_CONTROL_POINT_MISSION_STATE']), ('capture', ['ARRAY', 'CAPTURE_CONTROL_POINT_MISSION_STATE']), ('suppress', ['ARRAY', 'SUPPRESS_BUILDING_MISSION_STATE']), ('kill', ['ARRAY', 'KILL_SPECIFIC_SHIP_MISSION_STATE']), ('teamsScore', ['ARRAY', 'TEAM_SCORE']), ('teamWinScore', 'UINT16'), ('teamLoseScore', 'UINT16')], True], 'RANK_BATTLES_DENY_REASON': ['FIXED_DICT', [('dbid', 'DB_ID'), ('reason', 'UINT16')], False], 'BOOL': 'UINT8', 'GLOBAL_WEATHER_NOTIFICATION': ['FIXED_DICT', [('param', 'GAMEPARAMS_ID'), ('time', 'INT16')], True], 'PRESET_ID': 'UINT8', 'WEATHER_LOGIC_PARAMS': ['FIXED_DICT', [('visibilityFactor', 'FLOAT'), ('visibilityFactorByPlane', 'FLOAT'), ('maxVisibilityDistance', 'FLOAT'), ('maxVisibilityDistanceByPlane', 'FLOAT'), ('mgVisibilityTime', 'FLOAT'), ('smokeVisibilityTime', 'FLOAT'), ('GMIdealRadius', 'FLOAT'), ('GSIdealRadius', 'FLOAT'), ('AAMaxDist', 'FLOAT'), ('shootShift', 'FLOAT'), ('speedCoef', 'FLOAT'), ('airplanesSpeed', 'FLOAT'), ('burnDamage', 'FLOAT'), ('burnTime', 'FLOAT'), ('smokeLifeTime', 'FLOAT'), ('maxShipVisionDistance', 'FLOAT'), ('maxPlaneVisionDistance', 'FLOAT'), ('bad', 'FLOAT'), ('transparency', 'FLOAT')], False], 'MINIMAP_USER_INFO': ['FIXED_DICT', [('vehicleID', 'UINT32'), ('packedData', 'UINT32')], False], 'INTERACTIVE_ZONE_ENTITY_STATE': ['FIXED_DICT', [('forOwner', 'UINT8'), ('forAllies', 'UINT8'), ('forEnemies', 'UINT8')], False], 'SQUADRON_STATE': ['FIXED_DICT', [('planeID', 'PLANE_ID'), ('skinID', 'GAMEPARAMS_ID'), ('isActive', 'BOOL'), ('numBombs', 'INT8'), ('catapultState', 'INT8'), ('numPlanes', 'UINT8'), ('formation', 'INT8'), ('position', 'VECTOR3'), ('yaw', 'FLOAT'), ('throttleMode', 'INT8'), ('turnMode', 'INT8'), ('turnDirection', 'INT8'), ('attackState', 'UINT8')], False], 'READY_CLIENTS_LIST': ['ARRAY', 'ENTITY_ID'], 'ENTITY_ID': 'INT32', 'MINEFIELD_STATE': ['FIXED_DICT', [('id', 'UINT32'), ('position', 'VECTOR2'), ('length', 'FLOAT'), ('width', 'FLOAT'), ('yaw', 'FLOAT'), ('depth', 'FLOAT'), ('mineType', 'GAMEPARAMS_ID'), ('mines', ['ARRAY', 'MINE_STATE']), ('enableDebugDraw', 'BOOL')], False], 'SHIP_ID': 'UINT32', 'TEAM_ID': 'INT8', 'WATER_HIT_INFO': ['FIXED_DICT', [('pos', 'VECTOR3'), ('vel', 'FLOAT'), ('dist', 'FLOAT'), ('pathToDetonation', 'FLOAT'), ('penetration', 'FLOAT'), ('passTime', 'FLOAT')], False], 'STAT_INFO': ['FIXED_DICT', [('type', 'INT32'), ('amount', 'FLOAT'), ('vehicleId', 'PLAYER_ID'), ('victimId', 'TARGET_ID')], False], 'CAPTURE_INFO': ['FIXED_DICT', [('vehicleID', 'SHIP_ID'), ('share', 'FLOAT')], False], 'ARENA_UNIQUE_ID': 'UINT64', 'PRE_BATTLE_ID': 'UINT32', 'OBJECT_ID': 'INT32', 'PLAYER_DEF': ['FIXED_DICT', [('mbox', 'MAILBOX'), ('id', 'PLAYER_ID'), ('name', 'STRING'), ('dogTag', ['ARRAY', 'GAMEPARAMS_ID']), ('shipConfig', 'SHIP_CONFIG'), ('compactCrewModifiers', 'CREW_MODIFIERS_COMPACT_PARAMS'), ('aiConf', 'INT32'), ('dbid', 'DB_ID'), ('preBattleId', 'DB_ID'), ('clanInfo', 'PLAYER_CLAN_INFO'), ('extraInfo', 'PYTHON'), ('realm', 'STRING')], True], 'GOAL_DEF': ['FIXED_DICT', [('type', 'UINT8'), ('id', 'TARGET_ID'), ('position', 'VECTOR3'), ('teamId', 'TEAM_ID'), ('angle', 'UINT8')], True], 'CONTROL_POINT_STATE': ['FIXED_DICT', [('position', ['ARRAY', 'FLOAT', 2]), ('radius', 'FLOAT'), ('innerRadius', 'FLOAT'), ('buoy_modelID', 'GAMEPARAMS_ID'), ('nextControlPoint', 'INT8'), ('controlPointType', 'UINT8'), ('timerName', 'STRING'), ('teamId', 'TEAM_ID'), ('progress', ['ARRAY', 'FLOAT', 2]), ('neutralProgress', 'FLOAT'), ('invaderTeam', 'TEAM_ID'), ('bothInside', 'BOOL'), ('hasInvaders', 'BOOL'), ('isEnabled', 'BOOL'), ('isVisible', 'BOOL')], False], 'RESOURCE_RECORD': ['FIXED_DICT', [('id', 'ENTITY_ID'), ('current', 'INT32'), ('min', 'INT32'), ('max', 'INT32')], False], 'SHOT': ['FIXED_DICT', [('pos', 'VECTOR3'), ('pitch', 'FLOAT'), ('speed', 'FLOAT'), ('tarPos', 'VECTOR3'), ('shotID', 'UINT16'), ('gunBarrelID', 'UINT8'), ('serverTimeLeft', 'FLOAT'), ('shooterHeight', 'FLOAT'), ('hitDistance', 'FLOAT')], False], 'PLAYERS_DEFS': ['ARRAY', 'PLAYER_DEF'], 'REPLAY_METADATA_STATS': ['FIXED_DICT', [('credits', 'UINT32'), ('exp', 'UINT32'), ('damage', 'UINT32'), ('medals', 'UINT8'), ('kills', 'UINT8')], False], 'GLOBAL_WEATHER_ITEM': ['FIXED_DICT', [('fromParam', 'GAMEPARAMS_ID'), ('toParam', 'GAMEPARAMS_ID'), ('startTime', 'INT16'), ('endTime', 'INT16')], True], 'PREREQUISITE_DATA': ['FIXED_DICT', [('ships', ['ARRAY', 'PREREQUISITE_SHIP_DATA']), ('effects', ['ARRAY', 'STRING']), ('weather', ['ARRAY', 'GAMEPARAMS_ID']), ('squadrons', ['ARRAY', 'GAMEPARAMS_ID'])], False], 'VISIBILITY_DISTANCES': ['FIXED_DICT', [('byShip', 'FLOAT'), ('byPlane', 'FLOAT'), ('bySmoke', 'FLOAT')], False], 'PLANE_PATH': ['ARRAY', 'PLANE_WAYPOINT'], 'AVATAR_ID': 'INT64', 'BATTLE_DEF': ['FIXED_DICT', [('mapId', 'MAP_ID'), ('type', 'INT16'), ('duration', 'INT16'), ('weather', 'INT8'), ('level', 'INT8'), ('teamBuildType', 'UINT8'), ('regionID', 'STRING'), ('sseInfo', 'STRING'), ('pveInfo', 'UINT64'), ('realms', ['ARRAY', 'STRING']), ('eventInfo', 'GAMEPARAMS_ID'), ('holderTeams', ['ARRAY', 'TEAM_ID'])], False], 'MAP_ID': 'UINT8', 'TRAINING_ROOM_DEF': ['FIXED_DICT', [('commandersManagement', 'BOOL'), ('shipRestrictions', 'SHIP_RESTRICTIONS'), ('hideShips', 'BOOL'), ('scenario', 'UNICODE_STRING'), ('teamSize', 'INT32'), ('preBattleDef', 'PRE_BATTLE_DEF'), ('distributedPlayersCount', 'INT32'), ('notDistributedPlayersCount', 'INT32'), ('passwordLen', 'INT32'), ('hasFriends', 'BOOL'), ('observersAvailable', 'BOOL')], True], 'TORPEDO': ['FIXED_DICT', [('pos', 'VECTOR3'), ('dir', 'VECTOR3'), ('shotID', 'UINT16'), ('armed', 'UINT16')], False], 'ENTITY_DEBUG_TEXT': ['FIXED_DICT', [('layer', 'STRING'), ('text', 'STRING')], False], 'ON_HIT_INFO': ['FIXED_DICT', [('baseInfo', 'COLLISION_INFO_BASE'), ('ownerID', 'ENTITY_ID'), ('paramsId', 'GAMEPARAMS_ID'), ('weaponType', 'WEAPON_TYPE'), ('speed', 'UINT16'), ('salvoID', 'INT16'), ('shotID', 'UINT32'), ('waterHit', 'WATER_HIT_INFO'), ('waterRefraction', 'WATER_HIT_INFO'), ('initialPosXZ', ['ARRAY', 'FLOAT', 2])], False], 'PLANE_ID': 'INT64', 'BATTLE_LOGIC_DEBUG_CHANNEL': ['FIXED_DICT', [('name', 'STRING'), ('text', 'STRING'), ('position', 'VECTOR2')], False], 'DB_ID_LIST': ['ARRAY', 'DB_ID']}