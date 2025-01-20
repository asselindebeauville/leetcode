"""24. Swap Nodes in Pairs

https://leetcode.com/problems/swap-nodes-in-pairs/

>>> solution = Solution()  # doctest: +SKIP
>>> solution.swapPairs([1, 2, 3, 4])  # doctest: +SKIP
[2, 1, 4, 3]
>>> solution.swapPairs([])  # doctest: +SKIP
[]
>>> solution.swapPairs([1])  # doctest: +SKIP
[1]
>>> solution.swapPairs([1, 2, 3])  # doctest: +SKIP
[2, 1, 3]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        current = head

        while current and current.next:
            first = current
            second = current.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            current = first.next

        return dummy.next
