"""1496. Path Crossing

https://leetcode.com/problems/path-crossing/

>>> solution = Solution()
>>> solution.isPathCrossing("NES")
False
>>> solution.isPathCrossing("NESWW")
True
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = (0, 0)
        visited = {(x, y)}
        moves = {
            "N": (0, +1),
            "S": (0, -1),
            "E": (+1, 0),
            "W": (-1, 0),
        }

        for direction in path:
            dx, dy = moves[direction]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False
