#!/usr/bin/python3
# -*- coding: utf-8 -*-
# generate_tools.py

import os
import wb_utils 
import random


root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )


def generate_random_item_list(num_items):
    """
    Top level function to generate list of items
    """

    tools_base_list, hdr_tool_list = wb_utils.read_csv_to_list(wb_utils.get_fullname('tools_base.csv'))
    base_mat_list, hdr_mat_list =  wb_utils.read_csv_to_list(wb_utils.get_fullname('item_base_materials.csv'))

    

    print('generating ' + str(num_items) + ' items')
    for num in range(0, num_items):
        base_tool = random.choice(tools_base_list)
        mat = random.choice(base_mat_list)
        t = Tool()
        t.init_from_cols(base_tool)
        new_mat = Material()
        new_mat.init_from_cols(mat)
        new_tool = Tool()
        new_tool.init_from_cols(base_tool)
        new_tool.tool_name = new_mat.base_material_name + ' ' + t.tool_name 
        new_tool.add_random_post_modifier()
        new_tool.durability = new_mat.durability
        print('NEW TOOL ' + str(new_tool))


def generate_all_combinations():
    new_tool_list = []
    tools_base_list, hdr_tool_list = wb_utils.read_csv_to_list(wb_utils.get_fullname('tools_base.csv'))
    base_mat_list, hdr_mat_list =  wb_utils.read_csv_to_list(wb_utils.get_fullname('item_base_materials.csv'))
    for base_tool in tools_base_list:
        for mat in base_mat_list:
            t = Tool()
            t.init_from_cols(base_tool)
            for mod_num in range(0, len(t.modifiers)):
                new_mod = t.modifiers[mod_num]
                new_mat = Material()
                new_mat.init_from_cols(mat)
                new_tool = Tool()
                new_tool.init_from_cols(base_tool)
                if new_mod == '':
                    new_tool.tool_id = new_mat.item_base_material_id + '_' + t.tool_id
                else:
                    new_tool.tool_id = new_mat.item_base_material_id + '_' + t.tool_id + '_' + new_mod.replace(' of ', '').lower()
                new_tool.tool_name = new_mat.base_material_name + ' ' + t.tool_name 

                new_tool.add_random_post_modifier(mod_num)
                new_tool.durability = new_mat.durability
                print(str(new_tool))
                new_tool_list.append(new_tool.get_list())
    wb_utils.save_list_to_csv(new_tool_list, 'all_tools_list.csv')
            

class Tool(object):
    def __init__(self):
        self.tool_id = 'tool_id'
        self.tool_name = 'Tool Name'
        self.base_dmg = 0
        self.base_dig = 0
        self.base_wgt  = 0
        self.base_speed = 0
        self.durability  = 0
        self.modifiers = [
            '',
            ' of Agility',
            ' of Toughness',
            ' of Speed'
        ]  

    def __str__(self):
        res = ''
        #res += self.tool_id + ','
        res += self.tool_name + ', dmg='
        res += str(self.base_dmg) + ', dig='
        res +=  str(self.base_dig) + ', weight='
        res +=  str(self.base_wgt) + ', speed='
        res +=  str(self.base_speed) + ', durability='
        res +=  str(self.durability) + ''
        return res

    def get_list(self):
        return [self.tool_id, self.tool_name, self.base_dmg, self.base_dig, self.base_wgt, self.base_speed, self.durability ]

    def format_csv(self):
        """
        return a CSV line of the tool for export
        """
        res = '"'
        res += self.tool_id + '","'
        res += self.tool_name + '","'
        res += str(self.base_dmg) + '","'
        res +=  str(self.base_dig) + '","'
        res +=  str(self.base_wgt) + '","'
        res +=  str(self.base_speed) + '","'
        res +=  str(self.durability) + '"'
        return res

    def init_from_cols(self, cols):
        self.tool_id = cols[0]
        self.tool_name = cols[1]
        self.base_dmg = int(cols[2])
        self.base_dig = int(cols[3])
        self.base_wgt  = int(cols[4])
        self.base_speed = int(cols[5])
        self.durability  = int(cols[6])

    def add_random_post_modifier(self, num=-1):
        if num == -1:
            res = random.choice(self.modifiers)       
        else:
            res = self.modifiers[num]
        self.tool_name += res
        if 'Speed' in res:
            self.base_speed += 3
        if 'Toughness' in res:
            self.durability += 3


class Material(object):
    def __init__(self):
        self.item_base_material_id = ''
        self.base_material_name = ''
        self.durability = 0
    def __str__(self):
        return self.base_material_name
    def init_from_cols(self, cols):
        self.item_base_material_id = cols[0]
        self.base_material_name = cols[1]
        self.durability = int(cols[2])
    

if __name__ == '__main__':
	#generate_random_item_list(7)    
    generate_all_combinations()
