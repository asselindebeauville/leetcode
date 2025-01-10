"""930. Binary Subarrays With Sum

https://leetcode.com/problems/binary-subarrays-with-sum/

>>> solution = Solution()
>>> solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2)
4
>>> solution.numSubarraysWithSum([0, 0, 0, 0, 0], 0)
15
"""


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        left = curr_sum = count = prefix_zeros = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while left < right and (nums[left] == 0 or curr_sum > goal):
                if nums[left] == 0:
                    prefix_zeros += 1
                else:
                    prefix_zeros = 0

                curr_sum -= nums[left]
                left += 1

            if curr_sum == goal:
                count += 1 + prefix_zeros

        return count
