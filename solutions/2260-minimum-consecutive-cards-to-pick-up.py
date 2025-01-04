"""2260. Minimum Consecutive Cards to Pick Up

https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

>>> solution = Solution()
>>> solution.minimumCardPickup([3, 4, 2, 3, 4, 7])
4
>>> solution.minimumCardPickup([1, 0, 5, 3])
-1
"""


class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        last_seen = {}
        min_length = float("inf")

        for i, card in enumerate(cards):
            if card in last_seen:
                min_length = min(min_length, i - last_seen[card] + 1)
            last_seen[card] = i

        return min_length if min_length != float("inf") else -1
