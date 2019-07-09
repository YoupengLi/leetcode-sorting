# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 10:21
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0118_generate.py
# @Software: PyCharm

'''
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

from math import factorial as f

class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

    def generate_1(self, numRows: 'int') -> 'List[List[int]]':
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        res = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[i - 1][j - 1] + res[i - 1][j])
            tmp.append(1)
            res.append(tmp)
        return res

    def generate_2(self, numRows: 'int') -> 'List[List[int]]':
        C = lambda n, r: f(n) // f(r) // f(n - r)
        return [[C(n, r) for r in range(n + 1)] for n in range(numRows)]

if __name__  == "__main__":
    a = Solution()
    numRows = 1
    print(a.generate(numRows))
    print(a.generate_1(numRows))
    print(a.generate_2(numRows))