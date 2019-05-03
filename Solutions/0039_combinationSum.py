# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0021 20:48
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0039_combinationSum.py
# @Software: PyCharm

'''
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]


Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates, [], target, 0)
        return self.resList

    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.resList.append(sublist[:])
        if target < candidates[0]:
            return
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            sublist.append(n)
            self.dfs(candidates, sublist, target - n, n)
            sublist.pop()

if __name__ == "__main__":
    a = Solution()
    candidates = [2, 3, 5]
    target = 8
    res = a.combinationSum(candidates, target)
    print(res)
    candidates = [2, 3, 6, 7]
    target = 7
    res = a.combinationSum(candidates, target)
    print(res)
    candidates = [2, 3, 7]
    target = 18
    res = a.combinationSum(candidates, target)
    print(res)
    # [[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,2,3,7],[2,2,2,3,3,3,3],[2,2,7,7],[2,3,3,3,7],[3,3,3,3,3,3]]



