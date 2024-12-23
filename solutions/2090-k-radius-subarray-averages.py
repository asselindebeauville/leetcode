"""2090. K Radius Subarray Averages

https://leetcode.com/problems/k-radius-subarray-averages/

>>> solution = Solution()
>>> solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3)
[-1, -1, -1, 5, 4, 4, -1, -1, -1]
>>> solution.getAverages([100000], 0)
[100000]
>>> solution.getAverages([8], 100000)
[-1]
"""


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums

        n = len(nums)
        window_size = 2 * k + 1
        avgs = [-1] * n

        if window_size > n:
            return avgs

        window_sum = sum(nums[:window_size])
        avgs[k] = window_sum // window_size

        for i in range(k + 1, n - k):
            window_sum += nums[i + k] - nums[i - k - 1]
            avgs[i] = window_sum // window_size

        return avgs
