# -*- coding:utf-8 -*-
#! /usr/bin/env python

'''
File: longest_unique_substr.py
Author: gaodayue
Description:

Given a string, find the length of the longest substring without repeating characters.

Example:
    longest_unique_substr('BBB') == 'B'
    longest_unique_substr('ABDEFGABEF') in ('ABDEFG', 'BDEFGA', 'DEFGAB')
'''

def longest_unique_substr(s):
    cur_start, cur_len = (0, 0)
    max_start, max_len = (0, 0)
    # use hashmap to fast check character repeatness 
    char_pos = {} # char_pos['a'] is the last index we see 'a'
    for i in xrange(len(s)):
        last_idx = char_pos.get(s[i], -1)
        if last_idx < cur_start:
            # encounter a new character or a character not in current substring
            cur_len += 1
        else:
            # encounter a repeated character
            if cur_len > max_len:
                (max_start, max_len) = (cur_start, cur_len)
            cur_start = last_idx + 1
            cur_len = i - cur_start + 1
        char_pos[s[i]] = i
    if cur_len > max_len:
        (max_start, max_len) = (cur_start, cur_len)
    return s[max_start : max_start+max_len]


if __name__ == '__main__':
    assert longest_unique_substr('') == ''
    assert longest_unique_substr('ABCA') in ('ABC', 'BCA')
    assert longest_unique_substr('BBB') == 'B'
    assert longest_unique_substr('ABDEFGABEF') in ('ABDEFG', 'BDEFGA', 'DEFGAB')
