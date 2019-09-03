# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 22:52
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0217_containsDuplicate.py
# @Software: PyCharm

'''
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False

    def containsDuplicate_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in nums:
            if i in dic:
                return True
            dic[i] = 1
        return False

if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3, 1]
    print(a.containsDuplicate(nums))
    print(a.containsDuplicate_1(nums))
    nums = [1, 2, 3, 4]
    print(a.containsDuplicate(nums))
    print(a.containsDuplicate_1(nums))
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(a.containsDuplicate(nums))
    print(a.containsDuplicate_1(nums))