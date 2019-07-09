# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 9:04
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0117_connect.py
# @Software: PyCharm

'''
117. Populating Next Right Pointers in Each Node II

Given a binary tree

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
"left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,
"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},
"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},
"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to
point to its next right node, just like in Figure B.

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
        head = tail = Node(0)
        cur = root
        while root:
            for c in (root.left, root.right):
                tail.next = c
                if c:
                    tail = tail.next
            if root.next:
                root = root.next
            else:
                root, tail = head.next, head
        return cur

if __name__ == "__main__":
    '''
          1
        /   \
       2     3
      / \     \
     4   5     7
    '''
    a = Solution()
    t1 = Node(1)
    t2 = Node(2)
    t3 = Node(3)
    t4 = Node(4)
    t5 = Node(5)
    t6 = Node(7)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6

    root = t1
    print(a.connect(root))