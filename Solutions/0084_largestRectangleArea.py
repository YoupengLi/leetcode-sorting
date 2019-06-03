# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 8:05
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0084_largestRectangleArea.py
# @Software: PyCharm

'''
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10

Explaination:
The stack maintain the indexes of buildings with ascending height.
Before adding a new building pop the building who is taller than the new one.
The building popped out represent the height of a rectangle with the new building as the right boundary
and the current stack top as the left boundary. Calculate its area and update ans of maximum area.
Boundary is handled using dummy buildings.

'''

import numpy as np
class Solution:
    # Method 1: Memory Limit Exceeded
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        if not heights:
            return 0
        l = len(heights)
        idx = heights.index(min(heights))

        val1 = heights[idx] * l

        if idx != 0:
            val2 = self.largestRectangleArea(heights[0:idx])
        else:
            val2 = heights[0]
        if idx != l - 1:
            val3 = self.largestRectangleArea(heights[idx + 1:l])
        else:
            val3 = heights[l-1]
        return max(val1, val2, val3)

    def largestRectangleArea_1(self, heights: 'List[int]') -> 'int':
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res

    def largestRectangleArea_2(self, heights: 'List[int]') -> 'int':
        def backtrack(stack, tup):
            best, last_i = 0, tup[0]
            while len(stack) > 0 and stack[-1][1] > tup[1]:
                curr = stack.pop()
                last_i = curr[0]
                d = (tup[0] - curr[0]) * (curr[1])
                if d > best:
                    best = d
            return best, last_i

        best = 0
        stack = [(-1, 0)]
        for i, h in enumerate(heights):
            tup = (i, h)
            if h > stack[-1][1]:
                stack.append(tup)
            elif h < stack[-1][1]:
                new_best, last_i = backtrack(stack, tup)
                stack.append((last_i, h))
                best = max(best, new_best)
        best = max(best, backtrack(stack, (len(heights), 0))[0])
        return best

if __name__ == "__main__":
    a = Solution()
    nums = [2, 1, 5, 6, 2, 3]
    res = a.largestRectangleArea_1(nums)
    print(res)
    nums = [0, 9]
    res = a.largestRectangleArea(nums)
    print(res)
    nums = np.arange(2000)
    nums = nums.tolist()
    res = a.largestRectangleArea_2(nums)
    print(res)