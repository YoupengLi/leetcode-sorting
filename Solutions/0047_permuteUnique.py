# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 14:48
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0047_permuteUnique.py
# @Software: PyCharm

'''
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums: 'List[int]', path: 'List[int]', res: 'List[list[int]]'):
        if not nums and path not in res:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    def permuteUnique_1(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums or len(nums) == 0:
            return []
        nums.sort()
        res = []
        self.dfs_1(nums, [], [False for _ in range(len(nums))], res)
        return res

    def dfs_1(self, nums: 'List[int]', lst: 'List[int]', used: 'List[bool]', res: 'List[list[int]]'):
        if len(lst) == len(nums):
            res.append(list(lst))
            return
        prev = -1
        for i in range(len(nums)):
            if used[i]:
                continue
            if prev >= 0 and nums[i] == nums[prev]:
                continue
            lst.append(nums[i])
            used[i] = True
            self.dfs_1(nums, lst, used, res)
            used[i] = False
            lst.pop()
            prev = i

if __name__ == "__main__":
    a = Solution()
    nums = [1, 1, 2]
    res = a.permuteUnique(nums)
    print(res)
    res = a.permuteUnique_1(nums)
    print(res)