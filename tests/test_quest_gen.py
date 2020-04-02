#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_quest_gen.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)


import worldbuild.quest_gen.quest as mod_quest


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_01_location(self):
        hills = mod_quest.Location('hills', 'rolling hills', [4,8])
        print(hills)
        self.assertEqual(hills.name, 'hills')
        self.assertEqual(hills.desc, 'rolling hills')
        self.assertEqual(hills.coords, [4,8]) 
  
    def test_02_item(self):
        hills = mod_quest.Location('hills', 'rolling hills', [4,8])
        forest = mod_quest.Location('forest', 'Dark forest near the hills', [4,7])
        woods = mod_quest.Location('woods', 'Woodland between mountains and river', [7,12])
        wood = mod_quest.Item('wood', 'Wooden planks', [forest, hills, woods ])
        print(wood)
        self.assertEqual(wood.name, 'wood')
        self.assertEqual(wood.desc, 'Wooden planks')
        self.assertEqual(wood.spawns_at_locations, [forest, hills, woods ]) 
        

    def test_03_locations(self):
        locations = mod_quest.Locations()
        locations.fill_from_csv('..\worldbuild\data\locations.csv')
        print(locations)


        self.assertEqual(len(str(locations)), 169) 
        self.assertTrue(locations.raw_data[0], 'home,your home,0,0')
        


    


if __name__ == '__main__':
    unittest.main()