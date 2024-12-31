"""1248. Count Number of Nice Subarrays

https://leetcode.com/problems/count-number-of-nice-subarrays/

>>> solution = Solution()
>>> solution.numberOfSubarrays([1, 1, 2, 1, 1], 3)
2
>>> solution.numberOfSubarrays([2, 4, 6], 1)
0
>>> solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)
16
"""

from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix_odd_count = defaultdict(int)
        prefix_odd_count[0] = 1
        count = odd_count = 0

        for num in nums:
            odd_count += num % 2
            count += prefix_odd_count[odd_count - k]
            prefix_odd_count[odd_count] += 1

        return count
