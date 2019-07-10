# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 9:19
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0125_isPalindrome.py
# @Software: PyCharm

'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''

import re

class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        if not s:
            return True
        left, right = 0, len(s)-1
        s = s.lower()
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def isPalindrome_1(self, s: 'str') -> 'bool':
        if not s:
            return True
        s = s.lower()
        s = re.sub(r'\W+', '', s)
        return s == s[::-1]

if __name__  == "__main__":
    a = Solution()
    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))
    print(a.isPalindrome_1(s))
    s = "race a car"
    print(a.isPalindrome(s))
    print(a.isPalindrome_1(s))
    s = "0P"
    print(a.isPalindrome(s))
    print(a.isPalindrome_1(s))