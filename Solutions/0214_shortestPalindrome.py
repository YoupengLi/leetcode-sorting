# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 9:19
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0214_shortestPalindrome.py
# @Software: PyCharm

'''
214. Shortest Palindrome

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: "abcd"
Output: "dcbabcd"
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

    def shortestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        return s[::-1][:len(s) - j] + self.shortestPalindrome_1(s[:j - len(s)]) + s[j - len(s):]

if __name__ == "__main__":
    a = Solution()
    s = "aacecaaa"
    print(a.shortestPalindrome(s))
    print(a.shortestPalindrome_1(s))
    s = "abcd"
    print(a.shortestPalindrome(s))
    print(a.shortestPalindrome_1(s))
    s = "dedc"
    print(a.shortestPalindrome(s))
    print(a.shortestPalindrome_1(s))