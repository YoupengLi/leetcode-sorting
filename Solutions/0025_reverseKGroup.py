# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 0016 20:59
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0025_reverseKGroup.py
# @Software: PyCharm

'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: 'ListNode', k: int) -> 'ListNode':
        l1 = head
        temp = []
        for i in range(k):
            if l1:
                temp.append(l1.val)
                l1 = l1.next
            else:
                break
        if len(temp) < k:
            return head
        else:
            new_head = ListNode(temp.pop())
            l2 = new_head
            while temp:
                l2.next = ListNode(temp.pop())
                l2 = l2.next
        while l1:
            if len(temp) != k:
                temp.append(l1.val)
                l1 = l1.next
            else:
                while temp:
                    l2.next = ListNode(temp.pop())
                    l2 = l2.next
        if temp:
            if len(temp) < k:
                for i in range(len(temp)):
                    l2.next = ListNode(temp[i])
                    l2 = l2.next
            else:
                while temp:
                    l2.next = ListNode(temp.pop())
                    l2 = l2.next

        return new_head

    def reverseKGroup_1(self, head: 'ListNode', k: int) -> 'ListNode':
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        stack = []
        while cur:
            for _ in range(k):
                if not cur:
                    return dummy.next
                stack.append(cur)
                cur = cur.next
            if len(stack) < k:
                return dummy.next
            else:
                next_node = stack[-1].next
                for _ in range(k):
                    node = stack.pop()
                    pre.next = node
                    pre = pre.next
                pre.next = next_node
            cur = next_node
        return dummy.next

    def reverseKGroup_2(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if k == 1:
            return head

        dummy = prev = ListNode(0)
        prev.next = node = head

        while node:
            curr_head = node
            size = 0
            while node and size < k:
                size += 1
                node = node.next
            if size < k:
                prev.next = curr_head
                break

            prev.next = self.reverseLinkedList(curr_head, k)
            prev = curr_head

        return dummy.next

    def reverseLinkedList(self, head: 'ListNode', size: 'int') -> 'ListNode':
        if not head:
            return None

        prev = None
        node = head
        cntr = 0

        while node and cntr < size:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            cntr += 1

        return prev

if __name__ == "__main__":
    '''
    list1: 1 -> 2 -> 3 -> 4 -> 5  
    '''
    a = Solution()
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(3)
    t4 = ListNode(4)
    t5 = ListNode(5)

    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5

    head = t1

    head = a.reverseKGroup(head, 2)
    print(head)
    head = a.reverseKGroup_1(head, 2)
    print(head)
    head = a.reverseKGroup_2(head, 2)
    print(head)