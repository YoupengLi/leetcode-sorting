# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:26
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0104_maxDepth.py
# @Software: PyCharm

'''
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth_1(self, root: 'TreeNode') -> 'int':
        depth = 0
        queue = [root] if root else []
        while queue:
            depth += 1
            res = []
            for node in queue:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            queue = res
        return depth

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

    print(a.maxDepth(root))
    print(a.maxDepth_1(root))