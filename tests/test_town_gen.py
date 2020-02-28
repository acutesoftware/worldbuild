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
        res = town_gen.make_town(7)

        self.assertEqual(len(res),7)

    def test_02_print_town(self):
        med_town = town_gen.make_town(10)

        self.assertEqual(len(med_town),10)
        town_gen.print_town(med_town)





if __name__ == '__main__':
    unittest.main()