#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_crafting.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = root_folder #+ os.sep + 'worldbuild'
sys.path.append(pth)


from worldbuild.crafting import craft as mod_craft


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_01_recipe(self):
        res = mod_craft.Recipe('1', 'new recipe','20','mix')
        print(res)
        self.assertEqual(str(res),'new recipe')

    


if __name__ == '__main__':
    unittest.main()