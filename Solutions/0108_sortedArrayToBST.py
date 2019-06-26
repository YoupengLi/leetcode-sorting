# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 10:12
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0108_sortedArrayToBST.py
# @Software: PyCharm

'''
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None
        mid = (len(nums)-1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__ == "__main__":
    a = Solution()
    nums = [-10, -3, 0, 5, 9]
    res = a.sortedArrayToBST(nums)
    nums = [0, 1]
    res = a.sortedArrayToBST(nums)
    print(res)