#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_world_builder.py


import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

import world_builder


class TestWorldBuilder(unittest.TestCase):
    def test_01_instantiate_base_class(self):
        res = world_builder.BuildMap([],{})  # make sure we can pass dict or list
        print(res)
        #self.assertEqual(str(res),'Base class Interface for MINECRAFT')

        

if __name__ == '__main__':
    unittest.main()

