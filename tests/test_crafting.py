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
        #print(res)
        self.assertEqual(str(res),'new recipe')

    def test_02_dataset_recipe(self):
        recipes = mod_craft.DataSet(mod_craft.Recipe, mod_craft.get_fullname('recipes.csv'))
        self.assertEqual(str(recipes),'Dataset containing 6 Recipe objects')
        tot_time_to_build = 0
        for recipe in recipes.object_list:
            #print(recipe)
            tot_time_to_build += int(recipe.base_time_to_build)
        #print('total time to build all recipes = ' +  str(tot_time_to_build))
        self.assertEqual(str(recipes.object_list[0]), 'Torch')
        self.assertEqual(str(recipes.object_list[1]), 'Wooden Plank')
        self.assertEqual(19, tot_time_to_build)
    


if __name__ == '__main__':
    unittest.main()