# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 8:20
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0137_singleNumber.py
# @Software: PyCharm

'''
137. Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
'''

from collections import Counter

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber_1(self, nums: 'List[int]') -> 'int':
        return (3 * sum(set(nums)) - sum(nums)) // 2

    def singleNumber_2(self, nums: 'List[int]') -> 'int':
        for x, y in Counter(nums).items():
            if y == 1:
                return x

    def singleNumber_3(self, nums: 'List[int]') -> 'int':
        '''
        当2第一次出现的时候，one = 2, two = 0,  one记录这个数字
        当2第二次出现的时候，one = 0, two = 2,  two记录这个数字
        当2第三次出现的时候，one = 0, two = 0,  都清空，去处理其他数字
        所以，如果有某个数字出现了1次，就存在one中，出现了两次，就存在two中，所以返回 one|two
        公式方面 ，上面两次的时候，one清空的公式是 one = one xor i
        第三次时，one要等于零，而这时two是True，所以再 & 一个two的非就可以，one = one xor i & ~ two
        one = one xor i & ~ two
        two = two xor i & ~ one
        '''
        one = two = 0
        for num in nums:
            one = one ^ num & ~ two
            two = two ^ num & ~ one
        return one | two

    def singleNumber_4(self, nums: 'List[int]') -> 'int':
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three
        return one

if __name__ == "__main__":
    a = Solution()
    nums = [2, 2, 3, 2]
    print(a.singleNumber(nums))
    print(a.singleNumber_1(nums))
    print(a.singleNumber_2(nums))
    print(a.singleNumber_3(nums))
    print(a.singleNumber_4(nums))
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(a.singleNumber(nums))
    print(a.singleNumber_1(nums))
    print(a.singleNumber_2(nums))
    print(a.singleNumber_3(nums))
    print(a.singleNumber_4(nums))