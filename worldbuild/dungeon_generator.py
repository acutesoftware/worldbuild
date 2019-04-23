#!/usr/bin/python3
# -*- coding: utf-8 -*-
# dungeon_generator.py

import random

grid_x = 120
grid_y = 45
grd = []
ROOM_SIZE_START = 3
ROOM_SIZE_FINISH = 5
ROOM_SIZE_NORMAL = 9

layout = [
    {'name':'start', 'min_x':5, 'min_y':5, 'max_x':5, 'max_y':5, 'marker':'!', 'desc':'Map starting area'},
    {'name':'exit', 'min_x':grid_x-15, 'min_y':grid_y-12, 'max_x':grid_x-2, 'max_y':grid_y - 1, 'marker':'?', 'desc':'Map starting area'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-10, 'max_y':grid_y-4, 'marker':'L', 'desc':'Monster'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-10, 'max_y':grid_y-4, 'marker':'p', 'desc':'Bandit'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-5, 'max_y':grid_y-1, 'marker':'p', 'desc':'Thief'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-5, 'max_y':grid_y-1, 'marker':'r', 'desc':'rat'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-20, 'max_y':grid_y-4, 'marker':'r', 'desc':'rat'},
    {'name':'en1', 'min_x':1, 'min_y':5, 'max_x':grid_x-20, 'max_y':grid_y-4, 'marker':'r', 'desc':'rat'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-10, 'max_y':grid_y-4, 'marker':'L', 'desc':'Monster'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-10, 'max_y':grid_y-4, 'marker':'p', 'desc':'Bandit'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-5, 'max_y':grid_y-1, 'marker':'p', 'desc':'Thief'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-5, 'max_y':grid_y-1, 'marker':'r', 'desc':'rat'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-10, 'max_y':grid_y-4, 'marker':'L', 'desc':'Monster'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-10, 'max_y':grid_y-4, 'marker':'p', 'desc':'Bandit'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-5, 'max_y':grid_y-1, 'marker':'p', 'desc':'Thief'},
    {'name':'en1', 'min_x':5, 'min_y':3, 'max_x':grid_x-5, 'max_y':grid_y-1, 'marker':'r', 'desc':'rat'},
    ]


def main():
    print('generating map')
    create_grid(grid_x,grid_y)
    add_layout(layout)
    print(grid_as_str(grd))


def add_layout(layout):
    """
    add features to map defined by layout
    """
    for l in layout:
        x = random.randint(l['min_x'], l['max_x'])
        y = random.randint(l['min_y'], l['max_y'])
        if l['name'] == 'exit':
            make_room(y,x, ROOM_SIZE_FINISH)
        elif l['name'] == 'start':
            make_room(y,x, ROOM_SIZE_START)
            print('START')
        else:
            make_room(y,x, ROOM_SIZE_NORMAL)
        grd[y][x] = l['marker']


def rnum(max_val=5):
    """
    return a random integer 1 - max_val
    """
    return random.randint(1, max_val)

def make_room(y,x, radius):
    """
    builds a room around a coordinate
    """
    left = y-2-rnum(radius)
    right = y+1+rnum(radius)
    top = x-1-rnum(radius)
    bot = x+2+rnum(radius)
    for r in range(left, right):
        for c in range(top, bot):
            if c < 1: break
            if r < 1: break
            if c > grid_x-1: break
            if r > grid_y-1: break
            if r == left or r == right-1 or c == top or c == bot-1:
                # dont overwrite existing floors (allows rooms to be merged)
                if grd[r][c] != '.':
                    grd[r][c] = '#'
                    print('merging room')
            else:
                grd[r][c] = '.'

def grid_as_str(grd):
    """
    displays a nice grid
    """
    res = ''
    #print(grd)
    top_wall = '/' + ''.join('-' for x in grd[0]) + '\\\n'
    bot_wall = '\\' + ''.join('-' for x in grd[0]) + '/\n'

    res += top_wall
    for row_num, row in enumerate(grd):
        r_str = '|'
        for col_num, col in enumerate(row):
            #print('row_num,col_num = ', row_num,col_num)
            r_str += grd[row_num][col_num]
        r_str += '|'
        res += r_str + '\n'
    res += bot_wall
    return res

def create_grid(x,y):
    for r in range(0,y):
        row = []
        for c in range(0,x):
            row.append(' ')
        grd.append(row)

if __name__ == '__main__':
    main()
