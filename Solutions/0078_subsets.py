# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 8:01
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0078_subsets.py
# @Software: PyCharm

'''
78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums:
            return [[]]
        # without using built-in functions
        def backtrack(start: 'int', end: 'int', templist: 'List[int]', res: 'List[List[int]]'):
            res.append(templist[:])
            for i in range(start, end):
                templist.append(nums[i])
                backtrack(i + 1, end, templist, res)
                templist.pop()
        res = []
        backtrack(0, len(nums), [], res)
        return res

    def subsets_1(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums:
            return [[]]
        else:
            a, b = self.subsets_1(nums[:-1]), nums[-1]
            return list(map(lambda x: x + [b], a)) + a

if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3]
    res = a.subsets_1(nums)
    print(res)
    nums = [0]
    res = a.subsets(nums)
    print(res)