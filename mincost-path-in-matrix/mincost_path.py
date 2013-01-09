# -*- coding:utf-8 -*-
#! /usr/bin/env python

'''
File: mincost_path.py
Author: gaodayue
Description:

Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).

Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination).

You can only traverse down, right and diagonally lower cells from a given cell
'''

def mincost(costs, m, n):
    '''
    Compute minimal cost path using Dynamic Programming Paradigm in O(m*n) time
    '''
    table = [[0]*(n+1) for _ in xrange(m+1)]
    cell_cost = lambda i, j: table[i][j] if i >=0 and j >= 0 else float('inf')
    for i in xrange(m+1):
        for j in xrange(n+1):
            table[i][j] = costs[i][j]
            if (i, j) != (0, 0):
                table[i][j] += min(cell_cost(i-1, j),
                                   cell_cost(i, j-1),
                                   cell_cost(i-1, j-1))
    return table[m][n]


if __name__ == '__main__':
    costs = [[1, -2], [3, 4]]
    assert mincost(costs, 1, 1) == 3
    costs = [[1, 2, 3],
             [4, 8, 2],
             [1, 5, 3]]
    assert mincost(costs, 2, 2) == 8
