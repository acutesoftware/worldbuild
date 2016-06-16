#!/usr/bin/python3
# -*- coding: utf-8 -*-
# cls_interface_application.py

import time
import aikif.toolbox.interface_windows_tools as mod_tool


class InterfaceApplication(object):
    """
    Base class for talking to Minecraft,
    Blender, standard grids and other apps.
    
    This is inherited from one of the application
    specific classes below that handle the format
    of the commands.
    
    To start with, apps are controlled via SendKeys
    but to change this, you can subclass it or change
    the applications code once API details are working.
    """
    
    def __init__(self, app_caption=''):
        
            
        self.app_caption = app_caption
        
    def __str__(self):
        res = ''
        res += 'Base class Interface for ' + self.app_caption
        return res
        
        
    def activate(self):    
        mod_tool.app_activate(self.app_caption)
        time.sleep(.5)
        

        
        
class InterfaceMineCraft(InterfaceApplication):
    """
    Class to handle how to talk to MineCraft
    """
    def __init__(self, app_caption):
        self.string_execute = '{ENTER}'
        self.time_delay = 0.01
        InterfaceApplication.__init__(self, app_caption='')

    def __str__(self):
        res = ''
        res += 'BuildMap '
        return res
        
    def send_command(self, cmd):
        """
        Sends a command to the application
        """
        mod_tool.send_keys(cmd)
        time.sleep(self.time_delay) 
        mod_tool.send_keys(self.string_execute)
        time.sleep(self.time_delay) 
        return cmd + self.string_execute
