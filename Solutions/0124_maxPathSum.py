# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 8:54
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0124_maxPathSum.py
# @Software: PyCharm

'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node
n the tree along the parent-child connections. The path must contain at least one node
and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42
'''

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
            # Recursively
            self.res = -sys.maxsize - 1
            self.oneSideSum(root)
            return self.res

    def oneSideSum(self, root: 'TreeNode') -> 'int':
        # compute one side maximal sum,
        # (root+left children, or root+right children),
        # root is the included top-most node
        if not root:
            return 0
        l = max(0, self.oneSideSum(root.left))
        r = max(0, self.oneSideSum(root.right))
        self.res = max(self.res, l + r + root.val)
        return max(l, r) + root.val

if __name__ == "__main__":
    '''
          1
         / \
        2   3
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)

    t1.left = t2
    t1.right = t3
    root = t1
    print(a.maxPathSum(root))