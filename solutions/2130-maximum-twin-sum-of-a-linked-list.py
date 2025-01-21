"""2130. Maximum Twin Sum of a Linked List

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

>>> solution = Solution()
>>> # head = [5, 4, 2, 1]
>>> head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
>>> solution.pairSum(head)
6
>>> # head = [4, 2, 2, 3]
>>> head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
>>> solution.pairSum(head)
7
>>> # head = [1, 100000]
>>> head = ListNode(1, ListNode(100000))
>>> solution.pairSum(head)
100001
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow = fast = head
        max_sum = 0

        while fast and fast.next:
            fast = fast.next.next

            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            max_sum = max(max_sum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return max_sum
