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


    def test_01_make_huge_sparse_town(self):
        town_x = 78
        town_y = 50
        start_y = 3
        start_x = 3
        res = town_gen.make_town('Huge Empty Town', start_y, start_x, town_y,town_x, 99)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        #self.assertTrue(res.grid.get_grid_width() > 14)
        print(res)

    def test_02_make_huge_dense_town(self):
        town_x = 78
        town_y = 50
        res = town_gen.make_town('Huge Populated Town',3,3,town_y,town_x, 5)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        #self.assertTrue(res.grid.get_grid_width() > 14)
        print(res)

    def test_03_make_tiny_town(self):
        town_x = 5
        town_y = 3
        res = town_gen.make_town('Tiny Town - sparse',1,1,town_y,town_x, 80)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        print(res)

    def test_04_make_tiny_town(self):
        town_x = 5
        town_y = 3
        res = town_gen.make_town('Tiny Town - dense',1,1,town_y,town_x, 1)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        print(res)

    def test_05_make_normal_town_sparse(self):
        town_x = 20
        town_y = 5
        res = town_gen.make_town('Starting Town - sparse',3,3,town_y,town_x, 90)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        print(res)

    def test_06_make_normal_town_dense(self):
        town_x = 10
        town_y = 6
        res = town_gen.make_town('Starting Town - dense',3,3,town_y,town_x, 25)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        print(res)

    def test_07_output_town_image(self):
        town_x = 12
        town_y = 6
        res = town_gen.make_town('PrintableTown',3,3,town_y,town_x, 75)
        self.assertEqual(len(res.town_grid), town_y)
        self.assertEqual(len(res.town_grid[0]), town_x)
        print(res)
        print(res.output_detail('town_gen_test_result.png'))




if __name__ == '__main__':
    unittest.main()