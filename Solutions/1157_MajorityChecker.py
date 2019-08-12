# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 11:23
# @Author  : Youpeng Li
# @Site    : 
# @File    : 1157_MajorityChecker.py
# @Software: PyCharm

'''
1157. Online Majority Element In Subarray

Implementing the class MajorityChecker, which has the following API:
MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
int query(int left, int right, int threshold) has arguments such that:
0 <= left <= right < arr.length representing a subarray of arr;
2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least threshold times,
or -1 if no such element exists.

Example:
MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2

Constraints:
1 <= arr.length <= 20000
1 <= arr[i] <= 20000
For each query, 0 <= left <= right < len(arr)
For each query, 2 * threshold > right - left + 1
The number of queries is at most 10000
'''

import bisect
from collections import defaultdict

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.dp = defaultdict(list)
        for i, v in enumerate(arr):
            self.dp[v].append(i)
        self.occur = sorted([(len(v), k) for k, v in self.dp.items()], reverse=True)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for o, v in self.occur:
            if o < threshold: break
            arr = self.dp[v]
            low = bisect.bisect_left(arr, left)
            high = bisect.bisect_right(arr, right)
            if high - low >= threshold:
                return v
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

if __name__ == "__main__":
    majorityChecker = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(majorityChecker.query(0, 5, 4))  # returns 1
    print(majorityChecker.query(0, 3, 3))  # returns -1
    print(majorityChecker.query(2, 3, 2))  # returns 2

    majorityChecker = MajorityChecker([2, 2, 1, 2, 1, 2, 2, 1, 1, 2])
    print(majorityChecker.query(2, 5, 4))  # returns -1
    print(majorityChecker.query(0, 5, 6))  # returns -1
    print(majorityChecker.query(0, 1, 2))  # returns 2
    print(majorityChecker.query(2, 3, 2))  # returns -1
    print(majorityChecker.query(6, 6, 1))  # returns 2
    print(majorityChecker.query(0, 3, 3))  # returns 2
    print(majorityChecker.query(4, 9, 6))  # returns -1
    print(majorityChecker.query(4, 8, 4))  # returns -1
    print(majorityChecker.query(5, 9, 5))  # returns -1
    print(majorityChecker.query(0, 1, 2))  # returns 2