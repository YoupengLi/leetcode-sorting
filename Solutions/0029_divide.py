# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 0017 20:50
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0029_divide.py
# @Software: PyCharm

'''
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1
when the division result overflows.
'''

class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        if divisor == 0:
            print("Error")
            return -1
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

    def divide_1(self, dividend: 'int', divisor: 'int') -> 'int':
        if divisor == 0:
            print("Error")
            return -1
        if dividend == 0:
            return 0
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            shift = 1
            while dividend >= (divisor << shift):
                shift += 1
            dividend -= (divisor << shift-1)
            res += (1 << shift-1)
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

if __name__ == "__main__":
    a = Solution()
    dividend = 10
    divisor = 3
    res = a.divide(dividend, divisor)
    print(res)
    dividend = 10
    divisor = 3
    res = a.divide_1(dividend, divisor)
    print(res)