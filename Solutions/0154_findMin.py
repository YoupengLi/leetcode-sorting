# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 8:36
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0154_findMin.py
# @Software: PyCharm

'''
154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        front, rear = 0, len(nums) - 1
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
        for i in nums[front:rear + 1]:
            if i < res:
                res = i
        return res

    def findMin_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

if __name__  == "__main__":
    a = Solution()
    nums = [1, 3, 5]
    print(a.findMin(nums))
    print(a.findMin_1(nums))
    nums = [2, 2, 2, 0, 1]
    print(a.findMin(nums))
    print(a.findMin_1(nums))