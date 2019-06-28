# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 15:48
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0113_pathSum.py
# @Software: PyCharm

'''
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths
where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        # DFS Recursively
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root: 'TreeNode', sum: 'int', ls: 'List[int]', res: 'List[List[int]]'):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls + [root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls + [root.val], res)

    def pathSum_1(self, root: 'TreeNode', sum: 'int') -> 'bool':
        # DFS with stack
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            cur, val, ls = stack.pop()
            if not cur.left and not cur.right and val == 0:
                res.append(ls)
            if cur.left:
                stack.append((cur.left, val - cur.left.val, ls + [cur.left.val]))
            if cur.right:
                stack.append((cur.right, val - cur.right.val, ls + [cur.right.val]))
        return res

    def pathSum_2(self, root: 'TreeNode', sum: 'int') -> 'bool':
        # BFS + queue
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            cur, val, ls = queue.pop(0)
            if not cur.left and not cur.right and val == sum:
                res.append(ls)
            if cur.left:
                queue.append((cur.left, val + cur.left.val, ls + [cur.left.val]))
            if cur.right:
                queue.append((cur.right, val + cur.right.val, ls + [cur.right.val]))
        return res

    def pathSum_3(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        def dfs(root: 'TreeNode', tmp: 'List[int]', sum: 'int', res: 'List[List[int]]'):
            if not root:
                return
            if not root.left and not root.right and root.val == sum:
                res.append(tmp + [root.val])
            tmp.append(root.val)
            dfs(root.left, tmp, sum - root.val, res)
            dfs(root.right, tmp, sum - root.val, res)
            tmp.pop()

        res = []
        dfs(root, [], sum, res)
        return res

if __name__ == "__main__":
    '''
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
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
    t9 = TreeNode(5)
    t10 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.left = t5
    t3.right = t6
    t4.left = t7
    t4.right = t8
    t6.left = t9
    t6.right = t10

    root = t1
    sum = 22
    print(a.pathSum(root, sum))
    print(a.pathSum_1(root, sum))
    print(a.pathSum_2(root, sum))
    print(a.pathSum_3(root, sum))