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
        assert type(quantity) is str # should be int, but CSV generic import to be fixed later
        self.quantity = quantity
    def __str__(self):
        return str(self.item_id)  + ' (x' + str(self.quantity) + ')'
    def __gt__(self, inv2):
        return self.item_id > inv2.item_id
    def __lt__(self, inv2):
        return self.item_id < inv2.item_id


inv = craft.DataSet(InventoryItem, craft.get_fullname('inventory.csv'))




def main():
    cmd = 'start'
    print(recipes.str_object_list())
    print(inv.str_object_list('N'))
    while cmd != '':
        print(get_cmd_list('main'))
        cmd = input("enter command: ")
        if cmd in ['1','2','3','4','5','6','7','8','9']:
            command_craft(int(cmd)-1)
            # display the inventory to show new item in bags
            print(inv.str_object_list('N'))

        if cmd == 'a':
            command_buy()
        if cmd == 'r':
            print(recipes.str_object_list())
        if cmd == 'i':
            print(inv.str_object_list('N'))
        if cmd == 'b':
            command_build_all()
            inventory_sort()


def get_cmd_list(menu):
    res = '<'
    if menu == 'main':
        res += '[1-9] craft recipe  [a]dd random inv  [r]ecipes [i]nventory  [b]uild all  [Enter] to exit'

    res += '>'
    return res

def command_craft(recipe_num, print_results='Y'):

    if not do_we_have_ingredients_for_recipe(recipe_num):
        if print_results != 'N':
            print('Not enough ingredients to make ' + str(recipes.object_list[recipe_num]))
        return 0

    rec_to_make = recipes.object_list[recipe_num]
    #if print_results != 'N':
    print('crafting', str(rec_to_make))

    ing_needed = []
    rec_to_make = recipes.object_list[recipe_num]
    for ing in ingred.object_list:
        if ing.recipe_id == rec_to_make.recipe_id:
            ing_needed.append([ing.item_id,ing.quantity])

    # remove items from inventory
    for needed in ing_needed:
        for i in inv.object_list:
            if i.item_id == needed[0]:
                i.quantity = str(int(i.quantity) - int(needed[1]))
    
    # added the crafted item to the inventory
    inv_to_add = InventoryItem(rec_to_make.recipe_id, '1')

    inv.object_list.append(inv_to_add)
    inventory_sort()

def do_we_have_ingredients_for_recipe(recipe_num):
    """
    checks the users inventory to make sure there are 
    enough items to make the recipe. returns True/False
    """
    have_items = True
    ing_needed = []
    rec_to_make = recipes.object_list[recipe_num]
    for ing in ingred.object_list:
        if ing.recipe_id == rec_to_make.recipe_id:
            ing_needed.append([ing.item_id,ing.quantity])
    
    print('to make the recipe "' + rec_to_make.recipe_name + '", you need: ')
    print(str(ing_needed))

    # from list of ingredients, check inventory
    have_items = False # assume false until we have quant in inv
    for needed in ing_needed:
        for i in inv.object_list:
            if i.item_id == needed[0]:
                if i.quantity >= needed[1]:
                    # at least one ingred doesnt have quant, so bail 
                    print('MISSING - ' + str(i))
                    #print('i.quantity - ' + str(i.quantity))
                    #print('i.item_id - ' + str(i.item_id))
                    #print('needed - ' + str(needed))
                    return False
                have_items = True # so far, so good    
        print('you need - ' + str(needed))


    return have_items


def command_buy():
    num_items_to_add = random.randint(1,3)
    for i in range(num_items_to_add):
        item_num_to_add = random.randint(0,len(items.object_list)-1)
        itm = items.object_list[item_num_to_add]
        inv_to_add = InventoryItem(itm.name, str(random.randint(1,50)))
        print('Adding ' + str(inv_to_add))
        inv.object_list.append(inv_to_add)
    #print(inv.str_object_list())
    inventory_sort()
    print(inv.str_object_list('N'))

def inventory_sort():
    """
    sorts the inventory and consolidates slots
    """
    #print('sorting bags...')
    for orig_num, orig_item in enumerate(inv.object_list):
        for dupe_num, dupe_item in enumerate(inv.object_list):
            if dupe_num != orig_num:
                if dupe_item.item_id == orig_item.item_id:
                    merge_inv_items(orig_item, dupe_item)
                    del inv.object_list[dupe_num]
    inv.object_list.sort()

    # now remove any items that have zero quantity
    for orig_num, orig_item in enumerate(inv.object_list):
        if orig_item.quantity == '0':
            del inv.object_list[orig_num]
                    

def merge_inv_items(orig_item, dupe_item):
    """
    takes 2 items from a list and merges to 1 or at least slot size
    """
    #print('dupe : ' + str(orig_item) +  str(dupe_item))
    orig_item.quantity = str(int(orig_item.quantity) + int(dupe_item.quantity))
    dupe_item.quantity = '0'



def command_help():
    """
    Crafting help
    """
    print('Help Screen')
    print(' - modify the recipes.csv for different recipes')
    print(' - update item ingredients')
    
def command_build_all():
    """
    using all the current inventory, build all recipes until 
    running out of ingredients.
    """
    num_ingredients_left = len(inv.object_list)    
    total_things_crafted = 0
    can_still_make_stuff = 'Y'

    # try making a recipe
    while can_still_make_stuff == 'Y':
        can_still_make_stuff = 'N'
        for recipe_num, recipe in enumerate(recipes.object_list):
            if do_we_have_ingredients_for_recipe(recipe_num):
                can_still_make_stuff = 'Y'
                total_things_crafted += 1
            command_craft(recipe_num, 'N')
            
    print('Finished Build all - you made ', str(total_things_crafted) + ' items')
    print(inv.str_object_list('N'))

if __name__ == '__main__':
	main()
