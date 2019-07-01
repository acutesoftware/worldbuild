#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_convert_map_to_data.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

img_file = os.path.join(os.getcwd(), '..', 'worldbuild', 'samples', 'alrona', 'alrona-pen-coloured.jpg')

import convert_map_to_data


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_01_instantiate_class(self):
        convert_map_to_data.extract_data_from_map(img_file)

        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
