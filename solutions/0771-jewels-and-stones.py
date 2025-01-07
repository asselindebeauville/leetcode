"""771. Jewels and Stones

https://leetcode.com/problems/jewels-and-stones/

>>> solution = Solution()
>>> solution.numJewelsInStones("aA", "aAAbbbb")
3
>>> solution.numJewelsInStones("z", "ZZ")
0
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        return sum(stone in jewels_set for stone in stones)
