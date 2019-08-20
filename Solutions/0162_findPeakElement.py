# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 12:59
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0162_findPeakElement.py
# @Software: PyCharm

'''
162. Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:
Your solution should be in logarithmic complexity.
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return i-1
        return len(nums)-1

    def findPeakElement_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Recursive Binary Search
        # Time complexity : O(log(n))
        # Space complexity : O(log(n))
        if not nums:
            return
        return self.search(nums, 0, len(nums)-1)

    def search(self, nums, l, r):
        """
        :type nums: List[int]
        :type l, r: int
        :rtype: int
        """
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid+1]:
            return self.search(nums, l, mid)
        else:
            return self.search(nums, mid+1, r)

    def findPeakElement_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Iterative Binary Search
        # Time complexity : O(log(n))
        # Space complexity : O(1)
        if not nums:
            return
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l

if __name__  == "__main__":
    a = Solution()
    nums = [1, 2, 3, 1]
    print(a.findPeakElement(nums))
    print(a.findPeakElement_1(nums))
    print(a.findPeakElement_2(nums))
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(a.findPeakElement(nums))
    print(a.findPeakElement_1(nums))
    print(a.findPeakElement_2(nums))