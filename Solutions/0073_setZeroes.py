# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 16:02
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0073_setZeroes.py
# @Software: PyCharm

'''
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row, col = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        return

    def setZeroes_1(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        if not matrix or not matrix[0]:
            return
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n
        return

    def setZeroes_2(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        if not matrix or not matrix[0]:
            return
        rowset = set()
        colset = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowset.add(i)
                    colset.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowset or j in colset:
                    matrix[i][j] = 0
        return

if __name__ == "__main__":
    a = Solution()
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    a.setZeroes_1(matrix)
    print(matrix)
    matrix = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]
    a.setZeroes_1(matrix)
    print(matrix)