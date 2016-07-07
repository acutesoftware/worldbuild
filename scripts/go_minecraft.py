# go_minecraft.py

import sys
import time
import aikif.toolbox.interface_windows_tools as mod_tool

players = ['DynamiteBuilder', 'craftandstore']

server = '1.9'
server = '1.10'

if server ==  '1.10':
    locations = [ 
        {'name':'v2-home',            'loc':'248 66 -61'},
        {'name':'v2-farm',            'loc':'977 94 -228' },
        {'name':'v2-floating-garden', 'loc':'685 107 -588' },
        {'name':'v2-floating-castle', 'loc':'-202 105 -655' },
        {'name':'v2-stronghold',      'loc':'415 72 -2198' },
        {'name':'v2-village',         'loc':'121 77 -2019' },
        {'name':'v2-overhang-lookout', 'loc':'-449 110 -1830' },
    ]    
else:
    locations = [ 
        {'name':'v1-home',      'loc':'151 103 736'},
        {'name':'v1-treehouse', 'loc':'120 72 662' },
        {'name':'v1-castle',    'loc':'-132 68 388' },
        {'name':'v1-village',   'loc':'-298 82 946' },
        {'name':'v1-stables',   'loc':'-602 82 951' },
        {'name':'v1-desert',    'loc':'-1524 97 1580' },
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
    
    
    
