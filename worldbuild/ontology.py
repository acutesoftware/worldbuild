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
    o = Ontology(file_ontology)
    print(o)


def ont_find(txt):
    o = Ontology(file_ontology)
    res = o.find(txt)
    for line in res:
        print(line)
    print('Found ' + str(len(res)) + ' ontology nodes')


class OntologyItem (object):
    """
    graph_depth,sort_order,node_id,parent_id,node_name,detail,full_path,prefix_for_child_nodes,unique_name,reference_info
    """
    def __init__(self, csv_line):
        self.graph_depth	= int(csv_line[0])
        self.sort_order	= int(csv_line[1])
        self.node_id	= csv_line[2]
        self.parent_id = csv_line[3]
        self.node_name = csv_line[4]
        self.detail = csv_line[5]
        self.full_path = csv_line[6]
        self.prefix_for_child_nodes = csv_line[7]
        self.unique_name = csv_line[8]
        self.reference_info = csv_line[9]

    def __str__(self):
        res = ''
        res += self.parent_id + ' - '
        res += self.node_id + ' ['
        res += self.detail + '] full_path = '
        res += self.full_path
        return res

class Ontology (object):
    def __init__(self, csv_file):
        self.dat = []
        self.csv_file = csv_file
        self.raw_ontology = html_utils.read_csv_to_list(file_ontology)
        for row in self.raw_ontology:
            self.dat.append(OntologyItem(row))
        self.num_nodes = len(self.dat)

    def __str__(self):
        op = 'Ontology from - ' + self.csv_file + '\n'
        for o in self.dat:
            op += str(o) + '\n'
        op += 'Total nodes = ' + str(self.num_nodes)
        return op

    def find(self, txt):
        res = []
        for ont_item in self.dat:
            #print('checking line ' + str(ont_item) + ' for string ' + txt)
            if txt in str(ont_item).upper():
                #print(ont_item)
                res.append(ont_item)
        return res

    def tree_view(self):
        print('show as tree..')
        #sorted_ont = self.dat.sort(key=lambda x:str(x[1]))
        
        for node in self.dat:
            spaces = ' ' * node.graph_depth * 8
            
            print(spaces + node.node_name)
            #print('-' + node.node_name.rjust(spaces))


def ont_help():
    print('\n\nontology.py - utilies for ontology file')
    print('parameters : ')
    print(' -t = show as tree ')
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
    if sys.argv[1] == '-t':
        o = Ontology(file_ontology)
        o.tree_view()

