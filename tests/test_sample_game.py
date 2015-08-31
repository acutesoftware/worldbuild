#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_sample_yaml.py
import os
import sys
import unittest
import pprint

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

import sample


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_read_yaml_game(self):
        fle = os.path.join(pth, 'samples', 'game.yaml')
        
        # _print_yaml(fle)  # works
        y = sample._read_yaml(fle)
        #pprint.pprint(y)
        # {'Monsters': [{'ac': 16,
                       # 'attacks': ['BITE', 'HURT'],
                       # 'hp': [2, 6],
                       # 'name': 'Cave spider'},
                      # {'ac': 26,
                       # 'attacks': ['CRUSH', 'HIT'],
                       # 'hp': [5, 7],
                       # 'name': 'Troll'}]}    
        
        self.assertTrue(len(str(y)) > 600)
        
        #for m in y['Monsters']:
        #    print(m['name'], m['attacks'])
            # > Cave spider ['BITE', 'HURT']
            # > Troll ['CRUSH', 'HIT']
            
        self.assertEqual(y['Monsters'][0]['ac'], 16)
        self.assertEqual(y['Monsters'][1]['ac'], 26)
       
        self.assertEqual( y['Objects'][3], 'Cheese')
        
        #pprint.pprint(sample.convert_yaml_to_json(fle))
        #pprint.pprint(sample.convert_json_to_yaml(''))
        
        
        self.assertEqual(y['actions'][0]['name'], 'Smite')
        self.assertEqual(y['actions'][1]['name'], 'Fireball')
        self.assertEqual(y['actions'][2]['name'], 'Magic Missile')
        
     


        self.assertTrue(os.path.exists(fle))

 
if __name__ == '__main__':
    unittest.main()

