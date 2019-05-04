# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 0006 11:09
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0045_jump.py
# @Software: PyCharm

'''
45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        # 贪心算法
        cur = 0
        count = 0
        pos = 0
        while cur < len(nums)-1:
            count += 1
            pre = cur
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count

if __name__ == "__main__":
    a = Solution()
    nums = [2, 3, 1, 1, 4]
    res = a.jump(nums)
    print(res)