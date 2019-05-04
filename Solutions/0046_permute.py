# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 12:41
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0046_permute.py
# @Software: PyCharm

'''
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums: 'List[int]', path: 'List[int]', res: 'List[list[int]]'):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3]
    res = a.permute(nums)
    print(res)