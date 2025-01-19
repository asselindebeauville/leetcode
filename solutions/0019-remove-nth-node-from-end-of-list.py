"""19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

>>> solution = Solution()
>>> solution.removeNthFromEnd([1, 2, 3, 4, 5], 2)  # doctest: +SKIP
[1, 2, 3, 5]
>>> solution.removeNthFromEnd([1], 1)  # doctest: +SKIP
[]
>>> solution.removeNthFromEnd([1, 2], 1)  # doctest: +SKIP
[1]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
