# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 10:29
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0153_findMin.py
# @Software: PyCharm

'''
153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        front, rear = 0, len(nums)-1
        mid = front
        while nums[front] >= nums[rear]:
            if rear - front == 1:
                mid = rear
                break
            mid = (front + rear) // 2
            if nums[front] == nums[rear] and nums[front] == nums[mid]:
                return self.minOrder(nums, front, rear)
            if nums[front] <= nums[mid]:
                front = mid
            elif nums[rear] >= nums[mid]:
                rear = mid
        return nums[mid]

    def minOrder(self, nums, front, rear):
        res = nums[0]
        for i in nums[front:rear+1]:
            if i < res:
                res = i
        return res

    def findMin_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

if __name__  == "__main__":
    a = Solution()
    nums = [1, 2, 3, 4, 5]
    print(a.findMin(nums))
    print(a.findMin_1(nums))
    nums = [3, 4, 5, 1, 2]
    print(a.findMin(nums))
    print(a.findMin_1(nums))
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(a.findMin(nums))
    print(a.findMin_1(nums))