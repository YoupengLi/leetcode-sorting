# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 14:38
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0120_minimumTotal.py
# @Software: PyCharm

'''
120. Triangle

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
'''

class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        # O(n*n/2) space, top-down
        if not triangle:
            return
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])

    def minimumTotal_1(self, triangle: 'List[List[int]]') -> 'int':
        # Modify the original triangle, top-down
        if not triangle:
            return
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    def minimumTotal_2(self, triangle: 'List[List[int]]') -> 'int':
        # Modify the original triangle, bottom-up
        if not triangle:
            return
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    def minimumTotal_3(self, triangle: 'List[List[int]]') -> 'int':
        # bottom-up, O(n) space
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]

    def minimumTotal_4(self, triangle: 'List[List[int]]') -> 'int':
        m = len(triangle)
        for i in range(1, m):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
        for i in range(2, m):
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

if __name__  == "__main__":
    a = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(a.minimumTotal(triangle))
    print(a.minimumTotal_1(triangle))
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(a.minimumTotal_2(triangle))
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(a.minimumTotal_3(triangle))
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(a.minimumTotal_4(triangle))