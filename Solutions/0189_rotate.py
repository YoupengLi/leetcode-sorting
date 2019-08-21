# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 12:16
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0189_rotate.py
# @Software: PyCharm

'''
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

import collections

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k %= len(nums)
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])

    def rotate_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

    # O(n) space
    def rotate_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        deque = collections.deque(nums)
        k %= len(nums)
        for _ in range(k):
            deque.appendleft(deque.pop())
        nums[:] = list(deque)

    def rotate_3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k %= len(nums)
        size = len(nums)
        temp1 = nums[(size - k):size]
        temp2 = nums[0:(size - k)]
        nums[0:k] = temp1
        nums[k:size] = temp2


if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    a.rotate(nums, k)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    a.rotate_1(nums, k)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    a.rotate_2(nums, k)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    a.rotate_3(nums, k)
    print(nums)