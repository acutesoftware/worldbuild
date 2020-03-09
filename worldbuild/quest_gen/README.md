# Quest Generator

prototype code to manage stories and generate quests for games / worlds.

## Quick Start
See tests folder for examples (todo later)

For now, run quest.py to generate random quests based on NPC's

```

NPCs in this land:
Jim is at forest. Status = IdleThis NPC needs : wood
Sandy is at hills. Status = huntingThis NPC needs : string, shells
Your Quest List:
+------------------------------------------------------------
| ***Collect wood ***
| Jim needs you to collect wood
| Location = forest
| Status = Available
| Reward = 10 Gold
| Return to Jim with 25 wood
+------------------------------------------------------------

+------------------------------------------------------------
| ***Collect shells ***
| Sandy needs you to collect shells
| Location = beach
| Status = Available
| Reward = fishing rod
| Return to Sandy with 25 shells
+------------------------------------------------------------

```

## Quest Generation Process

There are 3 steps to generate quests
1. Create Locations

2. Create Items

3. Create NPC's

4. Generate Quests


### Create Locations

    hills = Location('hills', 'rolling hills', [4,8])
    forest = Location('forest', 'Dark forest near the hills', [4,7])
    woods = Location('woods', 'Woodland between mountains and river', [7,12])
    beach = Location('beach', 'Nice sandy beach', [2,1])

### Create Items

    wood = Item('wood', 'Wooden planks', [forest, hills, woods ])
    string = Item('string', 'Used for fishing rods and bows', [hills ])
    shells = Item('shells', 'Shells', [beach ])

### Create NPC's

    jim = NPC('Jim', forest, 'Idle', [wood])                
    sandy = NPC('Sandy', hills, 'hunting', [string, shells])

### Generate Quests
    
    my_quests = []
    my_quests.append(Quest().create_next_quest_via_npc_needs(jim))
    my_quests.append(Quest().create_next_quest_via_npc_needs(sandy))
    



## Stories
Write text files (one file per story section) to build up a story

Write a config file to show how to parse the stories into data structures.

