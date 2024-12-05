"""1. Two Sum

https://leetcode.com/problems/two-sum/

>>> solution = Solution()
>>> solution.twoSum([2, 7, 11, 15], 9)
[0, 1]
>>> solution.twoSum([3, 2, 4], 6)
[1, 2]
>>> solution.twoSum([3, 3], 6)
[0, 1]
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []
