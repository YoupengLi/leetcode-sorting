# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 0007 20:08
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0011_maxArea.py
# @Software: PyCharm

'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height: 'list[int]') -> 'int':
        max_area = 0
        l = 0
        r = len(height)-1
        while l < r:
            d = r - l
            if height[l] < height[r]:
                h = height[l]
                l = l + 1
            else:
                h = height[r]
                r = r - 1
            area = d * h
            if area > max_area:
                max_area = area
        return max_area

if __name__ == "__main__":
    a = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(a.maxArea(height))