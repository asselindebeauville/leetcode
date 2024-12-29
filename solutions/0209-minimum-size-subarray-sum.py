"""209. Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum/

>>> solution = Solution()
>>> solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
2
>>> solution.minSubArrayLen(4, [1, 4, 4])
1
>>> solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
0
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = curr_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_length if min_length != float("inf") else 0
