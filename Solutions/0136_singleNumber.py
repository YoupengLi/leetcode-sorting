# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 7:59
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0136_singleNumber.py
# @Software: PyCharm

'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

import operator
from functools import reduce

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        if not nums:
            return
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

    def singleNumber_1(self, nums: 'List[int]') -> 'int':
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber_2(self, nums: 'List[int]') -> 'int':
        return reduce(lambda n, res: res ^ n, nums)

    def singleNumber_3(self, nums: 'List[int]') -> 'int':
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber_4(self, nums: 'List[int]') -> 'int':
        return reduce(operator.xor, nums)

if __name__ == "__main__":
    a = Solution()
    nums = [2, 2, 1]
    print(a.singleNumber(nums))
    print(a.singleNumber_1(nums))
    print(a.singleNumber_2(nums))
    print(a.singleNumber_3(nums))
    print(a.singleNumber_4(nums))
    nums = [4, 1, 2, 1, 2]
    print(a.singleNumber(nums))
    print(a.singleNumber_1(nums))
    print(a.singleNumber_2(nums))
    print(a.singleNumber_3(nums))
    print(a.singleNumber_4(nums))