# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 10:04
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0110_isBalanced.py
# @Software: PyCharm

'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        # Time Limit Exceeded
        if not root:
            return True
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(left-right) <= 1:
            return True
        else:
            return False

    def getDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def isBalanced_1(self, root: 'TreeNode') -> 'bool':
        def check(root: 'TreeNode') -> 'int':
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return check(root) != -1

    def isBalanced_2(self, root: 'TreeNode') -> 'bool':
        def check(root: 'TreeNode'):
            if not root:
                return True, 0

            l_flag, l_depth = check(root.left)
            r_flag, r_depth = check(root.right)

            return l_flag and r_flag and abs(l_depth - r_depth) <= 1, max(l_depth, r_depth) + 1

        flag, height = check(root)
        return flag


if __name__ == "__main__":
    '''
            3
           / \
          9  20
            /  \
           15   7
    '''
    a = Solution()
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5

    root = t1
    print(a.isBalanced(root))
    print(a.isBalanced_1(root))
    print(a.isBalanced_2(root))
    '''
               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        '''
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(3)
    t6 = TreeNode(4)
    t7 = TreeNode(4)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t4.left = t6
    t4.right = t7

    root = t1
    print(a.isBalanced(root))
    print(a.isBalanced_1(root))
    print(a.isBalanced_2(root))
    '''
               1
              / \
             2   2
            /     \
           3       3
          /         \
         4           4
    '''
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(3)
    t6 = TreeNode(4)
    t7 = TreeNode(4)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5
    t4.left = t6
    t5.right = t7

    root = t1
    print(a.isBalanced(root))
    print(a.isBalanced_1(root))
    print(a.isBalanced_2(root))