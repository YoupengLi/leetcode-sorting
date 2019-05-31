# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 16:28
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0077_combine.py
# @Software: PyCharm

'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        if k == 0 or k > n:
            return [[]]
        # without using built-in functions
        def backtrack(start: 'int', K: 'int', templist: 'List[int]', res: 'List[List[int]]'):
            if K == 0:
                res.append(templist[:])
            else:
                for i in range(start, n + 1):
                    templist.append(i)
                    backtrack(i + 1, K - 1, templist, res)
                    templist.pop()
        res = []
        backtrack(1, k, [], res)
        return res

    def combine_1(self, n: 'int', k: 'int') -> 'List[List[int]]':
        if k == 0 or k > n:
            return [[]]
        res = [[i] for i in range(1, n - k + 2)]
        for m in range(1, k):  # the spot we are filling
            new_res = []
            for result in res:
                for i in range(result[-1] + 1, n - k + m + 2):
                    new_res += [result + [i]]
            res = new_res
        return res

if __name__ == "__main__":
    a = Solution()
    n = 4
    k = 3
    res = a.combine(n, k)
    print(res)
    res = a.combine_1(n, k)
    print(res)