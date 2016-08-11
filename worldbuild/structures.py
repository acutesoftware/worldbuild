#!/usr/bin/python3
# -*- coding: utf-8 -*-
# structures.py

class StructureDefinition(object):
    """
    base class for structure definitions. Application
    specific classes use this as a base class when 
    defining how to implement a structure.
    """
    
    def __init__(self, name, definition):

        assert isinstance(name, str)
        assert not isinstance(definition, str)
        self.name = name
        self.type = ''
        self.definition = definition
        
    def __str__(self):
        res = ''
        res += 'StructureDefinition = ' + self.name + '\n'
        res += ' has ' + str(len(self.definition)) + ' components' + '\n'
        return res
        
class StructureHut(StructureDefinition):
    def __init__(self, name):
        definition = {}
        definition['x1'] = 1
        definition['x2'] = 6
        definition['y1'] = 1
        definition['y2'] = 4
        definition['z1'] = 1
        definition['z2'] = 8       
        StructureDefinition.__init__(self, name, definition)
        self.type = 'shelter'
  
class StructureHouse(StructureDefinition):
    def __init__(self, name, width, height, length):
        definition = {}
        definition['x1'] = 1
        definition['x2'] = width
        definition['y1'] = 1
        definition['y2'] = height
        definition['z1'] = 1
        definition['z2'] = length       
        StructureDefinition.__init__(self, name, definition)
        self.type = 'shelter'
        
