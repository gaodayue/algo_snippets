"""
Knapsack problem, only one item for each

file format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...
"""
import numpy
import sys

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __str__(self):
        return 'item(%s, %s)' % (self.value, self.weight)

    def __repr__(self):
        return str(self)


def knapsack_iter(items, capacity):
    '''
    iterative version
    '''
    n, w = len(items), capacity
    table = numpy.zeros((n+1, w+1), dtype=int)
    for i in xrange(1, n+1):
        x = items[i-1]
        for j in xrange(1, w+1):
            exclude_x = table[i-1][j]
            if x.weight > j:
                table[i][j] = exclude_x
            else:
                include_x = x.value + table[i-1][j-x.weight]
                table[i][j] = exclude_x if exclude_x > include_x else include_x
    # rebuild knapsack solution
    pick = []
    while n >= 1:
        x = items[n-1]
        if table[n][w] != table[n-1][w]:
            pick.append(x)
            w -= x.weight
        n -= 1
    return (table[-1][-1], pick)

def knapsack_memo(items, capacity):
    cache = {}
    def recursive_compute(i, w):
        key = (i, w)
        if key in cache:
            return cache[key]
        x = items[i]
        if i == 0:
            cache[key] = x.value if x.weight <= w else 0
            return cache[key]
        exclude_x = recursive_compute(i-1, w)
        if x.weight > w:
            cache[key] = exclude_x
        else:
            include_x = x.value + recursive_compute(i-1, w-x.weight)
            cache[key] = include_x if include_x > exclude_x else exclude_x
        return cache[key]

    max_val = recursive_compute(len(items)-1, capacity)
    # rebuild knapsack solution
    pick = []
    i, w = len(items)-1, capacity
    while True:
        x = items[i]
        if i == 0:
            if cache[(i, w)]:
                pick.append(x)
            break
        if cache[(i, w)] != cache[(i-1, w)]: # include x
            pick.append(x)
            w -= x.weight
        i -= 1
    return (max_val, pick)
    

if __name__ == '__main__':
    filename = sys.argv[1]
    lines = [map(int, line.split()) for line in open(filename, 'r').read().splitlines()]
    capacity = lines[0][0]
    items = [Item(v,w) for v,w in lines[1:]]

    max_val, sln = knapsack_memo(items, capacity)
    print 'maxmum value is %s' % max_val
    print sln

    max_val, sln = knapsack_iter(items, capacity)
    print '\n\nmaxmum value is %s' % max_val
    print sln
