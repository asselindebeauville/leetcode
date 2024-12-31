"""560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/

>>> solution = Solution()
>>> solution.subarraySum([1, 1, 1], 2)
2
>>> solution.subarraySum([1,2,3], 3)
2
"""

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        count = curr_sum = 0

        for num in nums:
            curr_sum += num
            count += prefix_sum_count[curr_sum - k]
            prefix_sum_count[curr_sum] += 1

        return count
