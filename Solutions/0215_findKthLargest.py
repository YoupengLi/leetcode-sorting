# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 8:43
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0215_findKthLargest.py
# @Software: PyCharm

'''
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        for i in range(k):
            res = -heapq.heappop(heap)
        return res

    def findKthLargest_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        left = [l for l in nums if l < pivot]
        equal = [e for e in nums if e == pivot]
        right = [r for r in nums if r > pivot]
        if k <= len(right):
            return self.findKthLargest(right, k)
        elif k - len(right) <= len(equal):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))

if __name__ == "__main__":
    a = Solution()
    nums, k = [3, 2, 1, 5, 6, 4], 2
    print(a.findKthLargest(nums, k))
    print(a.findKthLargest_1(nums, k))
    print(a.findKthLargest_2(nums, k))
    nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    print(a.findKthLargest(nums, k))
    print(a.findKthLargest_1(nums, k))
    print(a.findKthLargest_2(nums, k))