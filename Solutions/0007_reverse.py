# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 0006 22:55
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0007_reverse.py
# @Software: PyCharm

'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0
when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: 'int') -> 'int':
        maxint = 2 ** 31 - 1
        minint = -2 ** 31
        res = int(str(abs(x))[::-1])
        return res * (abs(x)//x) if minint < res < maxint and res else 0

    def reverse_1(self, x: 'int') -> 'int':
        num = 0
        a = abs(x)
        while a:
            temp = a % 10
            num = num * 10 + temp
            a = int(a / 10)
        if x < 0 and num < 2 ** 31:
            return -num
        elif x > 0 and num < 2 ** 31 - 1:
            return num
        else:
            return 0

if __name__ == "__main__":
    a = Solution()
    x1 = -123
    x2 = 120
    print(a.reverse(x1))
    print(a.reverse_1(x1))
    print(a.reverse(x2))
    print(a.reverse_1(x2))