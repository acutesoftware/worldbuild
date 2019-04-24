#!/usr/bin/python3
# -*- coding: utf-8 -*-
# dungeon_generator.py

import sys
import random

grid_x = 128
grid_y = 48
grd = []
NUM_ROOMS = 18
ROOM_SIZE_START = 12
ROOM_SIZE_FINISH = 12
ROOM_SIZE_NORMAL = 7
PATH_NUM_HORIZ = 14
PATH_NUM_VERT = 5
PATH_NUM_VERT_PERC_DROP = 10
PATH_NUM_HORIZ_PERC_DROP = 60



EXIT_X = -1
EXIT_Y = -1
START_X = -1
START_Y = -1

SEED = 1633707415 #8392900704256678713 # 1633707415 # 351

TILESET = ' 1234.6789+-#' # note leading space, so 'box' is drawn as per numeric keypad
TILESET = ' ####.####+-#'
TILESET = ' \_/|.|/-\+-#'
TILESET = ' ╚═╝║.║╔═╗+-#'

"""
TILESET  = ' ' + u'\u255A' +  u'\u2550' + u'\u255D'
TILESET +=       u'\u2551' +  '.'       + u'\u2551'
TILESET +=       u'\u2554' +  u'\u2550' + u'\u2557' + '+-#'
"""


TILE_BLANK              = TILESET[0]
TILE_WALL_BOTTOM_LEFT   = TILESET[1]
TILE_WALL_BOTTOM        = TILESET[2]
TILE_WALL_BOTTOM_RIGHT  = TILESET[3]
TILE_WALL_LEFT          = TILESET[4]
TILE_FLOOR              = TILESET[5]
TILE_WALL_RIGHT         = TILESET[6]
TILE_WALL_TOP_LEFT      = TILESET[7]
TILE_WALL_TOP           = TILESET[8]
TILE_WALL_TOP_RIGHT     = TILESET[9]
TILE_DOOR_CLOSED_VERT   = TILESET[10]
TILE_DOOR_OPEN_VERT     = TILESET[11]
TILE_DOOR_FRAME_VERT    = TILESET[12]


MONSTERS = 'pLrcF'
layout = []
for i in range(NUM_ROOMS):
    m = random.choice(MONSTERS)
    layout.append({'name':'en1', 'min_x':8, 'min_y':5, 'max_x':grid_x-8, 'max_y':grid_y-4, 'marker':m})

layout.append({'name':'start', 'min_x':3, 'min_y':5, 'max_x':5, 'max_y':5, 'marker':'!', 'desc':'Map starting area'})
layout.append({'name':'exit', 'min_x':grid_x-15, 'min_y':grid_y-12, 'max_x':grid_x-2, 'max_y':grid_y - 1, 'marker':'?', 'desc':'Map starting area'})

def main():

    SEED = random.randrange(sys.maxsize)
    random.seed(SEED)
    create_grid(grid_x,grid_y)
    add_layout(layout)
    add_corridors()
    add_walls()
    print(grid_as_str(grd))
    #print(grd)
    print("Seed was:", SEED)

def add_walls():
    """
    traces the entire map and puts walls around all '.' which are
    either rooms or corridors
     ?--?     ?   ?
     |..|       ..+       ..
     ?--?

    """

    for r in range(0, grid_y-1):
        for c in range(0, grid_x-1):

            # BOTTOM wall
            if grd[r][c] == TILE_FLOOR and grd[r+1][c] == TILE_BLANK:
                grd[r+1][c] = TILE_WALL_BOTTOM # '?'  #TOK

            # TOP wall
            if grd[r][c] == TILE_FLOOR and grd[r-1][c] == TILE_BLANK:
                grd[r-1][c] = TILE_WALL_TOP # '?'  # top wall is thinner  ?

            # RIGHT wall
            if grd[r][c] == TILE_FLOOR and grd[r][c+1] == TILE_BLANK:
                grd[r][c+1] = TILE_WALL_RIGHT # '?'

                if grd[r-1][c+1] == TILE_BLANK and grd[r-1][c+1] != TILE_FLOOR: # add Top RIGHT corner - outer (TOK)
                    grd[r-1][c+1] = TILE_WALL_TOP_RIGHT #'?'  # ? ? ? ?  ? ?  ? ? ? ? ? ? ? ?

                if grd[r+1][c+1] == TILE_BLANK and grd[r+1][c] != TILE_FLOOR: # add bottom right corner - outer (TOK)
                    grd[r+1][c+1] = TILE_WALL_BOTTOM_RIGHT

            # LEFT wall
            if grd[r][c] == TILE_FLOOR and grd[r][c-1] == TILE_BLANK:
                grd[r][c-1] = TILE_WALL_LEFT # '?'

                if grd[r-1][c-1] == TILE_BLANK and grd[r-1][c-1] != TILE_FLOOR: # add Top Left corner - outer (TOK)
                    grd[r-1][c-1] = TILE_WALL_TOP_LEFT

                if grd[r+1][c-1] == TILE_BLANK and grd[r+1][c] != TILE_FLOOR: # add Bottom Left corner - outer (TOK)
                    grd[r+1][c-1] = TILE_WALL_BOTTOM_LEFT

    # Now fix the INSIDE corners (walls all set, but inside corners show up as VERT)
    for r in range(0, grid_y-1):
      for c in range(0, grid_x-1):
        if grd[r][c] == TILE_WALL_LEFT and grd[r][c+1] != TILE_FLOOR and grd[r+1][c] == TILE_FLOOR:
            grd[r][c] = TILE_WALL_BOTTOM_LEFT
        if grd[r][c] == TILE_WALL_TOP and grd[r][c+1] != TILE_FLOOR and grd[r][c-1] == TILE_FLOOR:
            grd[r][c] = TILE_WALL_TOP_LEFT
        if grd[r][c] == TILE_WALL_LEFT and grd[r][c-1] != TILE_FLOOR and grd[r][c-1] != TILE_BLANK and grd[r+1][c] != TILE_WALL_LEFT:
            grd[r][c] = TILE_WALL_BOTTOM_RIGHT

        if grd[r][c] == TILE_WALL_TOP and grd[r][c-1] != TILE_FLOOR and grd[r][c+1] == TILE_FLOOR:
            grd[r][c] = TILE_WALL_TOP_RIGHT



def add_corridors():
    """
    randomly add corridors hor and vert only, to join big rooms
    """

    passages = create_passage_list()

    for passage in passages:
        print(passage)
        for x in range(passage['start_x'], passage['end_x']):
            grd[passage['y']][x+1] = TILE_FLOOR
        grd[passage['y']][passage['start_x']+1] = TILE_DOOR_OPEN_VERT #'+'

        if grd[passage['y']-1][passage['start_x']+1] == TILE_BLANK:
            grd[passage['y']-1][passage['start_x']+1] = TILE_DOOR_FRAME_VERT
        if grd[passage['y']+1][passage['start_x']+1] == TILE_BLANK:
            grd[passage['y']+1][passage['start_x']+1] = TILE_DOOR_FRAME_VERT

        grd[passage['y']][passage['end_x']] = TILE_DOOR_CLOSED_VERT #'-'

        if grd[passage['y']-1][passage['end_x']] == TILE_BLANK:
            grd[passage['y']-1][passage['end_x']] = TILE_DOOR_FRAME_VERT
        if grd[passage['y']+1][passage['end_x']] == TILE_BLANK:
            grd[passage['y']+1][passage['end_x']] = TILE_DOOR_FRAME_VERT



def create_passage_list():
    """
    looks at the map and makes a list of places where corridors
    should exist
    """
    passages = []
    cur_y = 2
    for y in range(PATH_NUM_HORIZ):
        cur_y += rnum(int(grid_y / PATH_NUM_HORIZ)) + 2
        if cur_y > grid_y - 4:
            break

        passages.extend(get_path_end_points_HORIZ(cur_y))
    #print('START_Y = ', START_Y)
    #print('EXIT_Y = ', EXIT_Y)
    passages.extend(get_path_end_points_HORIZ(START_Y))  # starting horiz
    passages.extend(get_path_end_points_HORIZ(EXIT_Y))  # end horiz

    return passages

def get_path_end_points_HORIZ(cur_y):
    """
    PATH_NUM_HORIZ = 10
    PATH_NUM_VERT = 5
    PATH_NUM_VERT_PERC_DROP = 10
    PATH_NUM_HORIZ_PERC_DROP = 10
    """
    horiz_paths = []

    # we make a passage BETWEEN 2 rooms only
    mode = 'NONE'
    start_x = 0
    end_x = grid_x
    for x in range(2, grid_x-1):
        #print('y,x = ', cur_y, x, mode, grd[cur_y][x],  grd[cur_y][x+1])
        if grd[cur_y][x] == TILE_FLOOR and grd[cur_y][x+1] == TILE_BLANK:
            mode = 'PATH'  # start of path
            start_x = x
        if grd[cur_y][x] == TILE_BLANK and grd[cur_y][x+1] == TILE_FLOOR and mode == 'PATH':
            mode = 'END'
            end_x = x
            if random.randint(1,100) > PATH_NUM_HORIZ_PERC_DROP:   # skip about half the horiz tunnels
                horiz_paths.append({'y':cur_y,'start_x':start_x,'end_x':end_x})
            start_x = 0
            end_x = grid_x

    return horiz_paths


def add_layout(layout):
    """
    add features to map defined by layout

           ╔═══════╗
           ║.......║
           ║.......║
           ║.......║
           ║....p..║
           ║.......║
           ║.......║
           ║.......║
           ╚═══════╝
    """
    global START_Y, START_X, EXIT_X, EXIT_Y

    for l in layout:
        if l['min_x']  > l['max_x'] - 3:
            if not l['name'] in ['start', 'exit']:
                break
        x = random.randint(l['min_x'], l['max_x'])
        y = random.randint(l['min_y'], l['max_y'])


        print('add_layout: x,y,layout = ', x,y,str(l))

        if l['name'] == 'exit':
            make_room(y,x, ROOM_SIZE_FINISH, l['name'])
            EXIT_X = x
            EXIT_Y = y
        elif l['name'] == 'start':
            make_room(y,x, ROOM_SIZE_START, l['name'])
            START_X = x
            START_Y = y
        else:
            make_room(y,x, ROOM_SIZE_NORMAL, l['name'])
        grd[y][x] = l['marker']


def rnum(max_val=5):
    """
    return a random integer 1 - max_val
    """
    return random.randint(1, max_val)

def make_room(y,x, radius, nme):
    """
    builds a room around a coordinate
    """
    if nme  == 'start':
        left = x-9-rnum(radius)
        right = x+2+rnum(radius)
        top = y-99-rnum(radius)
        bot = y+2+rnum(radius)
    elif nme  == 'exit':
        left = x-2-rnum(radius)
        right = x+99+rnum(radius)
        top = y-2-rnum(radius)
        bot = y+99+rnum(radius)

    else:
        left = x-2-rnum(radius)
        right = x+2+rnum(radius)
        top = y-2-rnum(radius)
        bot = y+2+rnum(radius)

    #print('make_room : left,right,top,bot,grid_y,grid_x    = ', left,right,top,bot,grid_y,grid_x)

    """
    validations
    """
    if left < 2:
        left = 2
    if right > grid_x:
        right = grid_x - 2
    if bot > grid_y - 2:
        bot = grid_y - 2
    if top < 2:
        top = 2

    #print('make_room AFTER validations: left,right,top,bot = ', left,right,top,bot)

    for r in range(top, bot):
        for c in range(left, right):
            if c < 1: c =  0
            if r < 1: r = 0
            #if c > grid_x-1: break
            #if r > grid_y-1: break
            if r == left or r == right-1 or c == top or c == bot-1:
                # dont overwrite existing floors (allows rooms to be merged)
                if r < grid_y-1 and c < grid_x-1:
                    if grd[r][c] != TILE_FLOOR:
                        pass
                        #grd[r][c] = '#'
                        #print('merging room')
            else:
                if r < grid_y and c < grid_x:
                    grd[r][c] = TILE_FLOOR # '.'

def grid_as_str(grd):
    """
    displays a nice grid
    """
    res = ''
    top_wall = '/' + ''.join('-' for x in grd[0]) + '\\\n'
    bot_wall = '\\' + ''.join('-' for x in grd[0]) + '/\n'

    res += top_wall
    for row_num, row in enumerate(grd):
        r_str = '|'
        for col_num, col in enumerate(row):
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
