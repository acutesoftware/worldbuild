#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_structures.py


import os
import sys
import unittest
import pprint


root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

import structures

hut_data = {}
hut_data['type'] = 'shelter'
hut_data['x1'] = 0
hut_data['x2'] = 4
hut_data['y1'] = 0
hut_data['y2'] = 3
hut_data['z1'] = 0
hut_data['z2'] = 5

class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_baseclass_structures(self):
        s1 = structures.StructureDefinition('hut', hut_data)
        print(s1)
        self.assertEqual(s1.name, 'hut')
        self.assertEqual(s1.type, '')
        self.assertEqual(len(s1.definition), 7)
        
    def test_02_hut(self):
        s2 = structures.StructureHut('hut')
        self.assertEqual(s2.name, 'hut')
        self.assertEqual(s2.type, 'shelter')
        self.assertEqual(len(s2.definition), 6)
        
        

        
if __name__ == '__main__':
    unittest.main()


