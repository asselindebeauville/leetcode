"""1004. Max Consecutive Ones III

https://leetcode.com/problems/max-consecutive-ones-iii/

>>> solution = Solution()
>>> solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
6
>>> solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
10
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = zero_count = max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
