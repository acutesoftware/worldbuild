#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mod_gen_simple.py

import os
import sys
import csv
import mod_utils as md

op_folder = os.path.join(md.fldr_op_mod_root, 'simple' )

op_file_npc = os.path.join(op_folder,'mod_simple_npc.csv')
op_file_item = os.path.join(op_folder,'mod_simple_item.csv')

npcs = [
    'frank','jane','alex','simon','mary'
]

items = ['key','plank']


def main():
    print("generates simple mods from a list in a simplified config file")
    md.verify()
    make_file_npc()
    make_file_items()


def make_file_npc():
    npc_txt = ''
    for npc in npcs:
        npc_txt += md.create_npc_line(npc)

    with open(op_file_npc, 'w') as fop:
        fop.write(npc_txt)

def make_file_items():
    itm_txt = ''
    for itm in items:
        itm_txt += md.create_item_line(itm)

    with open(op_file_item, 'w') as fop:
        fop.write(itm_txt)


main()
    