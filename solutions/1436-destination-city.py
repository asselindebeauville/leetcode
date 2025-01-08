"""1436. Destination City

https://leetcode.com/problems/destination-city/

>>> solution = Solution()
>>> solution.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
'Sao Paulo'
>>> solution.destCity([["B", "C"], ["D", "B"], ["C", "A"]])
'A'
>>> solution.destCity([["A", "Z"]])
'Z'
"""


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        departures = set(departure for departure, _ in paths)

        for _, destination in paths:
            if destination not in departures:
                return destination
