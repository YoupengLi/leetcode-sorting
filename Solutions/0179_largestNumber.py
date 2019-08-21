# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 9:00
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0179_largestNumber.py
# @Software: PyCharm

'''
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums or len(nums) <= 0:
            return ""
        nums = list(map(str, nums))
        # 在python3.x中已经没有cmp函数，要是用operator函数进行比较，cmp函数就是比较输入两个字符串之间大小的数字
        # cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
        # 是两两对象之间的比较，排序默认是从小到大，在这个函数内部实现的两两排序
        def cmp(x, y):
            if x + y < y + x:
                return -1
            if x + y > y + x:
                return 1
            return 0

        nums.sort(key=functools.cmp_to_key(cmp), reverse=True)
        res = ''.join(nums).lstrip('0')
        return res or '0'

if __name__  == "__main__":
    a = Solution()
    nums = [10, 2]
    print(a.largestNumber(nums))
    nums = [3, 30, 34, 5, 9]
    print(a.largestNumber(nums))