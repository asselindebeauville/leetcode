"""2342. Max Sum of a Pair With Equal Sum of Digits

https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

>>> solution = Solution()
>>> solution.maximumSum([18, 43, 36, 13, 7])
54
>>> solution.maximumSum([10, 12, 19, 14])
-1
"""

from collections import defaultdict


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        max_seen = defaultdict(int)
        max_sum = -1

        for num in nums:
            digit_sum = self.digitSum(num)
            if digit_sum in max_seen:
                max_sum = max(max_sum, num + max_seen[digit_sum])
            max_seen[digit_sum] = max(max_seen[digit_sum], num)

        return max_sum

    def digitSum(self, num: int) -> int:
        digit_sum = 0

        while num:
            digit_sum += num % 10
            num //= 10

        return digit_sum
