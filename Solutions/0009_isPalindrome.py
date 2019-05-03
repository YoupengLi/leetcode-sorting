# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 0007 12:10
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0009_isPalindrome.py
# @Software: PyCharm

'''
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[len(x)-i-1]:
                return False
        return True

    def isPalindrome_1(self, x: 'int') -> 'bool':
        s = str(x)
        if s[::-1] == s:
            return True
        else:
            return False

    def isPalindrome_2(self, x: 'int') -> 'bool':
        s = str(x)
        if s[0] == '-':
            return False
        else:
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True

    def isPalindrome_3(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        else:
            s = str(x)
            return (s[::-1] == s)

if __name__ == "__main__":
    a = Solution()
    x1 = 121
    x2 = -121
    x3 = 10
    print(a.isPalindrome(x1))
    print(a.isPalindrome_1(x1))
    print(a.isPalindrome_2(x1))
    print(a.isPalindrome_3(x1))
    print(a.isPalindrome(x2))
    print(a.isPalindrome_1(x2))
    print(a.isPalindrome_2(x2))
    print(a.isPalindrome_3(x2))
    print(a.isPalindrome(x3))
    print(a.isPalindrome_1(x3))
    print(a.isPalindrome_2(x3))
    print(a.isPalindrome_3(x3))
