# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 0022 上午 8:28
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0004_findMedianSortedArrays.py
# @Software: PyCharm

'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

详细分析见网址：https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
'''

class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        sorted_joined = sorted(nums1 + nums2)
        if len(sorted_joined) % 2 == 0:
            index = int(len(sorted_joined) / 2)
            return (sorted_joined[index] + sorted_joined[index - 1]) / 2
        else:
            index = int(len(sorted_joined) / 2)
            return sorted_joined[index]

    def findMedianSortedArrays_1(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

if __name__ == "__main__":
    a = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(a.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(a.findMedianSortedArrays_1(nums1, nums2))