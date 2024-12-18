"""1475. Final Prices With a Special Discount in a Shop

https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

>>> solution = Solution()
>>> solution.finalPrices([8, 4, 6, 2, 3])
[4, 2, 4, 2, 3]
>>> solution.finalPrices([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
>>> solution.finalPrices([10, 1, 1, 6])
[9, 0, 1, 6]
"""


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = prices.copy()
        stack = []

        for i, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                discount_idx = stack.pop()
                answer[discount_idx] -= price
            stack.append(i)

        return answer
