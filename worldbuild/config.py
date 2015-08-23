#!/usr/bin/python3
# -*- coding: utf-8 -*-
# config.py

import os

cfg_fldr = root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) 
print('cfg_fldr = ', cfg_fldr)

wiki_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "data" ) 

wiki_pages = [  'overview',
                'history',
                'terrain',
                'vegeation',
                'animals',
                'people',
                'settlements',
                'buildings',
                'history',
             ]

             

