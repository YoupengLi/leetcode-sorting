# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 21:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0128_longestConsecutive.py
# @Software: PyCharm

'''
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_streak = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_streak += 1

                res = max(res, cur_streak)
        return res

    def longestConsecutive_1(self, nums: 'List[int]') -> 'int':
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num + 1
                while cur_num in num_set:
                    cur_num += 1

                res = max(res, cur_num - num)
        return res

if __name__  == "__main__":
    a = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(a.longestConsecutive(nums))
    print(a.longestConsecutive_1(nums))