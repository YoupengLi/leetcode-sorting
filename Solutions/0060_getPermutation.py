# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 0016 07:03
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0060_getPermutation.py
# @Software: PyCharm

'''
60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
we get the following sequence for n = 3:
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
Given n and k, return the kth permutation sequence.

Note:
    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
'''

from math import factorial
class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        nums = ""
        nums = [nums+str(i) for i in range(1, n+1)]
        nums = ''.join(nums)
        res = []
        self.dfs(nums, [], res)
        return ''.join(res[k-1])

    def dfs(self, nums: 'list[int]', path: 'list[str]', res: 'list[list[str]]'):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    def getPermutation_1(self, n: 'int', k: 'int') -> 'str':
        ns = [str(i + 1) for i in range(n)]
        s = ""
        k -= 1
        while ns:
            q, k = divmod(k, factorial(n - 1))
            s += ns.pop(q)
            n -= 1
        return s

if __name__ == "__main__":
    a = Solution()
    n = 9
    k = 171699
    res = a.getPermutation(n, k)
    print(res)
    res = a.getPermutation_1(n, k)
    print(res)
    n = 3
    k = 6
    res = a.getPermutation(n, k)
    print(res)
    res = a.getPermutation_1(n, k)
    print(res)