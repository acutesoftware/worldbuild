# init_minecraft.py
import os
import sys

sys.path.append(os.path.join('..','..','worldbuild'))
import cls_interface_application as mod_if

mc = mod_if.InterfaceMineCraft('Minecraft server', 0.2)
mc.activate()
print(mc.send_command('/difficulty 2'))
print(mc.send_command('/op DynamiteBuilder'))
print(mc.send_command('/op craftandstore'))




"""
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
    
"""
