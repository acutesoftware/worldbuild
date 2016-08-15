#!/usr/bin/python3
# -*- coding: utf-8 -*-
# structures.py

def debug(fn):
    def wrapper(*args):
        res = fn(*args)
        print (fn.__name__ + ' ' +  str(args) + ': ' + str(res))
        return res
    return wrapper
  
  

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
        
    @debug
    def __str__(self):
        res = ''
        res += 'StructureDefinition = ' + self.name + '\n'
        res += ' has ' + str(len(self.definition)) + ' components' + '\n'
        a,v = self._calc_size()
        res += ' area   =  ' + str(a)  + '\n'
        res += ' volume =  ' + str(v)  + '\n'
        
        return res
        
        
    def _calc_size(self):
        vol = 'unknown'
        area = 'unknown'
        try:
            area = (self.definition['x2'] - self.definition['x1'] ) * (self.definition['z2'] - self.definition['z1'] )
            vol = area * (self.definition['y2'] - self.definition['y1'])
        except Exception as ex:
            area = ''
            vol = ''
        return area, vol
        
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
        
