#!/usr/bin/python3
# -*- coding: utf-8 -*-
# simulate_npc.py

import os
import quest 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

# setup simulation
locations = quest.Locations()
locations.fill_from_csv(os.path.join(root_folder,'data', 'locations_town.csv'))

items = quest.Items()
items.fill_from_csv(os.path.join(root_folder,'data', 'items.csv'))

npcs = quest.NPCs()
npcs.fill_from_csv(os.path.join(root_folder,'data', 'npcs.csv'))


def main():
    cmd = get_command()
    while cmd != '':
        show_status()
        cmd = get_command()



def show_status():

    for n in npcs.raw_data:
        print(n)


def get_command():
    # press enter manually for now, but game loop
    print('commands are:')
    print('1 = move')
    print('2 = help')
    print('3 = fight')
    print('4 = pass')
    
    
    cmd = input("enter command: ")
    return cmd


if __name__ == '__main__':
	main()
