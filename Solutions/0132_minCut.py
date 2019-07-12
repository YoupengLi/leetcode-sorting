# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 11:11
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0132_minCut.py
# @Software: PyCharm

'''
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.


Explanation:
The main algorithm idea is if s[i,j] is a palindrome, then the minCut(s[:j]) is at most minCut(s[:i-1])+1.
This literally needs to find out all possible palindromes in the list.
The above post provides an efficient search algorithm.
'''

class Solution:
    def minCut(self, s: 'str') -> 'int':
        # O(n) space and O(n^2) time complexity
        # acceleration
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # algorithm
        cut = [x for x in range(-1, len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1
            # even palindrome
            while i - r2 >= 0 and i + r2 + 1 < len(s) and s[i - r2] == s[i + r2 + 1]:
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]

    def minCut_1(self, s: 'str') -> 'int':
        # O(n) space and O(n^3) time complexity
        # acceleration
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # algorithm
        cut = [x for x in range(-1, len(s))]
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i: j + 1][::-1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
        return cut[-1]

if __name__  == "__main__":
    a = Solution()
    s = "aab"
    print(a.minCut(s))
    print(a.minCut_1(s))
    s = "aabcdca"
    print(a.minCut(s))
    print(a.minCut_1(s))