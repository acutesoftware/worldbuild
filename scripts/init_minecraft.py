# init_minecraft.py

import time
import aikif.toolbox.interface_windows_tools as mod_tool

print('remember to start the minecraft server')
mod_tool.app_activate('Minecraft server')
time.sleep(1.0) 

mod_tool.send_keys("{ESC}")   # client will be paused
time.sleep(0.1) 
mod_tool.send_keys('/difficulty 2')
time.sleep(0.2) 
mod_tool.send_keys("{ENTER}")  # needs Enter key
time.sleep(0.2) 

players = ['DynamiteBuilder', 'craftandstore']

for p in players:
    mod_tool.send_keys('/op ' + p)
    mod_tool.send_keys("{ENTER}")  # needs Enter key
    time.sleep(0.1) 
    
