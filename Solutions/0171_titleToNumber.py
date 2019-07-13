# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 11:20
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0171_titleToNumber.py
# @Software: PyCharm

'''
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
'''

class Solution:
    def titleToNumber(self, s: 'str') -> 'int':
        dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))
        res = 0
        for i in s:
            res = 26 * res + dic[i]
        return res

    def titleToNumber_1(self, s: 'str') -> 'int':
        res = 0
        for c in s:
            res = res * 26 + (ord(c) - ord('A') + 1)
        return res

if __name__  == "__main__":
    a = Solution()
    s = 'A'
    print(a.titleToNumber(s))
    s = 'AB'
    print(a.titleToNumber(s))
    s = 'ZY'
    print(a.titleToNumber(s))