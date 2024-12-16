"""2558. Take Gifts From the Richest Pile

https://leetcode.com/problems/take-gifts-from-the-richest-pile/

>>> solution = Solution()
>>> solution.pickGifts([25, 64, 9, 4, 100], 4)
29
>>> solution.pickGifts([1, 1, 1, 1], 4)
4
"""

import heapq
import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        max_heap = [-num for num in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            max_num = -heapq.heappop(max_heap)
            remaining = math.isqrt(max_num)
            heapq.heappush(max_heap, -remaining)

        return -sum(max_heap)
