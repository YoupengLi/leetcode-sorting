# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 17:05
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0263_isUgly.py
# @Software: PyCharm

'''
263. Ugly Number

Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
Input: 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:
Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:
1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
'''

class Solution:
    def isUgly(self, num: 'int') -> 'bool':
        if num == 0:
            return False
        prime = [2, 3, 5]
        for i in prime[::-1]:
            while num % i == 0:
                num = num // i
        return True if num == 1 else False

    def isUgly_1(self, num: 'int') -> 'bool':
        if num < 1:
            return False
        numSet = set([1, 2, 3, 5])
        if num in numSet:
            return True
        while num not in numSet:
            find = False
            for n in [5, 3, 2]:
                if num % n == 0:
                    num = num // n
                    find = True
                    break
            if not find:
                return False
        return True

if __name__ == "__main__":
    a = Solution()
    num = 6
    print(a.isUgly(num))
    print(a.isUgly_1(num))
    num = 8
    print(a.isUgly(num))
    print(a.isUgly_1(num))
    num = 14
    print(a.isUgly(num))
    print(a.isUgly_1(num))