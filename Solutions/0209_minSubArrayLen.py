# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 20:55
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0209_minSubArrayLen.py
# @Software: PyCharm

'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''

class Solution(object):
    # O(n) time
    # we scan from left to right, "total" tracks the
    # sum of the subarray. If the sum is less than s,
    # right moves forward one step, else left moves forward
    # one step, left and right form a window.
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = right = 0
        res = len(nums) + 1
        while right < len(nums):
            total += nums[right]
            while total >= s:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return res if res <= len(nums) else 0

    def minSubArrayLen_1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sumtmp = 0  # from left to cur
        left = 0
        res = float('inf')
        for i in range(len(nums)):
            sumtmp += nums[i]
            while sumtmp >= s:
                res = min(res, i - left + 1)
                sumtmp -= nums[left]
                left += 1
        return res if res != float('inf') else 0

if __name__ == "__main__":
    a = Solution()
    s, nums = 7, [2, 3, 1, 2, 4, 3]
    print(a.minSubArrayLen(s, nums))
    print(a.minSubArrayLen_1(s, nums))