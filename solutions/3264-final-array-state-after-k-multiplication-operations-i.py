"""3264. Final Array State After K Multiplication Operations I

https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

>>> solution = Solution()
>>> solution.getFinalState([2, 1, 3, 5, 6], 5, 2)
[8, 4, 6, 5, 6]
>>> solution.getFinalState([1, 2], 3, 4)
[16, 8]
"""

import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        min_heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            value, index = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (value * multiplier, index))

        while min_heap:
            value, index = heapq.heappop(min_heap)
            nums[index] = value

        return nums
