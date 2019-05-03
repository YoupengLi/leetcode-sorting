# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 0010 09:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0018_fourSum.py
# @Software: PyCharm

'''
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
from itertools import combinations
class Solution:
    def fourSum(self, nums: 'list[int]', target: 'int') -> 'list[int]':
        # 解法超时
        res = []
        if len(nums) <= 4:
            return res
        nums.sort()
        com = list(combinations(nums, 4))
        sum = 0
        for i in com:
            sum = i[0] + i[1] + i[2] + i[3]
            if sum == target and list(i) not in res:
                res.append(list(i))
        return res

    def fourSum_1(self, nums: 'list[int]', target: 'int') -> 'list[int]':
        n, res, dict = len(nums), set(), {}
        if n < 4:
            return []
        if n == 4:
            return [nums] if sum(nums) == target else []
        nums.sort()
        if target > nums[-1] * 4:
            return []
        for p in range(n):
            for q in range(p + 1, n):
                if nums[p] + nums[q] not in dict:
                    dict[nums[p] + nums[q]] = [(p, q)]
                else:
                    dict[nums[p] + nums[q]].append((p, q))
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                T = target - nums[i] - nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        res = [list(i) for i in res]
        return res

if __name__ == "__main__":
    a = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(a.fourSum(nums, target))
    print(a.fourSum_1(nums, target))
    nums = [-477, -476, -471, -462, -440, -400, -398, -394, -394, -393, -389, -386, -350, -346, -338, -315,
            -273, -249, -182, -172, -166, -161, -149, -116, -112, -109, -100, -73, -33, -26, -22, -11, 6, 8,
            13, 19, 56, 78, 101, 102, 111, 140, 155, 158, 181, 205, 211, 225, 232, 242, 254, 265, 281, 308,
            310, 320, 320, 364, 366, 381, 385, 387, 443, 496, 496]
    target = 1236
    print(a.fourSum(nums, target))
    print(a.fourSum_1(nums, target))
