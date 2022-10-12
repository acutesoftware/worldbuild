#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ontology.py
#
# Utilities to check the upper ontology for both game information
# and real world data

import os
import sys
import html_utils

file_ontology = os.path.join(os.getcwd(), 'data', 'ontology.csv')

def ont_list():
    print('reading ontology from ' + file_ontology )
    lst = html_utils.read_csv_to_list(file_ontology)
    #print(lst)
    for l in lst:
        o = OntologyItem(l)
        print(o)


def ont_find(txt):
    lst = html_utils.read_csv_to_list(file_ontology)
    for l in lst:
        o = OntologyItem(l)
        if txt in str(l).upper():
            print(o)

class OntologyItem (object):
    def __init__(self, csv_line):
        self.node_id	= csv_line[2]
        self.parent_id = csv_line[3]
        self.node_name = csv_line[4]
        self.detail = csv_line[5]
        self.full_path = csv_line[6]

    def __str__(self):
        res = ''
        res += self.parent_id + ' - '
        res += self.node_id + ' ['
        res += self.detail + '] full_path = '
        res += self.full_path
        return res





def ont_help():
    print('\n\nontology.py - utilies for ontology file')
    print('parameters : ')
    print(' -c = checks for mismatched entries ')
    print(' -f [txt] = lists entries containing "txt" ')
    

    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        ont_list()
        ont_help()
        exit(0)
    if sys.argv[1] == '-c':
        print('checking file...')
    if sys.argv[1] == '-f':
        #print('finding ' + sys.argv[2])
        ont_find(sys.argv[2].upper())

