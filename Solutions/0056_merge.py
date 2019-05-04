# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 0008 08:33
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0056_merge.py
# @Software: PyCharm

'''
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged

if __name__ == "__main__":
    a = Solution()
    intervals = [Interval(2, 6), Interval(8, 10), Interval(15, 18), Interval(1, 3)]
    res = a.merge(intervals)
    print(res)