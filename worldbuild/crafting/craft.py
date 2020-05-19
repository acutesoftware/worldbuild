#!/usr/bin/python3
# -*- coding: utf-8 -*-
# quest.py
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

import random



def main():
    # setup the main dataset definitions here
    items = Items()
    items.fill_from_csv(os.path.join(root_folder,'data', 'items.csv'))
    items.rebuild_list()


    recipes = Recipes()
    recipes.fill_from_csv(os.path.join(root_folder,'data', 'recipes.csv'))
    recipes.rebuild_list()

    ingred = RecipeIngredients()
    ingred.fill_from_csv(os.path.join(root_folder,'data', 'recipe_ingredients.csv'))
    ingred.rebuild_list()

    for recipe in recipes.object_list:
        print(recipe)
        print('--------ingredients ----------')
        for ing in ingred.object_list:
            if ing.recipe_id == recipe.recipe_id:
                print(ing.crafting_method_id + ' ' + ing.item_id)



class Recipe(object):
    """
    Recipe
    """
    def __init__(self, recipe_id,recipe_name,base_time_to_build,base_cost_to_build):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.base_time_to_build =  base_time_to_build
        self.base_cost_to_build =  base_cost_to_build
        
    def __str__(self):
        res = '\n----------------------------\n' + self.recipe_name
        return     res   

class DataSet(object):
    """
    handles a collection of Objects loaded from a reference file
    """
    def __init__(self):
        self.raw_data = []
        self.object_list = []

    def __str__(self):
        return ''.join([d for d in self.raw_data])


    def fill_from_csv(self, fname):
        with open(fname, 'r') as fip:
            for line in fip:
                self.raw_data.append(line.strip('\n'))

class Recipes(DataSet):
    """
    handles a collection of Locations loaded from a reference file
    """
    def __init__(self):
        DataSet.__init__(self)

    def rebuild_list(self):
        self.object_list = []  # clear the object list
        for raw_line in self.raw_data:
            cols = raw_line.split(',')
            #print('RECIPE RAW = ', cols)
            cur_loc = Recipe(cols[0], cols[1], cols[2], cols[3])
            self.object_list.append(cur_loc)


class Items(DataSet):
    """
    handles a collection of Items loaded from a reference file
    """
    def __init__(self):
        DataSet.__init__(self)

    def rebuild_list(self):
        self.object_list = []  # clear the object list
        for raw_line in self.raw_data:
            cols = raw_line.split(',')
            #print('ITEMS RAW = ', cols)
            cur_item = Item(cols[0], cols[1], cols[2], cols[3])
            self.object_list.append(cur_item)

class Item(object):
    """
    Items / objects that are in the world. Can be collected
    or crafted
    """
    def __init__(self, name,desc,buy_price,sell_price):
        self.name = name
        self.desc = desc
        self.buy_price = buy_price
        self.sell_price = sell_price
        
    def __str__(self):
        res = ''
        res += self.name + ' - ' + self.desc
        res += ' (sells for ' + self.sell_price + ')'

        return     res   

class RecipeIngredients(DataSet):
    """
    handles a collection of ingredients loaded from a reference file
    """
    def __init__(self):
        DataSet.__init__(self)

    def rebuild_list(self):
        self.object_list = []  # clear the object list
        for raw_line in self.raw_data:
            cols = raw_line.split(',')
            #print('INGREDIENTS RAW = ', cols)
            cur_item = RecipeIngredient(cols[0], cols[1], cols[2], cols[3])
            self.object_list.append(cur_item)

class RecipeIngredient(object):
    """
    multiple ingreds per recipe
    recipe_id,item_id,quantity,crafting_method_id
    """
    def __init__(self, recipe_id,item_id,quantity,crafting_method_id):
        self.recipe_id = recipe_id
        self.item_id = item_id
        self.quantity =  quantity
        self.crafting_method_id =  crafting_method_id
        
    def __str__(self):
        res = ''
        res += self.recipe_id + ' - ' + self.item_id

        return     res   




if __name__ == '__main__':
	main()
