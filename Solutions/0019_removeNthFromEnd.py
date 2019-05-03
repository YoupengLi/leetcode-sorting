# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 0010 18:40
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0019_removeNthFromEnd.py
# @Software: PyCharm

'''
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        if not head or n <= 0:
            return None
        if n == 1:
            pHead = head
            if not pHead.next:
                head = None
                return head
            while pHead.next:
                p1 = pHead
                pHead = pHead.next
            p1.next = None
            return head
        else:
            pAhead = head
            for i in range(n - 1):
                if pAhead.next:
                    pAhead = pAhead.next
                else:
                    return None
            if not pAhead.next:
                head = head.next
                return head
            pBehind = head
            while pAhead.next:
                p1 = pBehind
                pAhead = pAhead.next
                pBehind = pBehind.next
            p1.next = pBehind.next
            return head

    def removeNthFromEnd_1(self, head: 'ListNode', n: 'int') -> 'ListNode':
        fast = slow = head
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head

        counter = 1
        while counter != n + 1:
            fast = fast.next
            counter += 1

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next
        return dummy.next

    def removeNthFromEnd_2(self, head: 'ListNode', n: 'int') -> 'ListNode':
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        fast = slow = start
        count = 0
        while fast.next:
            fast = fast.next
            if count >= n:
                slow = slow.next
            count += 1
        slow.next = slow.next.next
        return start.next

if __name__ == "__main__":
    '''
    A -> B -> C -> D -> E -> F -> G -> H
    '''
    t1 = ListNode('A')
    t2 = ListNode('B')
    t3 = ListNode('C')
    t4 = ListNode('D')
    t5 = ListNode('E')
    t6 = ListNode('F')
    t7 = ListNode('G')
    t8 = ListNode('H')

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6
    t6.next = t7
    t7.next = t8

    head = t1

    a = Solution()
    print(a.removeNthFromEnd(head, 8))
    print(a.removeNthFromEnd_1(head, 7))
    print(a.removeNthFromEnd_2(head, 6))