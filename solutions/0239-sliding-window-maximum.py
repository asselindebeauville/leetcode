"""239. Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum/

>>> solution = Solution()
>>> solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
[3, 3, 5, 5, 6, 7]
>>> solution.maxSlidingWindow([1], 1)
[1]
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        max_deque = deque()

        for i in range(k):
            while max_deque and nums[max_deque[-1]] < nums[i]:
                max_deque.pop()
            max_deque.append(i)

        result.append(nums[max_deque[0]])

        for i in range(k, len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[i]:
                max_deque.pop()
            max_deque.append(i)

            if max_deque[0] <= i - k:
                max_deque.popleft()

            result.append(nums[max_deque[0]])

        return result
