# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 0023 17:26
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0042_trap.py
# @Software: PyCharm

'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        res = 0
        if len(height) <= 0:
            return res
        for i in range(1, len(height)-1):
            max_left = 0
            max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            res += min(max_left, max_right) - height[i]
        return res

    def trap_1(self, height: 'List[int]') -> 'int':
        res = 0
        if len(height) <= 0:
            return res
        max_left = [height[0]] * len(height)
        max_right = [height[-1]] * len(height)
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])
            max_right[-i-1] = max(max_right[-i], height[-i-1])
        for i in range(1, len(height)-1):
            res += min(max_left[i], max_right[i]) - height[i]
        return res

if __name__ == "__main__":
    a = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = a.trap(height)
    print(res)
    res = a.trap_1(height)
    print(res)
    height = [2, 0, 2]
    res = a.trap(height)
    print(res)
    res = a.trap_1(height)
    print(res)