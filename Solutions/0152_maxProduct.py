# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 0006 22:47
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0152_maxProduct.py
# @Software: PyCharm

'''
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

解题思路：
本题要求连续子数组的最大乘积，思路与求连续子数组的最大和相似，都是采用动态规划，
maxvalue[i]maxvalue[i]表示以a[i]a[i]为结尾的子数组中最大乘积，同时维护一个全局最大值globalmaxglobalmax，
记录maxvalue[i]maxvalue[i]中的最大值。与求子数组的最大和不同的是，还需要维记录子数组最小乘积minvalue[i]minvalue[i]，
因为可能会出现 负×负=正 的情况，并且最大最小乘积只可能出现在
(maxvalue[i−1]×a[i],minvalue[i−1]×a[i],a[i])(maxvalue[i−1]×a[i],minvalue[i−1]×a[i],a[i])三者之间。
'''
class Solution:
    def maxProduct(self, nums: 'List[int]') -> 'int':
        prev_min = prev_max = global_max = nums[0]
        for num in nums[1:]:
            minn, maxx = min(num, prev_max * num, prev_min * num), max(num, prev_max * num, prev_min * num)
            prev_min, prev_max, global_max = minn, maxx, max(global_max, maxx)
        return global_max

    def maxProduct_1(self, nums: 'List[int]') -> 'int':
        front_max = front_min = global_max = nums[0]
        for num in nums[1:]:
            front_max, front_min = max(num, front_max * num, front_min * num), min(num, front_max * num, front_min * num)
            global_max = max(global_max, front_max)
        return global_max

    def maxProduct_2(self, nums: 'List[int]') -> 'int':
        revs = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            revs[i] *= revs[i - 1] or 1
        return max(nums + revs)

if __name__ == "__main__":
    a = Solution()
    nums = [2, 3, -2, 4]
    print(a.maxProduct(nums))
    print(a.maxProduct_1(nums))
    print(a.maxProduct_2(nums))
    nums = [-2, 0, -1]
    print(a.maxProduct(nums))
    print(a.maxProduct_1(nums))
    print(a.maxProduct_2(nums))