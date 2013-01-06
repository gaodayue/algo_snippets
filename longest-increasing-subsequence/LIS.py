# -*- coding: utf-8 -*-
#!/usr/bin/env python

def LIS_slow(seq):
    """
    Compute a Longest-Increasing-Subsequence of ``seq`` in
    quadratic time.

    Note: LIS may not be unique
    """
    if not seq: return []
    # table[i] = (prev, lis)
    # lis : length of LIS ended in s[i]
    # prev: index of number previous to s[i] in LIS
    table = [(-1, 1) for _ in xrange(len(seq))]
    lis = 1
    last = 0
    for i in xrange(1, len(seq)):
        for j in xrange(0, i):
            if seq[j] < seq[i] and table[j][1]+1 > table[i][1]:
                table[i] = (j, table[j][1]+1)
        if table[i][1] > lis:
            lis = table[i][1]
            last = i
    result = []
    while last != -1:
        result.append(seq[last])
        last = table[last][0]
    return list(reversed(result))


def LIS_fast(seq):
    """
    Compute a Longest-Increasing-Subsequence of ``seq`` in
    O(n*lg(n))
    """
    pass


if __name__ == '__main__':
    assert LIS_slow([1, 2, 3]) == [1, 2, 3]
    assert LIS_slow([3, 1, 2]) == [1, 2]
    assert LIS_slow([10, 22, 9, 33, 21, 50, 41, 60]) == [10, 22, 33, 50, 60] 
