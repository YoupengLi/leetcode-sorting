# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 0015 07:49
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0024_swapPairs.py
# @Software: PyCharm

'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None
        if head.next == None:
            return head
        pNode = ListNode(0)
        pNode.next = head
        p1 = pNode
        while True:
            if p1.next and p1.next.next:
                p2 = p1.next
                p1.next = p1.next.next
                p2.next = p2.next.next
                p1 = p1.next
                p1.next = p2
                p1 = p1.next
            else:
                break
        return pNode.next

    def swapPairs_1(self, head: 'ListNode') -> 'ListNode':
        if head and head.next:
            temp = head.val
            head.val = head.next.val
            head.next.val = temp
            self.swapPairs_1(head.next.next)
        return head

    def swapPairs_2(self, head: 'ListNode') -> 'ListNode':
        pNode = ListNode(0)
        pNode.next = head
        p1 = pNode
        while True:
            if p1.next and p1.next.next:
                val = p1.next.val
                p1.next.val = p1.next.next.val
                p1.next.next.val = val
                p1 = p1.next.next
            else:
                break
        return pNode.next

    def swapPairs_3(self, head: 'ListNode') -> 'ListNode':
        pNode = ListNode(0)
        pNode.next = head
        p1 = pNode
        while p1.next and p1.next.next:
            val = p1.next.val
            p1.next.val = p1.next.next.val
            p1.next.next.val = val
            p1 = p1.next.next
        return pNode.next

if __name__ == "__main__":
    '''
    list: 1 -> 2 -> 3 -> 4
    '''
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(4)
    t1.next = t2
    t2.next = t3
    t3.next = t4

    head = t1

    a = Solution()
    head = a.swapPairs(head)
    print(head)
    head = a.swapPairs_1(head)
    print(head)
    head = a.swapPairs_2(head)
    print(head)
    head = a.swapPairs_3(head)
    print(head)

