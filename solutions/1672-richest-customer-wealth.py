"""1672. Richest Customer Wealth

https://leetcode.com/problems/richest-customer-wealth/

>>> solution = Solution()
>>> solution.maximumWealth([[1, 2, 3], [3, 2, 1]])
6
>>> solution.maximumWealth([[1, 5], [7, 3], [3, 5]])
10
>>> solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
17
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            max_wealth = max(max_wealth, sum(customer))

        return max_wealth
