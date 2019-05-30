# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 9:16
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0075_sortColors.py
# @Software: PyCharm

'''
75. Sort Colors

Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''

class Solution:
    def sortColors(self, nums: 'List[int]') -> 'List[int]':
        """
        Do not return anything, modify nums in-place instead.
        """
        # basically do a double partition, around 1 and 0 pivots
        def order(a):
            # i and k are the indices of pivot 0 and 1

            i, k, n = -1, -1, len(a)
            for j in range(n):

                # If less than pivot 1, increment k and swap a[j] with a[k]
                # If also less than pivot 0, increment i and swap a[k] with a[i]

                if a[j] <= 1:
                    k += 1
                    a[k], a[j] = a[j], a[k]
                    if a[k] == 0:
                        i += 1
                        a[k], a[i] = a[i], a[k]
        if not nums:
            return
        order(nums)
        return

    def sortColors_1(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low = low + 1
                mid = mid + 1
            elif nums[mid] == 1:
                mid = mid + 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1
        return

if __name__ == "__main__":
    a = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    a.sortColors(nums)
    print(nums)
    nums = [2, 0, 2, 1, 1, 0]
    a.sortColors_1(nums)
    print(nums)