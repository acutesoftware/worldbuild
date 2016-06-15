#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_cls_interface_application.py

import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'

sys.path.append(pth)


import cls_interface_application as mod_if

class TestAgentInterfaceEnvironment(unittest.TestCase):
    def test_01_instantiate_base_class(self):
        res = mod_if.InterfaceApplication('MINECRAFT')
        self.assertEqual(str(res),'Base class Interface for MINECRAFT')
        
    def test_02_activate_minecraft(self):
        res = mod_if.InterfaceMineCraft('Minecraft server')
        res.activate()
        res.send_command('/say hello')
        

        
if __name__ == '__main__':
    unittest.main()
