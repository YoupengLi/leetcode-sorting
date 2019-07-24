# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 15:15
# @Author  : Youpeng Li
# @Site    : 
# @File    : 0141_hasCycle.py
# @Software: PyCharm

'''
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
           ——————————
          |          |
          V          |
     3 -> 2 -> 0 -> -4
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
      ————
     |    |
     V    |
     1 -> 2
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    1
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == float('-inf'):
                return True
            head.val = float('-inf')
            head = head.next
        return False

    def hasCycle_1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        pointer1 = head
        pointer2 = head.next

        while pointer1 != pointer2:
            if pointer2 is None or pointer2.next is None:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

        return True

    def hasCycle_2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dict = {}
        cur = head
        while cur:
            if cur in dict:
                return True
            dict[cur] = cur
            cur = cur.next
        return False

    def hasCycle_3(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

if __name__ == "__main__":
    a = Solution()

    '''
           ——————————
          |          |
          V          |
     3 -> 2 -> 0 -> -4

    '''
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2
    head = l1
    print(a.hasCycle_1(head))
    print(a.hasCycle_2(head))
    print(a.hasCycle_3(head))
    print(a.hasCycle(head))

    '''
      ————
     |    |
     V    |
     1 -> 2

    '''
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l2.next = l1
    head = l1
    print(a.hasCycle_1(head))
    print(a.hasCycle_2(head))
    print(a.hasCycle_3(head))
    print(a.hasCycle(head))

    '''
    1

    '''
    l1 = ListNode(1)
    head = l1
    print(a.hasCycle_1(head))
    print(a.hasCycle_2(head))
    print(a.hasCycle_3(head))
    print(a.hasCycle(head))