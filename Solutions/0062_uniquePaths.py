# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0016 08:40
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0062_uniquePaths.py
# @Software: PyCharm

'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?
Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        if n == 0 and m == 0:
            return 0
        if n == 1 and m == 1:
            return 1
        res = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[n-1][m-1]

if __name__ == "__main__":
    a = Solution()
    m = 7
    n = 3
    res = a.uniquePaths(m, n)
    print(res)