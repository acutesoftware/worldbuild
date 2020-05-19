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
    for recipe in recipes.object_list:
        print(recipe)



class Recipe(object):
    """
    Recipe
    """
    def __init__(self, name, desc, ingred):
        self.name = name
        self.desc = desc
        self.ingred =  ingred
    def __str__(self):
        res = ''
        res += self.name + ' - ' + self.desc 
        res += str(self.ingred)
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
                self.raw_data.append(line)

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
            print('RECIPE RAW = ', cols)
            cur_loc = Recipe(cols[0], cols[1], cols[2])
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
            print('ITEMS RAW = ', cols)
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
        self.buy_price =  buy_price
        self.sell_price =  sell_price
        
    def __str__(self):
        res = ''
        res += self.name + ' - ' + self.desc
        res += ' (sells for ' + self.sell_price + ')'
        res += '\n'

        return     res   


if __name__ == '__main__':
	main()
