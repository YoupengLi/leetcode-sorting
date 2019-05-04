# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 0023 17:40
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0066_plusOne.py
# @Software: PyCharm

'''
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        if not digits:
            return []
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

    def plusOne_1(self, digits: 'List[int]') -> 'List[int]':
        if set(digits) == {9}:
            return [1] + [0] * len(digits)
        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]
        return self.plusOne(digits[:-1]) + [0]

if __name__ == "__main__":
    a = Solution()
    digits = [4, 3, 2, 1]
    res = a.plusOne(digits)
    print(res)
    res = a.plusOne_1(digits)
    print(res)
    digits = [9, 9, 9, 9]
    res = a.plusOne(digits)
    print(res)
    res = a.plusOne_1(digits)
    print(res)