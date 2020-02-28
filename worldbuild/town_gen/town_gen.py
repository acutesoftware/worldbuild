#!/usr/bin/python3
# -*- coding: utf-8 -*-
# town_gen.py

import random 

def TEST():
    print('generating town...')
    dat_town = make_town(4)
    print_town(dat_town)


def make_town(sze):
    """
    generates the town
    [1,1,1,1,1,1,1]
    """
    dat = []

    buildings = 'HSP'

    for s in range(sze):
        current_building = random.choice(buildings)
        dat.append([s, current_building])


    return dat
    



def print_town(dat_town):
    """
    prints the town to console
    """
    print(dat_town)




if __name__ == '__main__':
    TEST()

