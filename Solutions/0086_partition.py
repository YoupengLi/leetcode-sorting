# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 17:46
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0086_partition.py
# @Software: PyCharm

'''
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes
greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        if not head:
            return None
        small_head = None
        large_head = None
        p1 = None
        p2 = None
        cur = head
        while cur:
            if cur.val < x:
                if not small_head:
                    small_head = cur
                    p1 = small_head
                else:
                    p1.next = cur
                    p1 = p1.next
            else:
                if not large_head:
                    large_head = cur
                    p2 = large_head
                else:
                    p2.next = cur
                    p2 = p2.next
            cur = cur.next
        if p2:
            p2.next = None
        if small_head and large_head:
            p1.next = large_head
            return small_head
        else:
            return head

    def partition_1(self, head: 'ListNode', x: 'int') -> 'ListNode':
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

if __name__ == "__main__":
    '''
    list1: 1->4->3->2->5->2
    '''
    a = Solution()
    t1 = ListNode(1)
    t2 = ListNode(4)
    t3 = ListNode(3)
    t4 = ListNode(2)
    t5 = ListNode(5)
    t6 = ListNode(2)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6

    head = t1

    head = a.partition(head, 3)
    print(head)

    t1 = ListNode(1)
    t2 = ListNode(1)

    t1.next = t2
    head = t1

    head = a.partition(head, 2)
    print(head)

    t1 = ListNode(1)
    t2 = ListNode(4)
    t3 = ListNode(3)
    t4 = ListNode(2)
    t5 = ListNode(5)
    t6 = ListNode(2)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6

    head = t1

    head = a.partition_1(head, 3)
    print(head)