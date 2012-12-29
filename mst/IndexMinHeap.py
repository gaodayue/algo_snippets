# -*- coding: utf-8 -*-
#!/usr/bin/env python

class IndexMinHeap(object):

    def __init__(self, maxnum):
        self.NMAX = maxnum
        self.N = 0
        # heap array, 1-based index
        self.hp = [-1] * (maxnum+1)
        # inverted of heap array:
        # hp[ihp[i]] = i, ihp[hp[n]] = n
        self.ihp = [-1] * maxnum
        self.keys = [None] * maxnum

    def _greater(self, i, j):
        return self.keys[self.hp[i]] > self.keys[self.hp[j]]
    
    def _exch(self, i, j):
        self.ihp[self.hp[i]] = j
        self.ihp[self.hp[j]] = i
        self.hp[i], self.hp[j] = self.hp[j], self.hp[i]

    def _swin(self, k):
        while k > 1 and self._greater(k/2, k):
            self._exch(k, k/2)
            k /= 2

    def _sink(self, k):
        while k*2 <= self.N:
            j = k * 2
            if j < self.N and self._greater(j, j+1):
                j += 1
            if not self._greater(k, j):
                break
            self._exch(k, j)
            k = j

    def insert(self, i, key):
        if self.ihp[i] != -1:
            raise Exception('already use key index %s' % i)
        self.keys[i] = key
        self.N += 1
        self.hp[self.N] = i
        self.ihp[i] = self.N
        self._swin(self.N)

    def min_index(self):
        return self.hp[1]

    def min_key(self):
        if self.N == 0:
            raise Exception('heap is empty, no min key')
        return self.keys[self.hp[1]]

    def del_min(self):
        """
        delete the minimal key, return associated index
        """
        if self.N == 0:
            return -1
        min_index = self.hp[1]
        self._exch(1, self.N)
        self.hp[self.N] = -1
        self.ihp[min_index] = -1
        self.keys[min_index] = None
        self.N -= 1
        self._sink(1)
        return min_index

    def change_key(self, i, key):
        if self.ihp[i] == -1:
            raise Exception('no key index %s' % i)
        if key > self.keys[i]:
            # increase key, sink
            self.keys[i] = key
            self._sink(self.ihp[i])
        elif key < self.keys[i]:
            # decrease key, swin
            self.keys[i] = key
            self._swin(self.ihp[i])

    def size(self):
        return self.N

    def is_empty(self):
        return self.N == 0

    def contains(self, i):
        return self.ihp[i] != -1

    def keyof(self, i):
        return self.keys[i]

if __name__ == '__main__':
    pq = IndexMinHeap(5)
    assert pq.is_empty()
    pq.insert(0, 31)
    assert not pq.is_empty()
    pq.insert(1, 18)
    pq.insert(2, 6)
    pq.insert(3, 26)
    assert pq.size() == 4
    pq.insert(4, 15)
    assert pq.del_min() == 2
    assert pq.del_min() == 4
    pq.insert(2, 22)
    assert pq.min_index() == 1
    pq.change_key(2, 5)
    assert pq.min_index() == 2
    
