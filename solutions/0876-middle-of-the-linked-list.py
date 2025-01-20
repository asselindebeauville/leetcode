"""876. Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

>>> solution = Solution()  # doctest: +SKIP
>>> solution.middleNode([1, 2, 3, 4, 5])  # doctest: +SKIP
[3, 4, 5]
>>> solution.middleNode([1, 2, 3, 4, 5, 6])  # doctest: +SKIP
[4, 5, 6]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
