# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 09:10
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0043_multiply.py
# @Software: PyCharm

'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        return str(int(num1) * int(num2))

if __name__ == "__main__":
    a = Solution()
    num1 = "123"
    num2 = "456"
    res = a.multiply(num1, num2)
    print(res)