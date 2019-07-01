#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_aikif_agent_explore.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'worldbuild'
sys.path.append(pth)

import aikif_agent_explore


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        aikif_agent_explore.main()
        op_file = os.path.join(pth, 'data', 'world_traversed.txt')
        #print('op_file = ', op_file)
        self.assertTrue(os.path.exists(op_file))


if __name__ == '__main__':
    unittest.main()
