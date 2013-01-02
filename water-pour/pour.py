# -*- coding:utf-8 -*-
#! /usr/bin/env python
'''
File: pour.py
Author: gaodayue
Description: solve the water pouring puzzle

Given three containers whose size are 10 pints, 7 pints and 4 pints.
The 7-pint and 4-pint containers are full and 10-pint container is empty.
You can pour waters from one container into another, stopping only when the
source container is empty or the destination container is full.

Is there a sequence of pourings that leaves exactly 2 pints in the 7-
or 4-pint container?
'''
from collections import deque
from itertools import permutations

def pour(init, cap, stopfn):
    """
    Find a sequence of pouring start from ``init`` status 
    until stopfn(status) is True.

    Parameters
    ----------
    init : tuple of initial status
    cap : capacities of each bottle
    stopfn : stop pour if stopfn(status) is True
    
    Return
    ------
    A sequence of pouring operation [status1, status2,  ...] if found.
    Empty sequence [] if not found.
    """
    statuses = {}
    statuses[init] = None
    queue = deque([init])
    while queue:
        status = queue.popleft()
        for newstat in transform(status, cap):
            if newstat not in statuses:
                statuses[newstat] = status
                queue.append(newstat)
                if stopfn(newstat):
                    return getseq(newstat, statuses)
    return []


def transform(status, cap):
    tfs = set()
    for b1, b2 in permutations(range(len(status)), 2):
        if status[b2] < status[b1]+status[b2] <= cap[b2]:
            # pour all water in b1 to b2
            newstat = list(status)
            newstat[b1] = 0
            newstat[b2] = status[b1]+status[b2]
            tfs.add(tuple(newstat))
        if status[b2] < cap[b2] < status[b1]+status[b2]:
            # pour water from b1 to b2 until b2 is full
            newstat = list(status)
            newstat[b1] = status[b1]+status[b2]-cap[b2]
            newstat[b2] = cap[b2]
            tfs.add(tuple(newstat))
    return tfs


def getseq(s, statuses):
    seq = []
    while True:
        if s is None:
            break
        seq.append(s)
        s = statuses[s]
    return list(reversed(seq))


if __name__ == '__main__':
    seq = pour((0,7,4), (10,7,4), lambda s: s[1]==2 or s[2]==2)
    print seq
