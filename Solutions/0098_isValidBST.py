# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 14:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0098_isValidBST.py
# @Software: PyCharm

'''
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3
Input: [2,1,3]
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return self.isValidNode(root, float('-inf'), float('inf'))

    def isValidNode(self, root: 'TreeNode', l: 'float', r:'float') -> 'bool':
        if not root:
            return True
        return l < root.val < r and self.isValidNode(root.left, l, root.val) and self.isValidNode(root.right, root.val, r)

    def isValidBST_1(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        order = []
        self.inorderT(root, order)
        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True

    def inorderT(self, root: 'TreeNode', order: 'list[int]') -> 'None':
        if not root:
            return
        self.inorderT(root.left, order)
        order.append(root.val)
        self.inorderT(root.right, order)

    def isValidBST_2(self, root: TreeNode) -> bool:
        def valid_subtree(root, lo, hi):
            if not root: return True
            if root.val <= lo or root.val >= hi: return False
            return valid_subtree(root.left, lo, root.val) and valid_subtree(root.right, root.val, hi)

        return valid_subtree(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    '''
        2
       / \
      1   3
    '''
    t1 = TreeNode(2)
    t2 = TreeNode(1)
    t3 = TreeNode(3)

    t1.left = t2
    t1.right = t3
    root = t1

    a = Solution()
    print(a.isValidBST(root))
    print(a.isValidBST_1(root))
    '''
        5
       / \
      1   4
         / \
        3   6
    '''
    t11 = TreeNode(5)
    t12 = TreeNode(1)
    t13 = TreeNode(4)
    t14 = TreeNode(3)
    t15 = TreeNode(6)

    t11.left = t12
    t11.right = t13
    t13.left = t14
    t13.right = t15
    root = t11

    a = Solution()
    print(a.isValidBST(root))
    print(a.isValidBST_1(root))