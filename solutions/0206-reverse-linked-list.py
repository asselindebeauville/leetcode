"""206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

>>> solution = Solution()  # doctest: +SKIP
>>> solution.reverseList([1, 2, 3, 4, 5])  # doctest: +SKIP
[5, 4, 3, 2, 1]
>>> solution.reverseList([1, 2])  # doctest: +SKIP
[2, 1]
>>> solution.reverseList([])  # doctest: +SKIP
[]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
