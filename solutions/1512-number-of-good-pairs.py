"""1512. Number of Good Pairs

https://leetcode.com/problems/number-of-good-pairs/

>>> solution = Solution()
>>> solution.numIdenticalPairs([1, 2, 3, 1, 1, 3])
4
>>> solution.numIdenticalPairs([1, 1, 1, 1])
6
>>> solution.numIdenticalPairs([1, 2, 3])
0
"""

from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        good_pairs = 0

        for num in nums:
            good_pairs += counts[num]
            counts[num] += 1

        return good_pairs
