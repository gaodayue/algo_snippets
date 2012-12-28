"""
max weighted independancy set
"""
import sys
from random import randint

def wis_recur(weights):
    '''
    input:  weights of each vertex in a path graph
    output: list of vertices in MWIS
    '''
    def recursive_slove(weights, endidx):
        if endidx == 0:
            return [0]
        if endidx == 1:
            return [1] if weights[1] > weights[0] else [0]
        exclude_last = recursive_slove(weights, endidx-1)
        include_last = recursive_slove(weights, endidx-2) + [endidx]
        if sum(weights[i] for i in exclude_last) > sum(weights[i] for i in include_last):
            return exclude_last
        else:
            return include_last
    return recursive_slove(weights, len(weights)-1)

def wis_dp(weights):
    '''
    input:  weights of each vertex in a path graph
    output: list of vertices in MWIS
    '''
    size = len(weights)
    result = []
    a = [0] * (size+1)
    a[1] = weights[0]
    for i in xrange(2, size+1):
        exclude_last = a[i-1]
        include_last = weights[i-1] + a[i-2]
        if exclude_last > include_last:
            a[i] = exclude_last
        else:
            a[i] = include_last
    i = size
    while i > 0:
        if a[i] > a[i-1]: # include
            result.append(i-1)
            i -= 2
        else:
            i -= 1
    return list(reversed(result))


if __name__ == '__main__':
    n_vertices = int(sys.argv[1])
    weights = [randint(1,100) for _ in xrange(n_vertices)]
    print 'path graph:\n%s' % weights

    print '\nDP solution:'
    s2 =wis_dp(weights)
    print s2
    print [weights[i] for i in s2]
    print sum([weights[i] for i in s2])

    print '\nrecursive solution:'
    s1 = wis_recur(weights)
    print s1
    print [weights[i] for i in s1]
    print sum([weights[i] for i in s1])

