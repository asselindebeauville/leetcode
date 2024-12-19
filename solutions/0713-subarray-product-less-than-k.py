"""713. Subarray Product Less Than K

https://leetcode.com/problems/subarray-product-less-than-k/

>>> solution = Solution()
>>> solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
8
>>> solution.numSubarrayProductLessThanK([1, 2, 3], 0)
0
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        left = count = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1

        return count
