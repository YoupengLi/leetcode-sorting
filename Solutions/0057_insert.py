# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 0008 09:17
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0057_insert.py
# @Software: PyCharm

'''
57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
import pandas as pd
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        if not intervals or len(intervals) <= 0:
            return [newInterval]
        if intervals[0].start > newInterval.end:
            intervals.insert(0, newInterval)
            return intervals
        if intervals[-1].end < newInterval.start:
            intervals.append(newInterval)
            return intervals
        overlap = []
        ind = 0
        flag = True
        for i in range(len(intervals)):
            if self.isOverlap(intervals[i], newInterval):
                if flag == True:
                    ind = i
                    flag = False
                overlap.append(intervals[i])
            if overlap and not self.isOverlap(intervals[i], newInterval):
                break
            else:
                if intervals[i].start > newInterval.end:
                    ind = i
                    break
        if overlap:
            merged = Interval(min(overlap[0].start, newInterval.start), max(overlap[-1].end, newInterval.end))
            for i in overlap:
                intervals.remove(i)
            intervals.insert(ind, merged)
        else:
            intervals.insert(ind, newInterval)
        return intervals

    def isOverlap(self, interval, newInterval):
        if interval.end < newInterval.start or interval.start > newInterval.end:
            return False
        else:
            return True

    def insert_1(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        '''
        res = []
        insert_pos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                res.append(interval)
                insert_pos += 1
            elif interval.start > newInterval.end:
                res.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        res.insert(insert_pos, newInterval)
        return res
        '''
        lo, hi = 0, len(intervals)
        while lo < hi:
            mid = (lo + hi) // 2
            if intervals[mid].end < newInterval.start:
                lo = mid + 1
            else:
                hi = mid

        left_interval_index = lo

        # find the highest start that is lower than newInterval.end
        lo, hi = left_interval_index, len(intervals)
        while lo < hi:
            mid = (lo + hi) // 2
            if intervals[mid].start <= newInterval.end:
                lo = mid + 1
            else:
                hi = mid

        right_interval_index = lo - 1

        if left_interval_index < len(intervals):
            newInterval.start = min(newInterval.start, intervals[left_interval_index].start)
        if right_interval_index >= 0:
            newInterval.end = max(newInterval.end, intervals[right_interval_index].end)

        return intervals[:left_interval_index] + [newInterval] + intervals[right_interval_index + 1:]

if __name__ == "__main__":
    a = Solution()
    intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
    newInterval = Interval(4, 8)
    res = a.insert(intervals, newInterval)
    print(res)
    intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
    newInterval = Interval(4, 8)
    res = a.insert_1(intervals, newInterval)
    print(res)

    intervals = [Interval(1, 5)]
    newInterval = Interval(2, 3)
    res = a.insert(intervals, newInterval)
    print(res)
    intervals = [Interval(1, 5)]
    newInterval = Interval(2, 3)
    res = a.insert_1(intervals, newInterval)
    print(res)

    intervals = [Interval(3, 5), Interval(12, 15)]
    newInterval = Interval(6, 6)
    res = a.insert(intervals, newInterval)
    print(res)
    intervals = [Interval(3, 5), Interval(12, 15)]
    newInterval = Interval(6, 6)
    res = a.insert_1(intervals, newInterval)
    print(res)


