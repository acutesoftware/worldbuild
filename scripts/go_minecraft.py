# go_minecraft.py

import sys
import time
import aikif.toolbox.interface_windows_tools as mod_tool

players = ['DynamiteBuilder', 'craftandstore']

locations = [
    {'name':'home',      'loc':'151 103 736'},
    {'name':'treehouse', 'loc':'120 72 662' },
    {'name':'castle',    'loc':'-132 68 388' },
    {'name':'village',   'loc':'-298 82 946' },
    {'name':'stables',   'loc':'-602 82 951' },
    {'name':'desert',    'loc':'-1524 97 1580' },
    
]    
    
print('Minecraft Teleport Service for players ' + str(players))
for num, l in enumerate(locations):
    print(str(num+1) + ' = ' + l['name'])
    
loc = locations[int(input('Enter Location ')) - 1]   

mod_tool.app_activate('Minecraft server')
    
for p in players:
    print('Teleporting ' + p + ' to ' + loc['name'] + ' (' + loc['loc'] + ')')
    mod_tool.send_keys('/tp ' + p + ' ' + loc['loc'])
    mod_tool.send_keys("{ENTER}")  # needs Enter key
    time.sleep(0.1) 
    
    
    
