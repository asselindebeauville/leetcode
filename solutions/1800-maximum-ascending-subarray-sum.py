"""1800. Maximum Ascending Subarray Sum

https://leetcode.com/problems/maximum-ascending-subarray-sum/

>>> solution = Solution()
>>> solution.maxAscendingSum([10, 20, 30, 5, 10, 50])
65
>>> solution.maxAscendingSum([10, 20, 30, 40, 50])
150
>>> solution.maxAscendingSum([12, 17, 15, 13, 10, 11, 12])
33
"""


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        prev_num = curr_sum = max_sum = 0

        for num in nums:
            if num > prev_num:
                curr_sum += num
            else:
                curr_sum = num

            max_sum = max(max_sum, curr_sum)
            prev_num = num

        return max_sum
