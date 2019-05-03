# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 0022 上午 10:45
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0005_longestPalindrome.py
# @Software: PyCharm

'''
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

解题思路：
简单来说就是寻找字符串中最长的回文。
在最开始自己写的时候把回文区分成两种：
第一种是奇数长的回文，这样的回文在寻找时，只要从某个位置开始，同时往两边扩展，边扩展边判断，同时注意边界条件；
第二种是偶数长的回文，这样的回文在寻找时，要从相邻的两个位置想两边扩展，边扩展边判断，同时注意边界条件。
'''

class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if len(s) <= 1:
            return s

        res = ""
        # 寻找奇数长的回文
        for i in range(len(s)):
            j = i
            k = i
            tmp = ""
            while j >= 0 and k <= len(s)-1 and s[j] == s[k]:
                j = j-1
                k = k+1
            if j != k:
                tmp = s[j+1:k]
            else:
                tmp += s[i]
            if len(tmp) >= len(res):
                res = tmp

        # 寻找偶数长的回文
        for i in range(len(s)):
            j = i
            k = i+1
            tmp = ""
            while j >= 0 and k <= len(s)-1 and s[j] == s[k]:
                j = j-1
                k = k+1
            if k-j != 1:
                tmp = s[j+1:k]

            if len(tmp) >= len(res):
                res = tmp

        return res

    def longestPalindrome_1(self, s: 'str') -> 'str':
        if len(s) <= 1:
            return s

        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s, i, i)
            self.expandFromCenter(s, i, i + 1)
        return s[self.start:self.start + self.maxlen]

    def expandFromCenter(self, s: 'str', l: 'int', r: 'int'):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if self.maxlen < r - l - 1:
            self.maxlen = r - l - 1
            self.start = l + 1

if __name__ == "__main__":
    a = Solution()
    s1 = "babad"
    s2 = "cbbd"
    print(a.longestPalindrome(s1))
    print(a.longestPalindrome_1(s2))