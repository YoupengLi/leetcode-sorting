# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 0020 19:37
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0034_searchRange.py
# @Software: PyCharm

'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if not nums or nums[0] > target:
            return [-1, -1]
        res = [0, 0]
        count = 0
        for i in range(len(nums)):
            if nums[i] < target:
                continue
            elif nums[i] == target:
                count += 1
                if count == 1:
                    res[0] = i
            else:
                break
        if count == 0:
            return [-1, -1]
        elif count == 1:
            res[1] = res[0]
            return res
        else:
            if nums[i] == target:
                res[1] = i
                return res
            else:
                res[1] = i-1
                return res

    def searchRange_1(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if not nums or nums[0] > target:
            return [-1, -1]
        flag = False
        for i in range(len(nums)):
            if nums[i] == target:
                flag = True
                break
        if not flag:
            return [-1, -1]

        if nums[-1] == target:
            return [i, len(nums)-1]
        for j in range(i, len(nums)):
            if nums[j] != target:
                return [i, j-1]
        return [i, i]

    def searchRange_2(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if not nums or nums[0] > target:
            return [-1, -1]
        return [self.get_start_index(nums, target), self.get_end_index(nums, target)]

    def get_start_index(self, nums: 'List[int]', target: 'int') -> 'int':
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def get_end_index(self, nums: 'List[int]', target: 'int') -> 'int':
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def searchRange_3(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        i, j = 0, 0
        for i in range(len(nums)):
            if nums[i] == target:
                break
        else:
            return [-1, -1]

        for j in range(i + 1, len(nums)):
            if nums[j] != target:
                return [i, j - 1]
        else:
            return [i, j or i]

if __name__ == "__main__":
    a = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = a.searchRange(nums, target)
    print(res)
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = a.searchRange_1(nums, target)
    print(res)
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = a.searchRange_2(nums, target)
    print(res)
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = a.searchRange_3(nums, target)
    print(res)
    nums = [1, 4]
    target = 4
    res = a.searchRange(nums, target)
    print(res)
    res = a.searchRange_1(nums, target)
    print(res)
    res = a.searchRange_2(nums, target)
    print(res)
    res = a.searchRange_3(nums, target)
    print(res)