# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 22:50
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0064_minPathSum.py
# @Software: PyCharm

'''
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        if not grid or len(grid) <= 0 or not grid[0] or len(grid[0]) <= 0:
            return None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    def minPathSum_1(self, grid: 'List[List[int]]') -> 'int':
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = (min(dp[j], dp[j - 1]) or dp[j - 1]) + grid[i][j]
        return dp[-1]

if __name__ == "__main__":
    a = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = a.minPathSum(grid)
    print(res)
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = a.minPathSum_1(grid)
    print(res)