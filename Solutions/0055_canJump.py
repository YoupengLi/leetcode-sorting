# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 0007 20:20
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0055_canJump.py
# @Software: PyCharm

'''
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''


class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        if not nums or len(nums) <= 0:
            return True
        goal = len(nums) - 1
        for i in range(len(nums)-1)[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

    def canJump_1(self, nums: 'List[int]') -> 'bool':
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True

if __name__ == "__main__":
    a = Solution()
    nums = [2, 3, 1, 1, 4]
    res = a.canJump(nums)
    print(res)
    res = a.canJump_1(nums)
    print(res)
    nums = [3, 2, 1, 0, 4]
    res = a.canJump(nums)
    print(res)
    res = a.canJump_1(nums)
    print(res)
    nums = [3, 4, 1, 0, 4]
    res = a.canJump(nums)
    print(res)
    res = a.canJump_1(nums)
    print(res)