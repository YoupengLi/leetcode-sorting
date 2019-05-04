# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 09:19
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0044_isMatch.py
# @Software: PyCharm

'''
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''
import re
from itertools import islice
class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1]

    def isMatch_1(self, s: 'str', p: 'str') -> 'bool':
        # Solution 1: Greedy
        m = len(s)
        n = len(p)
        i = 0
        j = 0
        iStart = -1
        jStart = -1

        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):  # 字符匹配
                i += 1
                j += 1
            elif j < n and p[j] == '*':  # 万能字符匹配，直到遇到字符匹配
                jStart = j + 1
                iStart = i
                j = jStart
            elif iStart != -1 and jStart != -1:
                iStart += 1
                i = iStart
                j = jStart
            else:
                return False

        while j < n and p[j] == '*':  # i == m and j < n
            j += 1

        return j == n

    def isMatch_2(self, s: 'str', p: 'str') -> 'bool':
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                for n in range(length-1, -1, -1):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

if __name__ == "__main__":
    a = Solution()
    s = "aa"
    p = "a"
    res = a.isMatch(s, p)
    print(res)
    res = a.isMatch_1(s, p)
    print(res)
    res = a.isMatch_2(s, p)
    print(res)
    s = "aa"
    p = "*"
    res = a.isMatch(s, p)
    print(res)
    res = a.isMatch_1(s, p)
    print(res)
    res = a.isMatch_2(s, p)
    print(res)
    s = "cb"
    p = "?a"
    res = a.isMatch(s, p)
    print(res)
    res = a.isMatch_1(s, p)
    print(res)
    res = a.isMatch_2(s, p)
    print(res)
    s = "adceb"
    p = "*a*b"
    res = a.isMatch(s, p)
    print(res)
    res = a.isMatch_1(s, p)
    print(res)
    res = a.isMatch_2(s, p)
    print(res)
    s = "acdcb"
    p = "a*c?b"
    res = a.isMatch(s, p)
    print(res)
    res = a.isMatch_1(s, p)
    print(res)
    res = a.isMatch_2(s, p)
    print(res)