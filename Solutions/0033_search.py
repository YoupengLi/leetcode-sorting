# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 0020 08:42
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0033_search.py
# @Software: PyCharm

'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        '''
        Only three cases when we need to choose the left part (m = (left + right + 1) // 2):
        left = 0, m = 3, right = 6
        [4,5,6,7,0,1,2] target 5: nums[left] <= target <= nums[m]
        [6,7,0,1,2,4,5] target 7: nums[m] <= nums[left] <= target
        [6,7,0,1,2,4,5] target 0: target <= nums[m] <= nums[left]
        '''
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right + 1) // 2
            if nums[m] == target:
                return m
            elif nums[m] <= nums[left] <= target or nums[left] <= target <= nums[m] or target <= nums[m] <= nums[left]:
                right = m - 1
            else:
                left = m + 1
        return -1

if __name__ == "__main__":
    a = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 7
    res = a.search(nums, target)
    print(res)