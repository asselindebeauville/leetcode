"""1290. Convert Binary Number in a Linked List to Integer

https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

>>> solution = Solution()
>>> # head = [1, 0, 1]
>>> solution.getDecimalValue(ListNode(1, ListNode(0, ListNode(1))))
5
>>> # head = [0]
>>> solution.getDecimalValue(ListNode(0))
0
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        num = 0

        while current:
            num = (num << 1) | current.val
            current = current.next

        return num
