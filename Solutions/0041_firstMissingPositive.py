# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 0023 16:42
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0041_firstMissingPositive.py
# @Software: PyCharm

'''
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
'''

class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        res = 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < res:
                continue
            elif nums[i] == res:
                res += 1
            else:
                return res
        return res

    def firstMissingPositive_1(self, nums: 'List[int]') -> 'int':
        nums = sorted(list({num for num in nums if num > 0}))
        prev = 0
        for num in nums:
            if num - prev > 1:
                return prev + 1
            prev = num
        return prev + 1

    def firstMissingPositive_2(self, nums: 'List[int]') -> 'int':
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        for i in range(n):
            if abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

if __name__ == "__main__":
    a = Solution()
    nums = [7, 8, 9, 11, 12]
    res = a.firstMissingPositive(nums)
    print(res)
    res = a.firstMissingPositive_1(nums)
    print(res)
    res = a.firstMissingPositive_2(nums)
    print(res)
    nums = [3, 4, -1, 1]
    res = a.firstMissingPositive(nums)
    print(res)
    res = a.firstMissingPositive_1(nums)
    print(res)
    res = a.firstMissingPositive_2(nums)
    print(res)