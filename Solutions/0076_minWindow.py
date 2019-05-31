# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 9:59
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0076_minWindow.py
# @Software: PyCharm

'''
76. Minimum Window Substring

Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

import collections
from collections import defaultdict
import sys
class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        Tc = collections.Counter(t)
        Sc = collections.Counter()

        best_i = -sys.maxsize
        best_j = sys.maxsize

        i = 0
        for j, char in enumerate(s):
            Sc[char] += 1
            while Sc & Tc == Tc:
                if j - i < best_j - best_i:
                    best_i, best_j = i, j

                Sc[S[i]] -= 1
                i += 1
        return s[best_i: best_j + 1] if best_j - best_i < len(s) else ""

    def minWindow_1(self, s: 'str', t: 'str') -> 'str':
        mem = defaultdict(int)
        for c in t:
            mem[c] += 1
        t_len = len(t)

        minL, minR = 0, float('inf')
        l = 0

        for i, c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1
            mem[c] -= 1

            if t_len == 0:
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1

                if i - l < minR - minL:
                    minR, minL = i, l

                mem[s[l]] += 1
                t_len += 1
                l += 1

        return '' if minR == float('inf') else s[minL:minR + 1]

if __name__ == "__main__":
    a = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    res = a.minWindow(S, T)
    print(res)
    res = a.minWindow_1(S, T)
    print(res)