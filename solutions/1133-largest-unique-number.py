"""1133. Largest Unique Number

https://leetcode.com/problems/largest-unique-number/

>>> solution = Solution()
>>> solution.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1])
8
>>> solution.largestUniqueNumber([9, 9, 8, 8])
-1
"""

from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        num_count = Counter(nums)

        return max(
            (num for num, count in num_count.items() if count == 1),
            default=-1,
        )
