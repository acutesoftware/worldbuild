#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_sample_tiny.py
# for examples see https://gist.github.com/bowsersenior/979804
import os
import sys
import unittest
import pprint

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

import sample


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_read_yaml_tiny(self):
        fle = os.path.join(pth, 'samples', 'tiny_world.yaml')
        
        # _print_yaml(fle)  # works
        y = sample._read_yaml(fle)
        pprint.pprint(y) 
        self.assertEqual(y['rooms'][0]['name'], 'kitchen')
        self.assertEqual(y['rooms'][1]['name'], 'lounge')
        
        self.assertEqual(y['objects'][0]['name'], 'chair')
        self.assertEqual(y['objects'][1]['name'], 'ball')
        
        self.assertEqual(y['characters'][0]['name'], 'cat')

    def test_02_check_mappings(self):
        fle = os.path.join(pth, 'samples', 'tiny_world.yaml')
        y = sample._read_yaml(fle)
        
        print('mappings[0] = ', y['mappings'][0])
        print('mappings[1] = ', y['mappings'][1])
        
        self.assertEqual(y['mappings'][1], {'people <<': [{'name': 'cat'}]})
        #self.assertEqual(y['mappings']['locations'][1]['name'], 'lounge')
        #self.assertEqual(y['mappings']['people'][0]['name'], 'cat')
        
        
        
if __name__ == '__main__':
    unittest.main()

