# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 20:57
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0168_convertToTitle.py
# @Software: PyCharm

'''
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
'''

class Solution:
    def convertToTitle(self, n: 'int') -> 'str':
        r = ''
        while n > 0:
            n -= 1
            r = chr(n % 26 + 65) + r
            n //= 26
        return r

    def convertToTitle_1(self, n: 'int') -> 'str':
        id2name = dict(enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1))
        colname = []
        while n > 0:
            i = n % 26
            if i == 0: i = 26
            colname.append(id2name[i])
            n = (n - i) / 26
        return "".join(colname[::-1])

    def convertToTitle_2(self, n: 'int') -> 'str':
        dic = dict(enumerate("ZABCDEFGHIJKLMNOPQRSTUVWXY", 0))
        res = []

        def calc(num, res=''):
            if num == 0:
                return res
            d, r = divmod(num, 26)
            res = dic[r] + res
            if r == 0:
                d -= 1
            return calc(d, res)

        return calc(n)

if __name__  == "__main__":
    a = Solution()
    n = 701
    print(a.convertToTitle(n))
    print(a.convertToTitle_1(n))
    print(a.convertToTitle_2(n))