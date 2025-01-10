"""1695. Maximum Erasure Value

https://leetcode.com/problems/maximum-erasure-value/

>>> solution = Solution()
>>> solution.maximumUniqueSubarray([4, 2, 4, 5, 6])
17
>>> solution.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5])
8
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = curr_sum = max_score = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]
            max_score = max(max_score, curr_sum)

        return max_score
