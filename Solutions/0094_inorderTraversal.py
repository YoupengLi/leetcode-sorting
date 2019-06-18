# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 19:39
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0094_inorderTraversal.py
# @Software: PyCharm

'''
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def inorderTraversal_1(self, root: 'TreeNode') -> 'List[int]':
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def inorderTraversal_2(self, root: 'TreeNode') -> 'List[int]':
        self.res = []

        def dfs(root: 'TreeNode') -> 'List[int]':
            if root is None:
                return
            if root.left:
                dfs(root.left)
            self.res.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)
        return self.res

if __name__ == "__main__":
    '''
       1
        \
         2
        /
       3
    '''
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)

    t1.right = t2
    t2.left = t3
    root = t1

    a = Solution()
    print(a.inorderTraversal(root))
    print(a.inorderTraversal_1(root))
    print(a.inorderTraversal_2(root))