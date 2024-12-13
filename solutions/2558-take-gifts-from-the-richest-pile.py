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
        heap = [-num for num in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            max_num = -heapq.heappop(heap)
            remaining = math.isqrt(max_num)
            heapq.heappush(heap, -remaining)

        return -sum(heap)
