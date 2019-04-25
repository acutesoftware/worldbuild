#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pathfind.py



from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]



def path_find(matrix, start_cell, end_cell):
    """
    example from https://pypi.org/project/pathfinding/
    """
    grid = Grid(matrix=matrix)


    #print('pathfind.py start, end, grid = ', start_cell, end_cell, matrix)
    print('pathfind.py start, end = ', start_cell, end_cell)

    start = grid.node(start_cell[0], start_cell[1])
    end = grid.node(end_cell[0], end_cell[1])

    #finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    #print(grid.grid_str(path=path, start=start, end=end))
    return path

if __name__ == '__main__':
    main()
