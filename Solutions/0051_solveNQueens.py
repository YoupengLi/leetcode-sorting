# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 20:48
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0051_solveNQueens.py
# @Software: PyCharm

'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

class Solution:
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

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
        # check whether nth queen can be placed in that column

    def valid(self, nums: 'list[int]', n: 'int') -> 'bool':
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

if __name__ == "__main__":
    a = Solution()
    n = 8
    res = a.solveNQueens(n)
    print(res)