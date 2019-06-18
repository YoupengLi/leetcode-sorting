# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 21:53
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0095_generateTrees.py
# @Software: PyCharm

'''
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if n == 0:
            return []
        return self.dfs(1, n + 1)

    def dfs(self, start: 'int', end: 'int') -> 'List[TreeNode]':
        if start == end:
            return None
        res = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    res.append(node)
        return res

    def generateTrees_1(self, n: 'int') -> 'List[TreeNode]':
        dp = {}

        def helper(left: int, right: int) -> list:
            if (left, right) in dp:
                return dp[(left, right)]
            if left > right:
                return [None]
            ret = []
            for num in range(left, right + 1):
                left_subtrees = helper(left, num - 1)
                right_subtrees = helper(num + 1, right)
                for l_tree in left_subtrees:
                    for r_tree in right_subtrees:
                        to_add = TreeNode(num)
                        to_add.left = l_tree
                        to_add.right = r_tree
                        ret.append(to_add)
            dp[(left, right)] = ret
            return ret

        if n < 1:
            return []
        return helper(1, n)

if __name__ == "__main__":
    a = Solution()
    n = 3
    print(a.generateTrees(n))
    print(a.generateTrees_1(n))