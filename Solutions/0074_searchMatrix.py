# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 8:29
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0074_searchMatrix.py
# @Software: PyCharm

'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        row = 0
        col = n-1
        while row < m and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False

    def searchMatrix_1(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        col = [row[0] for row in matrix]
        row_idx = self.binarySearch(col, target)
        col_idx = self.binarySearch(matrix[row_idx], target)
        if (matrix[row_idx][col_idx] == target):
            return True
        return False

    def binarySearch(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while (start + 1) < end:
            mid = int(start + (end - start) / 2)
            if (nums[mid] > target):
                end = mid
            else:
                start = mid
        if (nums[end] <= target):
            return end
        return start

if __name__ == "__main__":
    a = Solution()
    matrix = [[1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    res = a.searchMatrix(matrix, 3)
    print(res)
    matrix = [[1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    res = a.searchMatrix_1(matrix, 13)
    print(res)