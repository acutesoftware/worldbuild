#!/usr/bin/python3
# -*- coding: utf-8 -*-
# world_builder.py



class BuildMap(object):
    """
    Base class to actually build a map which is defined 
    by the 'World' object or Grid (to be decided).
    This can mean printing the grid, display as image, 
    create the map in Minecraft or create in other virtual
    environments.
    """
    def __init__(self, struct_data, style):
        """
        struct_data = details of coords to fill, make  
        style = details on colours, textures, if applicable
        
        The assert checks that both are NOT strings, but should
        be iterable lists / dicts or subclasses of 
        """
        assert not isinstance(struct_data, str)
        assert not isinstance(style, str)
    
        self.struct_data = struct_data
        self.style =  style
    
    def __str__(self):
        res = ''
        res += 'BuildMap ' + '\n'
        if type(self.struct_data) is list:
            for l in self.struct_data:
                res += 'data:' + str(l) + '\n'
        else:   # assume dictionary
            for k,v in self.struct_data.items():
                res += 'data:' + str(k) + ' = ' + str(v) + '\n'
                
                
        if type(self.style) is list:
            for l in self.style:
                res += 'style:' + str(l) + '\n'
        else:   # assume dictionary
            for k,v in self.style.items():
                res += 'style:' + str(k) + ' = ' + str(v) + '\n'
                
                
                
        return res

class BuildMapMineCraft(BuildMap):
    """
    Interface with Minecraft (currently via sendkeys to server)
    to create objects in the Minecraft world.
    """
    def build(self, ip_file):
        import minecraft_builder
        minecraft_builder.make_structure(ip_file)

    

class BuildMapGrid(BuildMap):
    """
    Not much to do here, simply returns a standard grid or 
    CSV formatted file of the world
    to create objects in the Minecraft world.
    """
    pass
    
    
class BuildMapImage(BuildMap):
    """
    Generates an image of the world, which is a 2d grid, or 
    multiple images if multiple floors (not much point calling this 
    for a proper 3d world ( Unity) , but useful for castle/dungeon 
    game maps with multiple floors.
    """
    pass
    
    
    