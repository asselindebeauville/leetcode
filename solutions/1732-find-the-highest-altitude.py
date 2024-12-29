"""1732. Find the Highest Altitude

https://leetcode.com/problems/find-the-highest-altitude/

>>> solution = Solution()
>>> solution.largestAltitude([-5, 1, 5, 0, -7])
1
>>> solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2])
0
"""


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr_altitude = max_altitude = 0

        for diff in gain:
            curr_altitude += diff
            max_altitude = max(max_altitude, curr_altitude)

        return max_altitude
