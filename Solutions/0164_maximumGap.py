# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 15:31
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0164_maximumGap.py
# @Software: PyCharm

'''
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Return 0 if the array contains less than 2 elements.

Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Note:
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
'''

import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i - 1])
        return res

    def maximumGap_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        K = int(math.ceil(math.log(2 ** 31, 10)))  # 用K位数可表示任意整数
        bucket = [[] for _ in range(10)]
        for i in range(K):  # K次循环
            for val in nums:
                bucket[val % (10 ** (i + 1)) // (10 ** i)].append(val)  # 析取整数第K位数字 （从低到高）
            del nums[:]
            for each in bucket:
                nums.extend(each)  # 桶合并
            bucket = [[] for _ in range(10)]
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i - 1])
        return res

if __name__  == "__main__":
    a = Solution()
    nums = [3, 6, 9, 1]
    print(a.maximumGap(nums))
    print(a.maximumGap_1(nums))
    nums = [10]
    print(a.maximumGap(nums))
    print(a.maximumGap_1(nums))
    nums = [0, 2**31]
    print(a.maximumGap(nums))
    print(a.maximumGap_1(nums))