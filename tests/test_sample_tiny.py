#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_sample_tiny.py
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
        print(y) 
        self.assertEqual(y['location'][0]['name'], 'kitchen')
        self.assertEqual(y['location'][1]['name'], 'lounge')
        
        self.assertEqual(y['object'][0]['name'], 'chair')
        self.assertEqual(y['object'][1]['name'], 'ball')
        self.assertEqual(y['object'][2]['name'], 'cat')

if __name__ == '__main__':
    unittest.main()

