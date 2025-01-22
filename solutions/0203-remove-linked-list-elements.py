"""203. Remove Linked List Elements

https://leetcode.com/problems/remove-linked-list-elements/

>>> solution = Solution()  # doctest: +SKIP
>>> solution.removeElements([1, 2, 6, 3, 4, 5, 6], 6)  # doctest: +SKIP
[1, 2, 3, 4, 5]
>>> solution.removeElements([], 1)  # doctest: +SKIP
[]
>>> solution.removeElements([7, 7, 7, 7], 7)  # doctest: +SKIP
[]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = dummy = ListNode(0, head)

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next
