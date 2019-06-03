# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 17:03
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0085_maximalRectangle.py
# @Software: PyCharm

'''
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n+1)
        res  = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res

if __name__ == "__main__":
    a = Solution()
    nums = [["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]]
    res = a.maximalRectangle(nums)
    print(res)
