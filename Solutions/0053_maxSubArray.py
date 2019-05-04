# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 0007 16:07
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0053_maxSubArray.py
# @Software: PyCharm

'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if not nums or len(nums) <= 0:
            return 0
        sum = 0
        res = nums[0]
        for i in range(len(nums)):
            if sum <= 0:
                sum = nums[i]
            else:
                sum += nums[i]
            if sum > res:
                res = sum
        return res

    def maxSubArray_1(self, nums: 'List[int]') -> 'int':
        if not nums or len(nums) <= 0:
            return 0
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res

    def maxSubArray_2(self, nums: 'List[int]') -> 'int':
        res, sum = nums[0], 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > res:
                res = sum
            if sum < 0:
                sum = 0
        return res

if __name__ == "__main__":
    a = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = a.maxSubArray(nums)
    print(res)
    res = a.maxSubArray_1(nums)
    print(res)
    res = a.maxSubArray_2(nums)
    print(res)
    nums = [-2, -3, -1]
    res = a.maxSubArray(nums)
    print(res)
    res = a.maxSubArray_1(nums)
    print(res)
    res = a.maxSubArray_2(nums)
    print(res)