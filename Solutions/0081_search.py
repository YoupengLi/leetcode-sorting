# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 16:50
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0081_search.py
# @Software: PyCharm

'''
81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''

class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'bool':
        if not nums:
            return False
        low = 0
        high = len(nums) - 1
        while low <= high:
            while low < high and nums[low] == nums[high]:  # 这样的目的是为了能准确判断mid位置，所以算法的最坏时间复杂度为O(n)
                low += 1
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[low]:  # 高区
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:  # 低区
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

if __name__ == "__main__":
    a = Solution()
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 6
    res = a.search(nums, target)
    print(res)