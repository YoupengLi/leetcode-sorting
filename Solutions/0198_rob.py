# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 8:30
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0198_rob.py
# @Software: PyCharm

'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

class Solution(object):
    # O(n) space
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(nums[i] + res[i - 2], res[i - 1])
        return res[-1]

    # O(n) space
    def rob_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[0] = nums[0]
            elif i == 1:
                res[1] = max(nums[0], nums[1])
            else:
                res[i] = max(nums[i] + res[i - 2], res[i - 1])
        return res[-1]

    # Constant space
    def rob_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = b
            b = max(nums[i] + a, b)
            a = tmp
        return b

    def rob_3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [[0 for i in range(len(nums) + 1)] for j in range(2)]
        dp[0][1] = 0
        dp[1][1] = nums[0]
        for j in range(2, len(nums) + 1):
            dp[0][j] = max(dp[0][j - 1], dp[1][j - 1])
            dp[1][j] = nums[j - 1] + max(dp[0][j - 2], dp[1][j - 2])
        return max(dp[0][len(nums)], dp[1][len(nums)])

if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3, 1]
    print(a.rob(nums))
    print(a.rob_1(nums))
    print(a.rob_2(nums))
    print(a.rob_3(nums))
    nums = [2, 7, 9, 3, 1]
    print(a.rob(nums))
    print(a.rob_1(nums))
    print(a.rob_2(nums))
    print(a.rob_3(nums))