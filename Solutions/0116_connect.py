# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 22:30
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0116_connect.py
# @Software: PyCharm

'''
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example:
Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,
"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5",
"left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,
"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,
"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},
"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,
"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

Explanation: Given the above perfect binary tree (Figure A),
your function should populate each next pointer to point to its next right node, just like in Figure B.

Note:
You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
'''

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root
        self.connect(root.left)
        self.connect(root.right)
        p, q = root.left, root.right
        while p:
            p.next = q
            p = p.right
            q = q.left
        return cur

    def connect_1(self, root: 'Node') -> 'Node':
        cur = root

        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next

        return cur

if __name__ == "__main__":
    '''
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
    '''
    a = Solution()
    t1 = Node(1)
    t2 = Node(2)
    t3 = Node(3)
    t4 = Node(4)
    t5 = Node(5)
    t6 = Node(6)
    t7 = Node(7)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7

    root = t1
    print(a.connect(root))

    t1 = Node(1)
    t2 = Node(2)
    t3 = Node(3)
    t4 = Node(4)
    t5 = Node(5)
    t6 = Node(6)
    t7 = Node(7)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7

    root = t1
    print(a.connect_1(root))