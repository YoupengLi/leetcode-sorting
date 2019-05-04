# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 0007 16:52
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0054_spiralOrder.py
# @Software: PyCharm

'''
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
            return []
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        while cols > start*2 and rows > start*2:
            self.printMatrix(matrix, rows, cols, start, res)
            start += 1
        return res

    def printMatrix(self, matrix, rows, cols, start, res):
        endX = cols-1-start
        endY = rows-1-start

        # 从左到右打印一行
        for i in range(start, endX+1):
            res.append(matrix[start][i])

        # 从上到下打印一列
        if start < endY:
            for i in range(start+1, endY+1):
                res.append(matrix[i][endX])

        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                res.append(matrix[endY][i])

        # 从下到上打印一列
        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                res.append(matrix[i][start])

    # matrix类型为二维列表，需要返回列表
    def spiralOrder_1(self, matrix: 'List[List[int]]') -> 'List[int]':
        # matrix and [*matrix.pop(0)]是为了防止matrix为空时进行pop出错，and短路机制：matrix为[]时不再执行and后的语句。
        # *matrix将矩阵压缩成每列对应的形式，[::-1]将其反转，最后*zip解压缩成原始形式
        # *matrix将矩阵压缩成每列对应的形式，然后取出第一个元素
        # 整个过程可以看作是不停地取第一行，取完之后逆时针翻转矩阵，继续取第一行，直到矩阵为空
        return matrix and [*matrix.pop(0)] + self.spiralOrder_1([*zip(*matrix)][::-1])

if __name__ == "__main__":
    a = Solution()
    nums = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
    res = a.spiralOrder(nums)
    print(res)
    res = a.spiralOrder_1(nums)
    print(res)
    nums = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    res = a.spiralOrder(nums)
    print(res)
    res = a.spiralOrder_1(nums)
    print(res)