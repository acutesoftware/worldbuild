#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_cls_interface_application.py

import os
import sys
import unittest
import time

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'

sys.path.append(pth)


import cls_interface_application as mod_if

class TestAgentInterfaceEnvironment(unittest.TestCase):
    def test_01_instantiate_base_class(self):
        res = mod_if.InterfaceApplication('MINECRAFT')
        self.assertEqual(str(res),'Base class Interface for MINECRAFT')
        
    def test_02_activate_minecraft(self):
        """
        TODO - check if server running before calling this
        """
        start_time = time.time()
        res = mod_if.InterfaceMineCraft('Minecraft server')
        res.activate()
        return_val = res.send_command('/say test_02')
        self.assertEqual(return_val, '/say test_02{ENTER}')
        self.assertTrue((time.time() - start_time) < 1)
        
    def test_03_slow_delay(self):
        start_time = time.time()
        res = mod_if.InterfaceMineCraft('Minecraft server', time_delay=2)
        res.activate()
        return_val = res.send_command('/say test_03')
        self.assertEqual(return_val, '/say test_03{ENTER}')
        end_time = time.time()
        print('Time for delayed send_keys = ', end_time - start_time)
        self.assertTrue((end_time - start_time) > 3)
        self.assertTrue((end_time - start_time) < 5)
        
if __name__ == '__main__':
    unittest.main()
