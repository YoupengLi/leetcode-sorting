# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 0006 20:16
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0006_convert.py
# @Software: PyCharm

'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if not s or len(s) <= numRows:
            return s
        res = []
        for i in range(numRows):
            res.append("")
        index = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        for i in range(len(s)):
            res[index[i % len(index)]] = res[index[i % len(index)]] + s[i]

        return ''.join(res)

    def convert_1(self, s: 'str', numRows: 'int') -> 'str':
        if numRows == 1:
            return s
        row = 0
        d = 1  # direction
        res = [""] * numRows
        for c in s:
            res[row] = res[row] + c
            if row == 0:
                d = 1
            elif row == numRows - 1:
                d = -1
            row = row + d
        return ''.join(res)

if __name__ == "__main__":
    a = Solution()
    s1 = "PAYPALISHIRING"
    s2 = "PAYPALISHIRING"
    print(a.convert(s1, 3))
    print(a.convert_1(s1, 3))
    print(a.convert(s2, 4))
    print(a.convert_1(s2, 4))