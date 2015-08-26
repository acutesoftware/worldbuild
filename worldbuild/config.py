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

             
culture_categories = [
     {'surface':'food'},
     {'surface':'language'},
     {'deep':'communicates_gestures'},
     {'deep':'communicates_tone_of_voice'},
     {'deep':'communicates_eye_contact'},
     {'deep':'attitues_elders'},
     {'deep':'attitudes_religion'},
     {'deep':'attitudes_nature'},
     ]

for c in culture_categories:
    print(str(c))

groups_of_people_categories = {
    'location':'location on the map',
    'race':'race of this group, if applicable',
    'political_leaning':'politics of this group, if applicable',
    'religious_leaning':'religion of this group, if applicable',
    }
    
print(groups_of_people_categories)    