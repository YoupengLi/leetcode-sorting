# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 10:38
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0169_majorityElement.py
# @Software: PyCharm

'''
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that
appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

from collections import Counter

class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement_1(self, nums: 'List[int]') -> 'int':
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement_2(self, nums: 'List[int]') -> 'int':
        c = Counter(nums)
        return c.most_common(1)[0][0]

if __name__  == "__main__":
    a = Solution()
    nums = [3, 2, 3]
    print(a.majorityElement(nums))
    print(a.majorityElement_1(nums))
    print(a.majorityElement_2(nums))
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(a.majorityElement(nums))
    print(a.majorityElement_1(nums))
    print(a.majorityElement_2(nums))