# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 0018 09:33
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0031_nextPermutation.py
# @Software: PyCharm

'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

这道题让我们求下一个排列顺序，有题目中给的例子可以看出来，如果给定数组是降序，则说明是全排列的最后一种情况，
则下一个排列就是最初始情况，可以参见之前的博客 Permutations 全排列。我们再来看下面一个例子，有如下的一个数组
1　　2　　7　　4　　3　　1

下一个排列为：
1　　3　　1　　2　　4　　7

那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，
然后我们再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：
1　　2　　7　　4　　3　　1

1　　3　　7　　4　　2　　1

1　　3　　1　　2　　4　　7
'''

class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'List[int]':
        """
        Do not return anything, modify nums in-place instead.
        """
        i, t = len(nums) - 1, len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:
            i -= 1
        i_orig = i
        if i > 0:
            while nums[t] <= nums[i - 1]:
                t -= 1
            nums[i - 1], nums[t] = nums[t], nums[i - 1]
            t = len(nums) - 1
            while i < t and i != t:
                nums[i], nums[t] = nums[t], nums[i]
                i += 1
                t -= 1
        if i_orig == 0:
            i, t = 0, len(nums) - 1
            while i < t and i != t:
                nums[i], nums[t] = nums[t], nums[i]
                i += 1
                t -= 1
        return nums

    def nextPermutation_1(self, nums: 'List[int]') -> 'List[int]':
        """
        Do not return anything, modify nums in-place instead.
        """
        i, t = len(nums) - 1, len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:
            i -= 1
        i_orig = i
        if i > 0:
            while nums[t] <= nums[i - 1]:
                t -= 1
            nums[i - 1], nums[t] = nums[t], nums[i - 1]
            tail = nums[i:]
            tail.reverse()
            nums[i:] = tail
        if i_orig == 0:
            nums.sort()
        return nums

if __name__ == "__main__":
    a = Solution()
    nums = [1, 3, 2]
    res = a.nextPermutation(nums)
    print(res)
    nums = [1, 3, 2]
    res = a.nextPermutation_1(nums)
    print(res)

