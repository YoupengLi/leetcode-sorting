# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 0007 12:41
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0010_isMatch.py
# @Software: PyCharm

'''
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            # self.isMatch(s, p[2:])对应于*代表0个的情况
            # self.isMatch(s[1:], p)对应于*代表多个的情况
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch_1(self, s: 'str', p: 'str') -> 'bool':
        st = [False] * (len(s) + 1)
        st[0] = True
        i = 0
        while i < len(p):
            # 对应有*的情况，在True值后面紧接的所有与True值相同的用*匹配
            if i < len(p) - 1 and p[i + 1] == '*':
                prev = False
                for j in range(0, len(s) + 1):
                    st[j] = st[j] or (prev and (s[j - 1] == p[i] or '.' == p[i]))
                    prev = st[j]
                i += 2
            # 对应没有*的情况，检查单个值，如果相同，则置为True
            else:
                for j in range(len(s), 0, -1):
                    st[j] = st[j - 1] and (s[j - 1] == p[i] or '.' == p[i])
                st[0] = False
                i += 1
        return st[-1]

if __name__ == "__main__":
    a = Solution()
    s = "aa"
    p = "a"
    print(a.isMatch(s, p))
    print(a.isMatch_1(s, p))
    s = "aa"
    p = "a*"
    print(a.isMatch(s, p))
    print(a.isMatch_1(s, p))
    s = "ab"
    p = ".*"
    print(a.isMatch(s, p))
    print(a.isMatch_1(s, p))
    s = "aab"
    p = "c*a*b"
    print(a.isMatch(s, p))
    print(a.isMatch_1(s, p))
    s = "mississippi"
    p = "mis*is*p*."
    print(a.isMatch(s, p))
    print(a.isMatch_1(s, p))


