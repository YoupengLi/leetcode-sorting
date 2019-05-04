# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 22:26
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0052_totalNQueens.py
# @Software: PyCharm
'''
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    def totalNQueens(self, n: 'int') -> 'int':
        res = []
        self.dfs([-1] * n, 0, [], res)
        return len(res)

        # nums is a one-dimension array, like [1, 3, 0, 2] means
        # first queen is placed in column 1, second queen is placed
        # in column 3, etc.

    def dfs(self, nums: 'list[int]', index: 'int', path: 'list[str]', res: 'list[list[str]]'):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "." * len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)

    def valid(self, nums: 'list[int]', n: 'int') -> 'bool':
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

    def totalNQueens_1(self, n: 'int') -> 'int':
        self.count = 0

        def dfs_1(s, check1, check2):
            if len(s) == n:
                self.count += 1
                return
            for i in range(n):
                c = len(s)
                if (i not in s) and (c - i not in check1) and (c + i not in check2):
                    dfs_1(s + [i], check1 + [c - i], check2 + [c + i])
        if not n:
            return 0
        dfs_1([], [], [])

        return self.count

if __name__ == "__main__":
    a = Solution()
    n = 4
    res = a.totalNQueens(n)
    print(res)
    res = a.totalNQueens_1(n)
    print(res)