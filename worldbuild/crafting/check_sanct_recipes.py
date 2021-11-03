#!/usr/bin/python3
# -*- coding: utf-8 -*-
# check_recipes.py
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

import random

def get_fullname(fname):
    """
    gets full filename of crafting data from this folder
    """
    return os.path.join(root_folder,'data','sanct_game', fname)

def main():
    # setup the main dataset definitions here
    items = DataSet(Item, get_fullname('ItemList.csv'))
    recipes = DataSet(Recipe, get_fullname('DT_craft_recipes.csv'))
    ingred = DataSet(RecipeIngredient, get_fullname('DT_craft_recipe_ingredients.csv'))
    methods = DataSet(CraftingMethod, get_fullname('DT_craft_methods.csv') )

    print(items)
    print(recipes)
    print(ingred)
    print(methods)
    print('Checking recipes against items and ingredients....')
    recipes_no_ingred = []
    recipes_no_ingred = []
    recipes_not_in_inventory = []
    for recipe in recipes.object_list:
        num_ingred = 0
        #print('--------ingredients ----------')
        for ing in ingred.object_list:
            if ing.recipe_id == recipe.recipe_id:
                #print(ing.crafting_method_id + ' ' + ing.quantity + ' ' + ing.item_id)
                num_ingred += 1
        if num_ingred < 1:
            print('recipe missing ingredients ' + recipe.recipe_name)  
            recipes_no_ingred.append(recipe)      

        exists_in_inv = 0
        for itm in items.object_list:
            if itm.item_id == ing.item_id:
                exists_in_inv += 1
        if exists_in_inv == 0:
            recipes_not_in_inventory.append(recipe)

    print('recipes_not_in_inventory = ' + str(len(recipes_not_in_inventory))) 
    for r in recipes_not_in_inventory:
        print(r)


    items_that_can_be_crafted = []
    items_used_in_crafting = []
    for itm in items.object_list:
        for ing in ingred.object_list:
            if itm.item_id == ing.item_id:
                items_used_in_crafting.append(itm)

        for recipe in recipes.object_list:
            if itm.item_id == recipe.recipe_id:
                    items_that_can_be_crafted.append(itm)


    print('Total items = ' + str(len(items.object_list)))
    print('items_that_can_be_crafted = ' + str(len(items_that_can_be_crafted)))
    print('items_used_in_crafting = ' + str(len(items_used_in_crafting)))
    

class DataSet(object):
    """
    handles a collection of Objects loaded from a reference file
    """
    def __init__(self, objectClass, fname):
        self.raw_data = []
        self.object_list = []
        self.fname = fname
        self.objectClass = objectClass  # Recipe, Item, RecipeIngredient
        self.column_headings = []
        self.fill_from_csv(self.fname)
        self.rebuild_list()


    def __str__(self):
        #return ''.join([d for d in self.raw_data])
        res = 'Dataset containing ' + str(len(self.object_list))
        res += ' ' + str(self.objectClass.__name__) + ' objects'
        return res
    def str_object_list(self, show_number='Y'):
        """
        returns full object list formatted by object definition __str__
        """
        res = '    -=< ' + str(self.objectClass.__name__) + ' >=-\n'
        res += '/=======================\\\n'
        for obj_num, obj in enumerate(self.object_list):
            if show_number == 'Y':
                res += '  ' + str(obj_num+1) + ' - ' + str(obj) + '\n'
            else:
                res += '  ' + str(obj) + '\n'
        res += '\\=======================/\n'
        return res


    def fill_from_csv(self, fname):
        with open(fname, 'r') as fip:
            for line in fip:
                self.raw_data.append(line.strip('\n'))

    def rebuild_list(self):
        self.object_list = []  # clear the object list
        for line_num, raw_line in enumerate(self.raw_data):
            if raw_line.strip(' ') != '':
                cols = raw_line.split(',')
                if line_num == 0:
                    self.column_headings = cols
                else:
                    #print('RECIPE DATA = ', cols)
                    cur_obj = self.objectClass(*cols) # cols[0], cols[1], cols[2], cols[3])
                    self.object_list.append(cur_obj)
                    #print('object = ' + str(cur_obj))


class Recipe(object):
    """
    Recipe
    """
    def __init__(self, ue4id, recipe_id, recipe_name,base_time_to_build,base_cost_to_build,num_produced_per_craft,tools_or_workbench_required):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.base_time_to_build =  base_time_to_build
        self.base_cost_to_build =  base_cost_to_build
        
    def __str__(self):
        res = self.recipe_name
        return     res   


class Item(object):
    """
    Items / objects that are in the world. Can be collected
    or crafted
    """
    def __init__(self,ue4id, ID, Name,Description,Quality,Icon,ItemType,Amount,IsStackable,MaxStackSize,IsDroppable,WorldMesh,Health,Duration,WeaponActorClass,EquipmentMesh,EquipmentType,EquipmentSlot,Damage,Armor,Strength,Dexterity,Intelligence):
        self.item_id = ID
        self.name = Name
        self.desc = Description
        
    def __str__(self):
        res = ''
        res += self.name + ' - ' + self.desc
        return     res   

class ItemSpawnRate(object):
    """
    Items that spawn in the world
    """
    def __init__(self,name,quant):
        self.name = name
        self.quant = quant
        
    def __str__(self):
        res = ''
        res += self.name + ' - ' + self.quant
        return     res   


class RecipeIngredient(object):
    """
    multiple ingreds per recipe
    recipe_id,item_id,quantity,crafting_method_id
    """
    def __init__(self, ue4id, recipe_id,item_id,quantity,crafting_method_id):
        self.recipe_id = recipe_id
        self.item_id = item_id
        self.quantity =  quantity
        self.crafting_method_id =  crafting_method_id
        
    def __str__(self):
        res = ''
        res += self.recipe_id + ' - ' + self.item_id + ' (' + str(self.quantity) + ')'

        return     res   

class CraftingMethod(object):
    """
    craft_method_id,craft_action,base_time,base_cost,tools_required,consumables_required,skill_areas
    """
    def __init__(self,ue4id, craft_method_id,craft_action,base_time,base_cost,tools_required,consumables_required,skill_areas):
        self.crafting_method_id =  craft_method_id
        self.crafting_action = craft_action
        self.base_time = base_time
        self.base_cost = base_cost
        self.tools_required = tools_required
        self.consumables_required = consumables_required
        self.skill_area =  skill_areas
        
    def __str__(self):
        res = ''
        res += self.crafting_method_id + ' - ' + self.crafting_action
        if self.tools_required:
            tools_needed = self.tools_required + ' and skill in '
        else:
            tools_needed = 'no tools, but skill in '

        res += ' (needs ' + tools_needed + self.skill_area + ')'

        return     res   





if __name__ == '__main__':
	main()
