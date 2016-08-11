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
        
    def test_03_house_small(self):    
        s3 = structures.StructureHouse('small_house', 4, 4, 4)
        self.assertEqual(s3.name, 'small_house')
        self.assertEqual(s3.type, 'shelter')
        self.assertEqual(len(s3.definition), 6)
 
    def test_04_house_large(self):    
        s4 = structures.StructureHouse('big_house', 16, 6, 20)
        print(s4)
        self.assertEqual(s4.name, 'big_house')
        self.assertEqual(s4.type, 'shelter')
        self.assertEqual(len(s4.definition), 6)
 
        area,vol = s4._calc_size()
        self.assertEqual(area, 285)
        self.assertEqual(vol, 1425)
 
        
if __name__ == '__main__':
    unittest.main()


