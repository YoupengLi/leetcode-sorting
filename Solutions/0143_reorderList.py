# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 18:09
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0143_reorderList.py
# @Software: PyCharm

'''
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        head2 = self.findMid(head)
        head2 = self.reverseList(head2)
        self.zigZagMerge(head, head2)

    def findMid(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # step1: separate list to two parts
        # ex: "1-2-3-4-5" ==> return head2 would be 4
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        head2, slow.next = slow.next, None
        return head2

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # step2: reverse the second half part
        # ex: following step1, second list "4-5" would become "5-4"
        pre, cur = head, head.next
        while cur:
            tmp, cur.next = cur.next, pre
            pre, cur = cur, tmp
        head.next = None
        return pre

    def zigZagMerge(self, head, head2):
        """
        :type head: ListNode
        :type head2: ListNode
        :rtype: None
        """
        # step3: merging
        # l1 = "1 2 3"
        # l2 =  "5 4"
        # connect these two are like drawing a zig zag
        cur1, cur2 = head, head2
        while cur2:
            tmp1, tmp2 = cur1.next, cur2.next
            cur1.next, cur2.next = cur2, tmp1
            cur1, cur2 = tmp1, tmp2

if __name__ == "__main__":
    a = Solution()

    '''
     1 -> 2 -> 3 -> 4

    '''
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    head = l1
    print(a.reorderList(head))

    '''
     1 -> 2 -> 3 -> 4 -> 5

    '''
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    head = l1
    print(a.reorderList(head))
    print(a.reorderList(head))