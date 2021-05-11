#!/usr/bin/python3
# -*- coding: utf-8 -*-
# wb_utils.py

import os
import csv



def get_fullname(fname):
    """
    gets full filename of crafting data from this folder
    """

    root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

    return os.path.join(root_folder,'data', fname)


def read_csv_to_list(filename):
    """
    reads a CSV file to a list
    """
    import csv

    rows_to_load = []
    with open(filename, 'r', encoding='cp1252') as csvfile: # sort of works with , encoding='cp65001'
        reader = csv.reader(csvfile)
        rows_to_load = list(reader)
    return rows_to_load[1:], rows_to_load[0]

def save_list_to_csv(lst, filename):
    """
    takes a list and saves to CSV
    """

    with open(filename, 'w', encoding='UTF-8') as f:
        for row in lst:
            for col in row:
                if col:
                    f.write( '"' + str(col) + '",')
                else:
                    f.write('"",')
            f.write('\n')
