# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 0016 上午 8:19
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0001_twoSum.py
# @Software: PyCharm

'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

解题思路：
<1> 建立字典 dict1 存放第一个数字，并存放该数字的 index
<2> 判断 (target - 当前数字) 在 dict1 中是否存在：
如果存在，则返回： (target - 当前数字) 的 index 和 当前值的 index；
如果不存在，继续遍历。
'''

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        if not nums or len(nums) <= 0:
            return []

        dict1 = {}
        for index, value in enumerate(nums):
            if target - value in dict1:
                return [dict1[target - value], index]
            dict1[value] = index

        return []

if __name__ == "__main__":
    a = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(a.twoSum(nums, target))
    nums = [3, 2, 3]
    target = 6
    print(a.twoSum(nums, target))