#!/usr/bin/python3
# -*- coding: utf-8 -*-
# skills.py

import os
import wb_utils 
import random


root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

def main():
    print('showing skills tree')
    skills_list, hdr_skills_list = wb_utils.read_csv_to_list(wb_utils.get_fullname('skills_tree.csv'))
    print_list = [] 
    for sk in skills_list:
        this_skill = sk[1] + ' - ' + sk[0]
        print_list.append([this_skill])

    for op in sorted(print_list):
        print(op)


if __name__ == '__main__':
	main()
