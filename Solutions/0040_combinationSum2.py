# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 0022 09:07
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0040_combinationSum2.py
# @Software: PyCharm

'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates, [], target, 0)
        return self.resList

    def dfs(self, candidates, sublist, target, last):
        if target == 0 and sublist not in self.resList:
            self.resList.append(sublist[:])
        if target < candidates[0]:
            return
        for i in range(last, len(candidates)):
            if candidates[i] > target:
                return
            if i < last:
                continue
            sublist.append(candidates[i])
            self.dfs(candidates, sublist, target - candidates[i], i+1)
            sublist.pop()

if __name__ == "__main__":
    a = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = a.combinationSum2(candidates, target)
    print(res)
    candidates = [2, 5, 2, 1, 2]
    target = 5
    res = a.combinationSum2(candidates, target)
    print(res)