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
    def __str__(self):
        res = ''
        res += 'BuildMap '
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
    
    
    