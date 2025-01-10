"""2958. Length of Longest Subarray With at Most K Frequency

https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

>>> solution = Solution()
>>> solution.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2)
6
>>> solution.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1)
2
>>> solution.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4)
4
"""

from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        left = max_length = 0

        for right in range(len(nums)):
            counts[nums[right]] += 1

            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
