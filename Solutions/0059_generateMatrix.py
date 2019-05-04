# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 0015 08:39
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0059_generateMatrix.py
# @Software: PyCharm

'''
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    def generateMatrix(self, n: 'int') -> 'List[List[int]]':
        row = col = count = 0
        size = n - 1
        A = [[None for _ in range(n)] for _ in range(n)]
        for i in range(1, n**2+1):
            if A[row][col]:
                row += 1
                col += 1
                count += 1
                size -= 1
            A[row][col] = i
            if row == count and col < size:
                col += 1
            elif row < size and col == size:
                row += 1
            elif row == size and col > count:
                col -= 1
            elif row > count and col == count:
                row -= 1
        return A

if __name__ == "__main__":
    a = Solution()
    n = 3
    res = a.generateMatrix(n)
    print(res)