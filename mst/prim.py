# -*- coding: utf-8 -*-
#! /usr/bin/env python

import sys
import heapq
from IndexMinHeap import IndexMinHeap
"""
read connected undirected graph from an input file,
run Prim's MST algorithm and output the total edge costs

input file format:
    [number_of_nodes] [number_of_edges]
    [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
    [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
    ...
"""

def prim_naive(lines):
    tree = [] # edges added to tree
    N, M = lines[0] # number of nodes and edged

    x = [False] * (N+1) # x[i] means whether node i is spaned
    edges = lines[1:]

    x[1] = True # start from node 1
    # N-1 loop, each loop traverse M edges, so takes O(NM) time
    for _ in xrange(N-1):
        next_edge = (None, None, float('inf'))
        for edge in edges:
            if x[edge[0]] != x[edge[1]] and edge[2] < next_edge[2]:
                next_edge = edge
        x[next_edge[0]] = x[next_edge[1]] = True
        tree.append(next_edge)
    return tree


def prim_use_heap(lines):
    tree = []
    N, M = lines[0]
    x = [False] * (N+1) # x keeps nodes spaned
    adj = [[] for _ in xrange(N+1)] # adjacent list start from index 1
    for edge in lines[1:]:
        adj[edge[0]].append(edge)
        adj[edge[1]].append(edge)
    
    heap = [] # contains (cost, edge), cost as key
    # start from node 1
    x[1] = True
    for e in adj[1]:
        heapq.heappush(heap, (e[2], e))

    for _ in xrange(N-1):
        # get the lightest cross edge
        while True:
            newedge = heapq.heappop(heap)[1]
            if x[newedge[0]] != x[newedge[1]]:
                break
        tree.append(newedge)
        newnode = newedge[1] if x[newedge[0]] else newedge[0]
        x[newnode] = True
        for e in adj[newnode]:
            if x[e[0]] != x[e[1]]:
                heapq.heappush(heap, (e[2], e))
    return tree
    

def prim_use_heap_advance(lines):
    """
    Input:  a connected undirected graph G = (V,E) with edge weights
    Output: a minimal spanning tree defined by the array prev

    for all u in V:
        cost(u) = infinite
        prev(u) = null
    pick any initial node v0
    cost(v0) = 0

    H = makequeue(V) # priority queue, using cost as keys
    while H is not empty:
        v = deletemin(H)
        for each (v, z) in E:
            if cost(z) > weight(v,z):
                cost(z) = weight(v,z)
                prev(z) = v
                decreasekey(H,z)
    """
    N, M = lines[0]
    adj = [[] for _ in xrange(N)]
    # convert 1-based vertex to 0-based
    for (v,z,weight) in lines[1:]:
        adj[v-1].append((z-1,weight))
        adj[z-1].append((v-1,weight))

    # since each time we spaned one new node and one new edge
    # edges[i] = edges spaned along with node i (0-based)
    edges = [None] * N
    heap = IndexMinHeap(N)
    for i in xrange(N):
        heap.insert(i, float('inf'))
    heap.change_key(0, 0)
    while not heap.is_empty():
        v = heap.del_min()
        for z, weight in adj[v]:
            if heap.contains(z) and weight < heap.keyof(z):
                edges[z] = (v+1, z+1, weight)
                heap.change_key(z, weight)
    return edges[1:]

if __name__ == '__main__':
    args = sys.argv
    mst = {
        "prim-naive": prim_naive,
        "prim-heap": prim_use_heap,
        "prim-heap-adv": prim_use_heap_advance
    }
    if len(args) < 2 or args[1] not in mst:
        print "Usage: python %s %s" % (args[0], '|'.join(mst.keys()))
        sys.exit()

    lines = [map(int, line.split()) for line in open('edges.txt').read().splitlines()]
    tree = mst.get(args[1])(lines)
    print 'total edge costs: %s' % sum(e[2] for e in tree)
