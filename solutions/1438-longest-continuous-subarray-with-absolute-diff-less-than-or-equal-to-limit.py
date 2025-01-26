"""1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

>>> solution = Solution()
>>> solution.longestSubarray([8, 2, 4, 7], 4)
2
>>> solution.longestSubarray([10, 1, 2, 4, 7, 2], 5)
4
>>> solution.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0)
3
"""

from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = max_length = 0

        for right in range(len(nums)):
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
