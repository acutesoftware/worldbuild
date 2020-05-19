#!/usr/bin/python3
# -*- coding: utf-8 -*-
# simulate_craft.py

import os
import craft 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

def main():
    cmd = 'start'
    while cmd != '':
        cmd = get_command()
        if cmd == '1':
            command_craft()
        if cmd == '2':
            command_buy()
        if cmd == '3':
            command_list()
        if cmd == '0':
            command_help()


def get_command():
    # press enter manually for now, but game loop
    print('commands are:')
    print('1 = craft')
    print('2 = buy')
    print('3 = list')
    print('0 = Help')
    print('press enter to exit')
 
    
    cmd = input("enter command: ")
    return cmd

def command_craft():
    print('todo - craft')

def command_buy():
    print('todo - buy stuff')

def command_list():
    print('todo - list')



def command_help():
    """
    Crafting help
    """
    print('Help Screen')
    print(' - modify the recipes.csv for different recipes')
    print(' - update item ingredients')
    
    


if __name__ == '__main__':
	main()
