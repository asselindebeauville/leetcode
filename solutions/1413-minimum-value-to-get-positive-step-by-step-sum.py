"""1413. Minimum Value to Get Positive Step by Step Sum

https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

>>> solution = Solution()
>>> solution.minStartValue([-3, 2, -3, 4, 2])
5
>>> solution.minStartValue([1, 2])
1
>>> solution.minStartValue([1, -2, -3])
5
"""


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        curr_sum = 0
        min_sum = float("inf")

        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)

        return max(1, -min_sum + 1)
