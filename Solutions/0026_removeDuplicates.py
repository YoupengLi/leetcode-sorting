# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 0017 10:24
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0026_removeDuplicates.py
# @Software: PyCharm

'''
26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.
Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2], Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference,
which means modification to the input array will be known to the caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

    def removeDuplicates_1(self, nums: 'List[int]') -> 'int':
        if len(nums) <= 1:
            return len(nums)
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[length-1]:
                nums[length] = nums[i]
                length += 1
        return length

if __name__ == "__main__":
    a = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = a.removeDuplicates(nums)
    print(res)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = a.removeDuplicates_1(nums)
    print(res)