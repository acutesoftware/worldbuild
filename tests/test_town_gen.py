#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_town_gen.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)


import worldbuild.town_gen.town_gen as town_gen


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_01_make_town(self):
        town_x = 60
        town_y = 3
        res = town_gen.make_town(town_y,town_x)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        #self.assertTrue(res.grid.get_grid_width() > 14)
        print(res)

    def test_02_print_town(self):

        #med_town = town_gen.make_town(10, 10)

        #self.assertEqual(len(med_town),10)
        #town_gen.print_town(med_town)
        pass





if __name__ == '__main__':
    unittest.main()