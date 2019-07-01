#!/usr/bin/python3
# -*- coding: utf-8 -*-
# quest.py

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
    for loc in locations:
        print('you search ' + loc['name'])
        for obj in objects:
            if obj['location'] == loc['name']:
                print('you find ', obj['name'])
                print(obj['when_seen'])



if __name__ == '__main__':
	main()
