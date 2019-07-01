#!/usr/bin/python3
# -*- coding: utf-8 -*-
# dungeon_generator.py

import sys
import random
import worldbuild.pathfind as pathfind
import worldbuild.convert_grid_to_tiled_map as convert_grid_to_tiled_map

grd = []

ROOM_SIZE_START = 8
ROOM_SIZE_FINISH = 8


PATH_NUM_VERT = 5
PATH_NUM_VERT_PERC_DROP = 10
PATH_NUM_HORIZ_PERC_DROP = 40



EXIT_X = -1
EXIT_Y = -1
START_X = -1
START_Y = -1


TILESET = ' 1234.6789+-#' # note leading space, so 'box' is drawn as per numeric keypad
TILESET = ' ####.####+-#'
TILESET = ' \_/|.|/-\+-#'
TILESET = ' ╚═╝║.║╔═╗+-#'

"""
TILESET  = ' ' + u'\u255A' +  u'\u2550' + u'\u255D'
TILESET +=       u'\u2551' +  '.'       + u'\u2551'
TILESET +=       u'\u2554' +  u'\u2550' + u'\u2557' + '+-#'
"""
csv_export_file = 'dungeon.csv'

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



def main():

    grid = create_dungeon()
    print(grid_as_str(grid))

    # optional - make a path through the grid
    print(path_find(grid))

    # optional - export as TMX file
    convert_grid_to_TileEditor_map('dungeon.tmx', 'samples/ascii_runeset.tsx')


def create_dungeon(grid_y=30, grid_x=80, NUM_ROOMS=16, ROOM_SIZE = 3, NUM_HORIZ = 10, lv_SEED = -1):
    if grid_x < 30:
        grid_x = 30
    if grid_y < 15:
        grid_y = 15

    if lv_SEED == -1:
        SEED = random.randrange(sys.maxsize)
    else:
        SEED = 1633707415 #8392900704256678713 # 1633707415 # 351
        SEED = 2951322320659409853  # simple path, 96x96 (saved as dungeon_map_solved_v1.txt) 18 rooms, 12
        SEED = 1612603902922459220  # good for pathfinding with 64 x 64
        SEED = 3320746558832866108  # 128x48, 30 rooms, 4 wide, 12 hor cor, 40pc chance drop
        SEED = 5529128865878819600

    random.seed(SEED)
    print('SEED=',SEED )

    MONSTERS = 'pLrcF'
    layout = []
    for i in range(NUM_ROOMS):
        m = random.choice(MONSTERS)
        layout.append({'name':'en1', 'min_x':8, 'min_y':5, 'max_x':grid_x-8, 'max_y':grid_y-4, 'marker':m})

    layout.append({'name':'start', 'min_x':3, 'min_y':5, 'max_x':5, 'max_y':5, 'marker':'!', 'desc':'Map starting area'})
    layout.append({'name':'exit', 'min_x':grid_x-15, 'min_y':grid_y-12, 'max_x':grid_x-2, 'max_y':grid_y - 1, 'marker':'?', 'desc':'Map starting area'})


    create_grid(grid_x,grid_y)
    add_layout(layout, grid_y, grid_x, ROOM_SIZE)
    add_corridors(grid_y, grid_x, NUM_HORIZ)
    add_walls(grid_y, grid_x)
    return grd




def convert_grid_to_TileEditor_map(op_file, tileset_file_def):
    """
    202,206,188,39,
    187,251, 46, 0,
    201,44, 189,39,
    tileset_index = { # for Runeset_32x32.png (ascii_runeset)
        ' ': -1,  # TILE_BLANK
        ' ': -1,  # TILE_WALL_BOTTOM_LEFT
        ' ': -1,  # TILE_WALL_BOTTOM
        ' ': -1,  # TILE_WALL_BOTTOM_RIGHT
        ' ': -1,  # TILE_WALL_LEFT
        ' ': -1,  # TILE_FLOOR
        ' ': -1,  # TILE_WALL_RIGHT
        ' ': -1,  # TILE_WALL_TOP_LEFT
        ' ': -1,  # TILE_WALL_TOP
        ' ': -1,  # TILE_WALL_TOP_RIGHT
        ' ': -1,  # TILE_DOOR_CLOSED_VERT
        ' ': -1,  # TILE_DOOR_OPEN_VERT
        ' ': -1,  # TILE_DOOR_FRAME_VERT
    }


    """



    tileset_index = { # for Runeset_32x32.png (ascii_runeset)
        TILE_BLANK: 0,
        TILE_WALL_BOTTOM_LEFT:201,
        TILE_WALL_BOTTOM: 206,
        TILE_WALL_BOTTOM_RIGHT: 189,
        TILE_WALL_LEFT:187,
        TILE_FLOOR: 251,
        TILE_WALL_TOP_LEFT:202,
        TILE_WALL_TOP_RIGHT:188,
        TILE_DOOR_CLOSED_VERT:46,
        TILE_DOOR_OPEN_VERT:44,
        TILE_DOOR_FRAME_VERT:39,
    }



    tmx_grid = convert_grid_to_tiled_map.build_tiled_map(grd, tileset_index)
    convert_grid_to_tiled_map.save_tmx_file(tmx_grid, op_file, tileset_file_def)





def path_find(grid):

    st = [START_X,START_Y]
    ex = [EXIT_X,EXIT_Y]
    path = pathfind.path_find(grid_to_int(grid), st, ex)
    if len(path) < 2:
        return 'no path found'
    return display_solved_grid(path)


def grid_to_int(grid):
    search_grid = []
    for row in grid:
        op_row = []
        for col in row:
            if col == TILE_FLOOR:
                cell = 1
            elif col == TILE_DOOR_OPEN_VERT:
                cell = 1
            elif col == TILE_DOOR_CLOSED_VERT:
                cell = 5
            elif col == TILE_DOOR_CLOSED_VERT:
                cell = 9
            elif col == TILE_BLANK:
                cell = 0
            else:
                cell = 99 # 9  # can dig through walls if needed but expensive
            op_row.append(cell)
        search_grid.append(op_row)
    return search_grid





def add_walls(grid_y, grid_x):
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



def add_corridors(grid_y, grid_x, PATH_NUM_HORIZ):
    """
    randomly add corridors hor and vert only, to join big rooms
    """

    passages = create_passage_list(grid_y, grid_x, PATH_NUM_HORIZ)

    for passage in passages:
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



def create_passage_list(grid_y, grid_x, PATH_NUM_HORIZ):
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

        passages.extend(get_path_end_points_HORIZ(cur_y, grid_y, grid_x))
    passages.extend(get_path_end_points_HORIZ(START_Y, grid_y, grid_x))  # starting horiz
    passages.extend(get_path_end_points_HORIZ(EXIT_Y, grid_y, grid_x))  # end horiz

    return passages

def get_path_end_points_HORIZ(cur_y, grid_y, grid_x):
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


def add_layout(layout, grid_y, grid_x, ROOM_SIZE_NORMAL):
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

        if l['name'] == 'exit':
            make_room(y,x, ROOM_SIZE_FINISH, l['name'], grid_y, grid_x)
            EXIT_X = x
            EXIT_Y = y
        elif l['name'] == 'start':
            make_room(y,x, ROOM_SIZE_START, l['name'], grid_y, grid_x)
            START_X = x
            START_Y = y
        else:
            make_room(y,x, ROOM_SIZE_NORMAL, l['name'], grid_y, grid_x)
        grd[y][x] = l['marker']


def rnum(max_val=5):
    """
    return a random integer 1 - max_val
    """
    return random.randint(1, max_val)

def make_room(y,x, radius, nme, grid_y, grid_x):
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

def display_solved_grid(path):
    """
    displays the grid with path overlayed on top
    """
    res = ''
    top_wall = '/' + ''.join('-' for x in grd[0]) + '\\\n'
    bot_wall = '\\' + ''.join('-' for x in grd[0]) + '/\n'

    res += top_wall
    for row_num, row in enumerate(grd):
        r_str = '|'
        for col_num, col in enumerate(row):
            if (col_num, row_num) in path:
                r_str += 'x'
            else:
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
