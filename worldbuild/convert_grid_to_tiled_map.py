#!/usr/bin/python3
# -*- coding: utf-8 -*-
# convert_grid_to_tiled_map.py

import os
import math
from random import randint
import vais.worlds as my_world

tile_indexes = { # for mountain_landscapes.png
'.': 164, # grass
'X': 10, # stone hills
'#': 76, # blocking rocks
}

def main():
    print('takes a grid built via the build_random_grid and converts to TMX file')
    grid = []
    cur_line = []
    with open('test_world.txt', 'r') as f:
      for line in f:
        cur_line = list(line)[:-1]
        #print('cur_line = ', cur_line)
        if cur_line != []:
            grid.append(cur_line)
    tmx_grid = build_tiled_map(grid, tile_indexes)
    save_tmx_file(tmx_grid, 'test_world.tmx', 'mountain_landscape.tsx')

    print('Done')




def build_tiled_map(grid, mapping):
  """
  takes a list of lists as a grid and returns a TMX file
  """
  print('working ...')
  tmx_grid = []
  cur_char = ''
  #print(grid)
  for row in grid:
    cur_line = []

    for col in row:
      cur_line.append(get_tile_index(col, mapping))
    tmx_grid.append(cur_line)

  return tmx_grid



def get_tile_index(letter, mapping):
    """
    lookups up the letter in the tileset definition
    and returns the grid index (single value for TMX)
    """
    if letter in mapping:
        return mapping[letter]
    else:
        return 0 # should return -1 to force tile fixing


def save_tmx_file(tmx_grid, op_file, tileset_file):
    """
    takes a the grid (list of lists as tile index numbers)
    and outputs in TMX file format
    """
    width = str(len(tmx_grid[0]))
    height = str(len(tmx_grid))

    with open(op_file, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<map version="1.2" tiledversion="1.2.3" orientation="orthogonal" renderorder="right-down" width="100" height="100" tilewidth="32" tileheight="32" infinite="0" nextlayerid="2" nextobjectid="1">\n')
        f.write(' <tileset firstgid="1" source="' + tileset_file + '"/>\n')
        f.write(' <layer id="1" name="Tile Layer 1" width="' + width + '" height="' + height + '">\n')
        f.write('  <data encoding="csv">\n')
        grd_txt = ''
        for row in tmx_grid:
            line = ','.join([str(c) for c in row])
            grd_txt += line + ',\n'
        f.write(grd_txt[:-2] + '\n')



        f.write('</data>\n</layer>\n</map>\n')


if __name__ == '__main__':
	main()
