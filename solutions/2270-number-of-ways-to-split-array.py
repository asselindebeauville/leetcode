"""2270. Number of Ways to Split Array

https://leetcode.com/problems/number-of-ways-to-split-array/

>>> solution = Solution()
>>> solution.waysToSplitArray([10, 4, -8, 7])
2
>>> solution.waysToSplitArray([2, 3, 1, 0])
2
"""


class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left_sum = count = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total - left_sum
            if left_sum >= right_sum:
                count += 1

        return count
