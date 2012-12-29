# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
"""
Max-spacing k-clustering algorithm
goal: compute the maxmum spacing of a k-clustering
"""

class DisjointSet(object):
    def __init__(self, n):
        self.parents = range(n)
        self.rank = [1] * n

    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return
        if self.rank[pi] < self.rank[pj]:
            self.parents[pi] = pj
        elif self.rank[pi] > self.rank[pj]:
            self.parents[pj] = pi
        else:
            self.parents[pi] = pj
            self.rank[pj] += 1
        
"""
input file format:
    [number_of_nodes]
    [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
    [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
"""
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print "Usage: python cluster.py k"
        sys.exit()
    try:
        k = int(args[1])
    except:
        k = -1

    lines = [map(int, line.split()) for line in open(
        'huge.txt').read().splitlines()]
    N = lines[0][0]
    if k < 2 or k > N:
        print "k should in [2,%s]" % N
        sys.exit()

    # convert vertices to 0-based
    edges = [(u-1, v-1, w) for (u,v,w) in lines[1:]]
    # max-spacing k-clustering algorithm
    edges.sort(key=lambda ln:ln[2])
    cluster_num = N 
    clusters = DisjointSet(N)
    while cluster_num != k:
        while True:
            u, v, weight = edges.pop(0)
            if clusters.find(u) != clusters.find(v):
                clusters.union(u, v)
                cluster_num -= 1
                break
    # find the maxmum spacing
    while True:
        u, v, weight = edges.pop(0)
        if clusters.find(u) != clusters.find(v):
            print 'maxmum spacing is %s' % weight
            break
