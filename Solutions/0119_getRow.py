# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 11:45
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0119_getRow.py
# @Software: PyCharm

'''
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
'''

from math import factorial as f

class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        triangle = []

        for row_num in range(rowIndex + 1):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle[-1]

    def getRow_1(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        res = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[i - 1][j - 1] + res[i - 1][j])
            tmp.append(1)
            res.append(tmp)

        return res[-1]

    def getRow_2(self, rowIndex: 'int') -> 'List[int]':
        C = lambda n, r: f(n) // f(r) // f(n - r)
        return [C(rowIndex, r) for r in range(rowIndex + 1)]

    def getRow_3(self, rowIndex: 'int') -> 'List[int]':
        res = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res[rowIndex]

if __name__  == "__main__":
    a = Solution()
    numRows = 3
    print(a.getRow(numRows))
    print(a.getRow_1(numRows))
    print(a.getRow_2(numRows))
    print(a.getRow_3(numRows))