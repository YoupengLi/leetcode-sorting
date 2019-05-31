# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 10:40
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0080_removeDuplicates.py
# @Software: PyCharm

'''
80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place
such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7,
with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
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
        if not nums:
            return 0
        count = 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                count = 1
            if nums[i] == nums[i + 1]:
                count += 1
                if count <= 2:
                    i += 1
                    continue
                else:
                    del nums[i]
                    continue
            i += 1
        return len(nums)

    def removeDuplicates_1(self, nums: 'List[int]') -> 'int':
        if len(nums) <= 2:
            return len(nums)

        tail = 1
        for i in range(2, len(nums)):
            if nums[i] == nums[tail] and nums[i] == nums[tail - 1]:
                pass
            else:  # when the current element does not equal to the two previous elemetnts in the answer subarray
                tail += 1
                nums[tail] = nums[i]
        # for each element after the first two in the array, we have a choice to either include it in the answer subarray, or skip it
        return tail + 1

if __name__ == "__main__":
    a = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    res = a.removeDuplicates(nums)
    print(res)
    print(nums)
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    res = a.removeDuplicates_1(nums)
    print(res)
    print(nums)