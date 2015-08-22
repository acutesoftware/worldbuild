#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_build_world.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

import build_world


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        build_world.main()
        self.assertTrue(os.path.exists('world_traversed.txt'))


if __name__ == '__main__':
    unittest.main()
