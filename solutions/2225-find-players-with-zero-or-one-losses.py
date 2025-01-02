"""2225. Find Players With Zero or One Losses

https://leetcode.com/problems/find-players-with-zero-or-one-losses/

>>> solution = Solution()
>>> solution.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10 ,4], [10, 9]])
[[1, 2, 10], [4, 5, 7, 8]]
>>> solution.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]])
[[1, 2, 5, 6], []]
"""


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loss_count = {}
        no_losses, one_loss = [], []

        for winner, loser in matches:
            loss_count[winner] = loss_count.get(winner, 0)
            loss_count[loser] = loss_count.get(loser, 0) + 1

        for player, losses in loss_count.items():
            if losses == 0:
                no_losses.append(player)
            elif losses == 1:
                one_loss.append(player)

        return [sorted(no_losses), sorted(one_loss)]
