# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 20:52
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0144_preorderTraversal.py
# @Software: PyCharm

'''
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # recursively
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        """
        :type root: TreeNode
        :type res: List[int]
        :rtype: None
        """
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)

    # iteratively
    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

if __name__ == "__main__":
    '''
       1
        \
         2
        /
       3
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t2.left = t3
    root = t1
    print(a.preorderTraversal(root))
    print(a.preorderTraversal_1(root))

    '''
           1
          / \
         4   3
        /
       2
    '''
    a = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(4)
    t3 = TreeNode(3)
    t4 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    root = t1
    print(a.preorderTraversal(root))
    print(a.preorderTraversal_1(root))