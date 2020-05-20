#!/usr/bin/python3
# -*- coding: utf-8 -*-
# simulate_craft.py

import os
import craft 
import random

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

items = craft.DataSet(craft.Item, craft.get_fullname('items.csv'))
recipes = craft.DataSet(craft.Recipe, craft.get_fullname('recipes.csv'))
ingred = craft.DataSet(craft.RecipeIngredient, craft.get_fullname('recipe_ingredients.csv'))
methods = craft.DataSet(craft.CraftingMethod, craft.get_fullname('crafting_methods.csv') )

class InventoryItem(object):
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity
    def __str__(self):
        return str(self.item_id)  + ' (x' + str(self.quantity) + ')'


inv = craft.DataSet(InventoryItem, craft.get_fullname('inventory.csv'))




def main():
    cmd = 'start'
    print(recipes.str_object_list())
    print(inv.str_object_list())
    while cmd != '':
        print(get_cmd_list('main'))
        cmd = input("enter command: ")
        if cmd in ['1','2','3','4','5','6','7','8','9']:
            command_craft(int(cmd)-1)
        if cmd == 'a':
            command_buy()
        if cmd == 'r':
            print(recipes.str_object_list())
        if cmd == 'i':
            print(inv.str_object_list())

def get_cmd_list(menu):
    res = '<'
    if menu == 'main':
        res += '[1-9] craft recipe  [a]dd random inv  [r]ecipes [i]nventory  [0] Help  [Enter] to exit'

    res += '>'
    return res

def command_craft(recipe_num):
    print('crafting ', str(recipes.object_list[recipe_num]))

def command_buy():
    num_items_to_add = random.randint(1,3)
    for i in range(num_items_to_add):
        item_num_to_add = random.randint(0,len(items.object_list)-1)
        itm = items.object_list[item_num_to_add]
        inv_to_add = InventoryItem(itm.name, str(random.randint(1,50)))
        print('Adding ' + str(inv_to_add))
        inv.object_list.append(inv_to_add)



def command_help():
    """
    Crafting help
    """
    print('Help Screen')
    print(' - modify the recipes.csv for different recipes')
    print(' - update item ingredients')
    
    


if __name__ == '__main__':
	main()
