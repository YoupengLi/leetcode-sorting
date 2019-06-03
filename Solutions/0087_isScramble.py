# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 19:41
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0087_isScramble.py
# @Software: PyCharm

'''
87. Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

解题思路1：递归
字符串长度为1：很明显，两个字符串必须完全相同才可以。
字符串长度为2：当s1=”ab”, s2只有”ab”或者”ba”才可以。
对于任意长度的字符串，我们可以把字符串s1分为a1,b1两个部分，s2分为a2,b2两个部分，满足（(a1~a2) && (b1~b2)）或者 （(a1~b2) && (a1~b2)）
'''

class Solution:
    def isScramble(self, s1: 'str', s2: 'str') -> 'bool':
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False

    # DP with memorization
    def __init__(self):
        self.dic = {}

    def isScramble_1(self, s1: 'str', s2: 'str') -> 'bool':
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):  # prunning
            self.dic[(s1, s2)] = False
            return False
        if s1 == s2:
            self.dic[(s1, s2)] = True
            return True
        for i in range(1, len(s1)):
            if (self.isScramble_1(s1[:i], s2[:i]) and self.isScramble_1(s1[i:], s2[i:])) or \
                    (self.isScramble_1(s1[:i], s2[-i:]) and self.isScramble_1(s1[i:], s2[:-i])):
                return True
        self.dic[(s1, s2)] = False
        return False

if __name__ == "__main__":
    a = Solution()
    s1 = "great"
    s2 = "rgeat"
    res = a.isScramble(s1, s2)
    print(res)
    s1 = "abcde"
    s2 = "caebd"
    res = a.isScramble_1(s1, s2)
    print(res)