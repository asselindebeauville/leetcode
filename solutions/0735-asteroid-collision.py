"""735. Asteroid Collision

https://leetcode.com/problems/asteroid-collision/

>>> solution = Solution()
>>> solution.asteroidCollision([5, 10, -5])
[5, 10]
>>> solution.asteroidCollision([8, -8])
[]
>>> solution.asteroidCollision([10, 2, -5])
[10]
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 > asteroid:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack
