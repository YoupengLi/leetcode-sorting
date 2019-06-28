# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 11:40
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0112_hasPathSum.py
# @Software: PyCharm

'''
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        # DFS Recursively
        res = []
        self.dfs(root, sum, res)
        return any(res)

    def dfs(self, root: 'TreeNode', target: 'int', res: 'List[int]'):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
            if root.left:
                self.dfs(root.left, target - root.val, res)
            if root.right:
                self.dfs(root.right, target - root.val, res)

    def hasPathSum_1(self, root: 'TreeNode', sum: 'int') -> 'bool':
        # DFS with stack
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            cur, val = stack.pop()
            if not cur.left and not cur.right:
                if val == sum:
                    return True
            if cur.left:
                stack.append((cur.left, val + cur.left.val))
            if cur.right:
                stack.append((cur.right, val + cur.right.val))
        return False

    def hasPathSum_2(self, root: 'TreeNode', sum: 'int') -> 'bool':
        # BFS with queue
        if not root:
            return False
        queue = [(root, sum - root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left, val - curr.left.val))
            if curr.right:
                queue.append((curr.right, val - curr.right.val))
        return False

    def hasPathSum_3(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

if __name__ == "__main__":
    '''
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
    '''
    a = Solution()
    t1 = TreeNode(5)
    t2 = TreeNode(4)
    t3 = TreeNode(8)
    t4 = TreeNode(11)
    t5 = TreeNode(13)
    t6 = TreeNode(4)
    t7 = TreeNode(7)
    t8 = TreeNode(2)
    t9 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.left = t5
    t3.right = t6
    t4.left = t7
    t4.right = t8
    t6.right = t9

    root = t1
    sum = 22
    print(a.hasPathSum(root, sum))
    print(a.hasPathSum_1(root, sum))
    print(a.hasPathSum_2(root, sum))
    print(a.hasPathSum_3(root, sum))