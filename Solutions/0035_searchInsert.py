# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 0020 22:41
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0035_searchInsert.py
# @Software: PyCharm

'''
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
'''

class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def searchInsert_1(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid == len(nums) - 1 or target < nums[mid + 1]:
                    return mid + 1
                left = mid + 1
            else:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                right = mid - 1

    def searchInsert_2(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left + 1 <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[left] >= target:
            return left
        else:
            return left + 1

if __name__ == "__main__":
    a = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    res = a.searchInsert(nums, target)
    print(res)
    res = a.searchInsert_1(nums, target)
    print(res)
    res = a.searchInsert_2(nums, target)
    print(res)
    target = 0
    res = a.searchInsert(nums, target)
    print(res)
    res = a.searchInsert_1(nums, target)
    print(res)
    res = a.searchInsert_2(nums, target)
    print(res)