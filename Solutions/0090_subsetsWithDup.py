# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 21:30
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0090_subsetsWithDup.py
# @Software: PyCharm

'''
90. Subsets II

Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        self.res = []
        nums.sort()
        self.dfs(nums, 0, [], self.res)
        return self.res

    def dfs(self, nums: 'List[int]', index: 'int', path: 'List[int]', res: 'List[List[int]]'):
        self.res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], self.res)

    def subsetsWithDup_1(self, nums: 'List[int]') -> 'List[List[int]]':
        # backtracking problem
        if not nums:
            return [[]]
        nums = sorted(nums)
        self.res = []  # final result
        self.backtrack(nums, [], 0)  # pass the current state to the function
        return self.res

    def backtrack(self, nums: 'List[int]', subset: 'List[int]', cur: 'int'):
        self.res.append(subset)
        if cur == len(nums):
            return
        while cur < len(nums):
            # pick current value
            self.backtrack(nums, subset + [nums[cur]], cur + 1)
            # skip same values
            while cur + 1 < len(nums) and nums[cur + 1] == nums[cur]:
                cur += 1
            cur += 1
        return

    def subsetsWithDup_2(self, nums: 'List[int]') -> 'List[List[int]]':
        res = [[]]
        for num in sorted(nums):
            res += [i + [num] for i in res if i + [num] not in res]
        return res

if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 2]
    print(a.subsetsWithDup(nums))
    print(a.subsetsWithDup_1(nums))
    print(a.subsetsWithDup_2(nums))