# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 0024 16:42
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0283_moveZeroes.py
# @Software: PyCharm

'''
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0
        return

    def moveZeroes_1(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        zero = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

if __name__ == "__main__":
    a = Solution()
    nums = [0, 1, 0, 3, 12]
    a.moveZeroes(nums)
    print(nums)
    nums = [0, 1, 0, 3, 12, 5, 8]
    a.moveZeroes_1(nums)
    print(nums)