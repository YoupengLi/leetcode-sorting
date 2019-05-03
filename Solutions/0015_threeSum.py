# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 0008 11:58
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0015_threeSum.py
# @Software: PyCharm

'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: list[int]) -> 'list[int]':
        if not nums or len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    a = [nums[i], nums[j], nums[k]]
                    if a not in res:
                        res.append(a)
                elif val < 0:
                    j += 1
                else:
                    k -= 1
        return res

    def threeSum_1(self, nums: list[int]) -> 'list[int]':
        gez = []
        sz = []
        hashmap = {}
        output = []
        for i in nums:
            if i >= 0:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    gez.append(i)
                    hashmap[i] = 1
            else:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    sz.append(i)
                    hashmap[i] = 1
        if 0 in hashmap and hashmap[0] >= 3:
            output.append([0, 0, 0])

        for i in gez:
            for j in sz:
                target = -(i + j)
                if target in hashmap and target in (i, j) and hashmap[target] > 1:
                    output.append([i, j, target])
                elif target in hashmap and (target > i or j < target < 0):
                    output.append([i, j, target])
        return output

if __name__ == "__main__":
    a = Solution()
    nums = [3, 0, -2, -1, 1, 2]
    print(a.threeSum_1(nums))