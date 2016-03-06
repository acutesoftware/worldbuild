# survival.py

import time
import aikif.toolbox.interface_windows_tools as mod_tool

print('remember to SET FOCUS to server text box')
#mod_tool.app_activate('Minecraft 1.9')  # doesnt like sending to client (ESC key works
mod_tool.app_activate('Minecraft server')
time.sleep(1.0) 

players = ['DynamiteBuilder', 'craftandstore']

for p in players:
    mod_tool.send_keys("{ESC}")   # client will be paused
    time.sleep(0.1) 
    mod_tool.send_keys('/gamemode survival ' + p)
    time.sleep(0.2) 
    mod_tool.send_keys("{ENTER}")  # needs Enter key
    time.sleep(0.2) 

