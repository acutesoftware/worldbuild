#!/usr/bin/python3
# -*- coding: utf-8 -*-
# quest.py

import random

objects = [
    {'name':'rusty key', 
     'desc':'an old rusty key',
     'location':'woods',
     'when_seen':'the key is old and rusty, but glitters slightly',
     'on_success':'the key slides into the lock with a firm click'},
    {'name':'chest', 
     'desc':'a battered chest',
     'location':'ravine',
     'when_seen':'the chest is covered in dirt',
     'on_success':'the chest opens, revealing $TREASURE$'},
]

locations = [
    {'name':'home'},
    {'name':'woods'},
    {'name':'forest'},
    {'name':'hills'},
    {'name':'ravine'},
    
]

characters = [
    {'name':'Zentar',
    }
]

def main():
    """
    for loc in locations:
        print('you search ' + loc['name'])
        for obj in objects:
            if obj['location'] == loc['name']:
                print('you find ', obj['name'])
                print(obj['when_seen'])
    """

    # setup locations
    hills = Location('hills', 'rolling hills', [4,8])
    forest = Location('forest', 'Dark forest near the hills', [4,7])
    woods = Location('woods', 'Woodland between mountains and river', [7,12])
    beach = Location('beach', 'Nice sandy beach', [2,1])


    wood = Item('wood', 'Wooden planks', [forest, hills, woods ])
    string = Item('string', 'Used for fishing rods and bows', [hills ])
    shells = Item('shells', 'Shells', [beach ])

    jim = NPC('Jim', forest, 'Idle', [wood])                
    sandy = NPC('Sandy', hills, 'hunting', [string, shells])


    # generate quest list
    my_quests = []
    my_quests.append(Quest().create_next_quest_via_npc_needs(jim))
    my_quests.append(Quest().create_next_quest_via_npc_needs(sandy))
    
    # Display game
    print('NPCs in this land:')
    print(jim)
    print(sandy)

    print('Your Quest List:')
    for q in my_quests:
        print(q)


class Location(object):
    """
    map areas
    """
    def __init__(self, name, desc, coords):
        self.name = name
        self.desc = desc
        self.coords =  coords
    def __str__(self):
        res = ''
        res += self.name + ' - ' + self.desc 
        res += str(self.coords)
        return     res   

class DataSet(object):
    """
    handles a collection of Objects loaded from a reference file
    """
    def __init__(self):
        self.raw_data = []
        self.object_list = []

    def __str__(self):
        return ''.join([d for d in self.raw_data])


    def fill_from_csv(self, fname):
        with open(fname, 'r') as fip:
            for line in fip:
                self.raw_data.append(line)

class Locations(DataSet):
    """
    handles a collection of Locations loaded from a reference file
    """
    def __init__(self):
        DataSet.__init__(self)


class NPCs(DataSet):
    """
    handles a collection of NPC Characters loaded from a reference file
    """
    def __init__(self):
        DataSet.__init__(self)

class Items(DataSet):
    """
    handles a collection of Items loaded from a reference file
    """
    def __init__(self):
        DataSet.__init__(self)





class Item(object):
    """
    Items / objects that are in the world. Can be collected
    or crafted
    """
    def __init__(self, name, desc, spawns_at_locations):
        self.name = name
        self.desc = desc
        self.spawns_at_locations =  spawns_at_locations
    def __str__(self):
        res = ''
        res += self.name + ' - ' + self.desc + ' (Spawns at locations:'
        res += '|'.join([l.name for l in self.spawns_at_locations])
        res += ')\n'

        return     res   


class NPC(object):
    """
    a Non-Player character
    """
    def __init__(self, name, location, status, items_needed):
        self.name = name
        self.location = location
        self.status = status
        self.items_needed = items_needed
    def __str__(self):
        res = ''
        res += self.name + ' is at ' + self.location.name + '. Status = ' + self.status 

        if len(self.items_needed) > 0:
            res += '\nThis NPC needs : '
            #for i in self.items_needed:
            #    res += str(i.name)
            res += ', '.join([i.name for i in self.items_needed])

        return     res   

class Quest(object):
    """
    handles a single quest
    """
    def __init__(self):
        pass
    def __str__(self):
        res = '+------------------------------------------------------------\n'
        res += '| ***' + self.name + ' ***\n'
        res += '| ' + self.desc + '\n'
        res += '| Location = ' + str(self.location[0].name) + '\n'
        res += '| Status = ' + self.status + '\n'
        res += '| Reward = ' + self.reward + '\n'
        res += '| Return to ' + self.quest_giver.name + ' with '
        #res += ','.join([i.name for i in self.items_required])
        res +=  str(self.quantity) + ' ' + self.items_required.name + '\n'
        res += '+------------------------------------------------------------\n'

        return     res   


    def create_next_quest_via_npc_needs(self, npc):
        """
        takes NPC as parameter and finds the next quest this person needs
        """

        for needs in npc.items_needed:   # just the first one
            self.name = 'Collect ' + needs.name
            self.quest_giver = npc
            self.quantity = random.choice([4,8,10,25])
            self.reward = random.choice(['fishing rod', 'hammer', '5 Gold', '10 Gold'])
            self.items_required = needs
            self.desc = npc.name + ' needs you to collect ' + needs.name #+ '. You can find these at ' + str(needs.spawns_at_locations) 
            self.status = 'Available'
            self.location = needs.spawns_at_locations
        
        return self

if __name__ == '__main__':
	main()
