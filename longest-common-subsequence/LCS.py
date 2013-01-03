# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
File: LCS.py
Author: gaodayue
Description: find the longest common subsequence of two given strings

LCS problem: http://en.wikipedia.org/wiki/Longest_common_subsequence_problem
'''


def lcs(s1, s2):
    """
    Find one longest common subsequence of string ``s1`` and ``s2``.
    """
    n, m = len(s1), len(s2)
    table = [[0]*(m+1) for _ in xrange(n+1)]
    for i in xrange(n+1):
        table[i][0] = 0
    for j in xrange(m+1):
        table[0][j] = 0
    for i in xrange(1, n+1):
        for j in xrange(1, m+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])
    # backtrace to reconstruct
    result = []
    while True:
        if i == 0 or j == 0:
            break
        if s1[i-1] == s2[j-1]:
            result.append(s1[i-1])
            i -= 1
            j -=1
        elif table[i][j] == table[i-1][j]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(result))


if __name__ == '__main__':
    assert lcs('', '') == ''
    assert lcs('', 'a') == ''
    assert lcs('abc', 'bcd') == 'bc'
    assert lcs('bdcaba', 'abcbdab') == 'bdab'
    assert lcs('thisisatest', 'testing123testing') == 'tsitest'
