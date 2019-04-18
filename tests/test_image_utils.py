#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_image_utils.py

import os
import sys
import unittest
import pprint

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

map_file = os.path.join(pth , 'samples', 'alrona', 'alrona-pen-coloured.jpg')
op_file = os.path.join(pth , 'samples', 'alrona', 'alrona-pen-coloured-grid.jpg')

import image_utils


class TestImageUtils(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_01_add_grid_lines(self):
        print('testing grid lines...')
        try:
            os.remove(op_file)
        except:
            pass 
        image_utils.add_grid_lines(map_file, op_file, 200)
        self.assertEqual(os.path.exists(op_file), True)



if __name__ == '__main__':
    unittest.main()
