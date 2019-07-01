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

    def test_04_network_minecraft(self):
        """
        Test of rcon connection to minecraft

        Notes on RCON protocol at http://wiki.vg/RCON
        TODO - make sure you modify the server.properties file as follows
        enable-rcon=true
        rcon.password=minecraft_server.cred
        rcon.port=25575
        broadcast-rcon-to-ops=false
        """

        f = open('T:\\user\\AIKIF\\pers_data\\credentials\\minecraft_server.cred')
        pwd = f.read()
        f.close()

        import mcrcon
        rcon = mcrcon.MCRcon()
        rcon.connect('192.168.1.9', 25575)
        rcon.login(pwd)
        say_hi = rcon.command('/say hi from rcon')
        rcon.command('/tp craftandstore 4 102 4')
        import time
        time.sleep(1)
        rcon.command('/fill 0 100 0 2 101 2 minecraft:air') # clear area first
        res2 = rcon.command('/fill 0 100 0 2 101 2 minecraft:glass 0')
        rcon.disconnect()
        self.assertEqual(res2, '18 blocks filled')


if __name__ == '__main__':
    unittest.main()
