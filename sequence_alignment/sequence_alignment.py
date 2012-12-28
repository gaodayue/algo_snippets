'''
compute best alignment (edit-distance) for two strings
in running time O(m*n) using dynamic programming paradigm
'''
import numpy

def align(s1, s2):
    '''
    Compute best alignment for tow input string.

    Parameters
    ----------
    s1 : first string
    s2 : second string

    Returns
    -------
    (ed, str1, str2)
    ed : edit distance of the best alignment
    str1 : s1 after alignment (use '-' for gap)
    str2 : s2 after alignment

    Examples
    --------
    >>> align('mother', 'father')
    (2, 'mother', 'father')

    >>> align('friend', 'fraid')
    (3, 'friend', 'fr-aid')
    
    >>> align('AACAGTTACC', 'TAAGGTCA')
    (5, 'AACAGTTACC', 'TA-AGGT-CA')
    '''
    m, n = len(s1), len(s2)
    table = numpy.zeros((m+1, n+1), dtype=numpy.int)
    for i in xrange(m+1):
        table[i][0] = i
    for i in xrange(n+1):
        table[0][i] = i
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            match = 0 if s1[i-1] == s2[j-1] else 1
            table[i][j] = min(match+table[i-1][j-1], # align x with y
                              1 + table[i-1][j],     # align x with -
                              1 + table[i][j-1])     # align - with y
    ed = table[i][j]
    # reverse engineering
    str1, str2 = [], []
    while True:
        if i == 0:
            while j > 0:
                str2.append(s2[j-1])
                j -= 1
            break
        if j == 0:
            while i > 0:
                str1.append(s1[i-1])
                i -= 1
            break
        x, y = s1[i-1], s2[j-1]
        match = 0 if x == y else 1
        if table[i][j] == (match + table[i-1][j-1]):
            str1.append(x)
            str2.append(y)
            i -= 1
            j -= 1
        elif table[i][j] == (1 + table[i][j-1]):
            str1.append('-')
            str2.append(y)
            j -= 1
        else:
            str1.append(x)
            str2.append('-')
            i -= 1
    return (ed, ''.join(reversed(str1)), ''.join(reversed(str2)))

if __name__ == '__main__':
    while True:
        print 'please input two string ("exit" to exit):'
        s1 = raw_input()
        if s1 == 'exit':
            break
        s2 = raw_input()
        (ed, str1, str2) = align(s1, s2)
        print '\nbest aligntment:'
        print str1
        print str2
        print 'with edit distance %s\n' % ed
