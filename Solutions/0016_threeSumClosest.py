# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 0008 18:41
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0016_threeSumClosest.py
# @Software: PyCharm

'''
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums
such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: 'list[int]', target: 'int') -> 'int':
        if not nums or len(nums) < 3:
            return None
        min_val = nums[0] + nums[1] + nums[2]
        min_diff = abs(min_val - target)
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    val = nums[i] + nums[j] + nums[k]
                    diff = abs(val - target)
                    if diff < min_diff:
                        min_diff = diff
                        min_val = val
        return min_val

    def threeSumClosest_1(self, nums: 'list[int]', target: 'int') -> 'int':
        nums.sort()
        min_dif = 2 ** 31 - 1
        res = 0
        for i in range(len(nums) - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            right = len(nums) - 1
            left = i + 1

            while (right > left):
                dif = nums[i] + nums[left] + nums[right] - target
                if min_dif > abs(dif):
                    min_dif = abs(dif)
                    res = nums[i] + nums[left] + nums[right]
                if dif > 0:
                    right -= 1
                elif dif < 0:
                    left += 1
                else:
                    return target
        return res

    def threeSumClosest_2(self, nums: 'list[int]', target: 'int') -> 'int':
        nums.sort()
        min_dif = 2 ** 31 - 1
        res = 0
        for i in range(len(nums) - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            two_sum = target - nums[i]
            right = len(nums) - 1
            left = i + 1
            while (right > left):
                dif = two_sum - nums[right] - nums[left]
                if (min_dif > abs(dif)):
                    min_dif = abs(dif)
                    res = nums[i] + nums[left] + nums[right]
                if (dif < 0):
                    right -= 1
                elif (dif > 0):
                    left += 1
                elif (dif == 0):
                    return target
        return res

if __name__ == "__main__":
    a = Solution()
    nums = [0, 2, 1, -3]
    target = 1
    print(a.threeSumClosest(nums, target))
    print(a.threeSumClosest_1(nums, target))
    print(a.threeSumClosest_2(nums, target))