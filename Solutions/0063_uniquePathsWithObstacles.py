# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 16:42
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0063_uniquePathsWithObstacles.py
# @Software: PyCharm

'''
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        if obstacleGrid[0][0]:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                elif i == 0 and j == 0:
                    res[i][j] = 1
                else:
                    if j - 1 >= 0:
                        res[i][j] += res[i][j-1]
                    if i - 1 >= 0:
                        res[i][j] += res[i-1][j]
        return res[-1][-1]

if __name__ == "__main__":
    a = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    res = a.uniquePathsWithObstacles(obstacleGrid)
    print(res)
    obstacleGrid = [[1, 0]]
    res = a.uniquePathsWithObstacles(obstacleGrid)
    print(res)
    obstacleGrid = [[0, 0], [0, 1]]
    res = a.uniquePathsWithObstacles(obstacleGrid)
    print(res)