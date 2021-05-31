#!/usr/bin/python3
# -*- coding: utf-8 -*-
# skills.py

import os
import random
from pprint import pprint

from treelib import Node, Tree
import wb_utils 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

def main():
    print('showing skills tree')
    tree = Tree()
    #tree.create_node("all_skills", "all_skills")  # root node
    skills_list, hdr_skills_list = wb_utils.read_csv_to_list(wb_utils.get_fullname('skills_tree.csv'))
    print_list = [] 
    for sk in skills_list:
        this_skill = sk[1] + ' - ' + sk[0]
        print(this_skill)
        if sk[1] == '':
            tree.create_node(tag=sk[0], identifier=sk[0], parent=None, data=[sk[1],sk[2]])
        else:
            tree.create_node(tag=sk[0], identifier=sk[0], parent=sk[1], data=[sk[1],sk[2]])
            
    tree.show()
    tree.save2file('skills_tree.txt')

    #for op in sorted(print_list):
    #    print(op)


if __name__ == '__main__':
	main()
