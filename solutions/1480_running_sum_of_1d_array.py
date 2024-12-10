"""1480. Running Sum of 1d Array

https://leetcode.com/problems/running-sum-of-1d-array/

>>> solution = Solution()
>>> solution.runningSum([1, 2, 3, 4])
[1, 3, 6, 10]
>>> solution.runningSum([1, 1, 1, 1, 1])
[1, 2, 3, 4, 5]
>>> solution.runningSum([3, 1, 2, 10, 1])
[3, 4, 6, 16, 17]
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums
