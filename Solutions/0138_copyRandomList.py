# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 9:56
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0138_copyRandomList.py
# @Software: PyCharm

'''
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.
Return a deep copy of the list.

Example 1:
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

Note:
You must return the copy of the given head as a reference to the cloned list.
'''

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        self.cloneNodes(head)
        self.cloneRandomNodes(head)
        return self.reconnectNodes(head)

    def cloneNodes(self, head: 'Node') -> 'Node':
        # 复制原始链表的每个节点，将复制的节点链接在其原始节点的后面
        pNode = head
        while pNode:
            pCloned = Node(0, None, None)
            pCloned.val = pNode.val
            pCloned.next = pNode.next

            pNode.next = pCloned
            pNode = pCloned.next

    def cloneRandomNodes(self, head: 'Node') -> 'Node':
        # 将复制后的链表中的克隆节点的random指针链接到被克隆节点random指针的后一个节点
        pNode = head
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    def reconnectNodes(self, head: 'Node') -> 'Node':
        # 拆分链表：将原始链表中的节点组成新的链表，复制节点组成复制后的链表
        pNode = head
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next
        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead

    def copyRandomList_1(self, head: 'Node') -> 'Node':
        if not head:
            return None

        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                old_to_new[cur].next = old_to_new[cur.next]
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]

if __name__ == "__main__":
    '''
           ———
          |   |
          V   |
     1 -> 2 -> 
     |____^

    '''
    p1 = Node(1, None, None)
    p2 = Node(2, None, None)
    p1.next = p2
    p1.random = p2
    p2.random = p2
    head = p1

    a = Solution()
    res = a.copyRandomList(head)
    print(res.val)
    res = a.copyRandomList_1(head)
    print(res.val)

    '''
             ——
            |  |
            V  |
            1-> 

    '''
    p1 = Node(-1, None, None)
    p1.random = p1
    head = p1

    a = Solution()
    res = a.copyRandomList(head)
    print(res.val)
    res = a.copyRandomList_1(head)
    print(res.val)