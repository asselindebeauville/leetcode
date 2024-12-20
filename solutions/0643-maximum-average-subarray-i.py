"""643. Maximum Average Subarray I

https://leetcode.com/problems/maximum-average-subarray-i/

>>> solution = Solution()
>>> solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
12.75
>>> solution.findMaxAverage([5], 1)
5.0
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k
