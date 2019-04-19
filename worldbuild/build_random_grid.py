#!/usr/bin/python3
# -*- coding: utf-8 -*-
# build_random_grid.py

import os
import math
from random import randint
import vais.worlds as my_world




def main():
     w = build_world(25, 60, 'test_world.txt')
     print(w)

def build_world(height, width, op_file):
    num_seeds   =   6   # number of seed points to start land generation
    perc_land   =  20   # % of world that is land
    perc_sea    =  80   # % of world that is sea
    perc_blocked=   4   # % of world that is blocked

    myWorld = my_world.World( height, width, ['.','X','#'])  # TODO - fix passing
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    myWorld.grd.save(op_file)
    return myWorld


if __name__ == '__main__':
	main()
