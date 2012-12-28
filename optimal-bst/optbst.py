"""
Given a sorted array keys[0..n-1] of search keys and an array
freq[0..n-1] of frequency counts, where freq[i] is the number
of searches to keys[i].

Construct a binary search tree of all keys such that the total
cost of all the searches is as small as possible.

Such a BST is called optimal binary search tree
"""

def opt_cost(keys, freq, get_bst=False):
    '''
    Return the cost of optimal binary search tree containing given keys,
    optionally return the optimal BST if ``get_bst`` is True.

    Parameters
    ----------
    keys : list of sorted search keys
    freq : list of frequency counts of search keys
    get_bst : whether to return optimal BST or not

    Returns
    -------
    cost of optimal BST or (cost, BST) if get_bst is True.
    BST is a dictionary of mapping:
        parent => (left_child, right_child) or None
    tree node is the index in ``keys``.

    Examples
    --------
    >>> opt_cost([0, 1], [30, 40])
    100 # 40 + 30 * 2

    >>> opt_cost(['a', 'b', 'c'], [30, 10, 40])
    (130, {0:(None,1), 1:None, 2:(0,None)})

    ``freq`` can also be probabilities.
    If probabilities sum to 1, then cost is the average search length.
    >>> opt_cost([0, 1], [0.6, 0.4])
    1.4
    '''
    n = len(keys)
    table = [[None] * n for _ in xrange(n)]
    for i in xrange(n):
        table[i][i] = (freq[i], i)
    # let optimal BST for subproblem keys[i..j] be T
    # if table[i][j] = (cost, keyidx)
    # then cost is the cost of T, keyidx is index of the root key of T
    for s in xrange(1, n):
        for i in xrange(n-s):
            # compute cost for keys[i..i+s]
            minimal, root = float('inf'), -1
            # search root with minimal cost
            freq_sum = sum(freq[x] for x in xrange(i, i+s+1))
            for r in xrange(i, i+s+1):
                left = 0 if r == i else table[i][r-1][0]
                right = 0 if r == i+s else table[r+1][i+s][0]
                cost = left + right + freq_sum
                if cost < minimal:
                    minimal = cost
                    root = r
            table[i][i+s] = (minimal, root)
    #TODO get_tree impl
    return table[0][n-1][0]


if __name__ == '__main__':
    assert opt_cost([0, 1], [30, 40]) == 100
    assert opt_cost(['a', 'b', 'c'], [30, 10, 40]) == 130
    assert opt_cost([0, 1], [0.6, 0.4]) == 1.4
    assert opt_cost(range(1, 8), [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]) == 2.18
