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

structure_data = [{'name':'test_world_build', 'coords':[0,5,67,3,6]}]
style_data = {'base':'wood', 'colour':'greens', 'texture':'soft'}


class TestWorldBuilder(unittest.TestCase):
    def test_01_instantiate_base_class(self):
        res = world_builder.BuildMap(structure_data,style_data)  # make sure we can pass dict or list
        self.assertEqual(res.style['base'],'wood')
        self.assertEqual(res.style['colour'],'greens')
        self.assertEqual(res.style['texture'],'soft')

        self.assertEqual(res.struct_data[0]['name'],'test_world_build')
        self.assertEqual(res.struct_data[0]['coords'],[0, 5, 67, 3, 6])
        

if __name__ == '__main__':
    unittest.main()

