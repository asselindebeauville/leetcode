"""1944. Number of Visible People in a Queue

https://leetcode.com/problems/number-of-visible-people-in-a-queue/

>>> solution = Solution()
>>> solution.canSeePersonsCount([10, 6, 8, 5, 11, 9])
[3, 1, 2, 1, 1, 0]
>>> solution.canSeePersonsCount([5, 1, 2, 3, 10])
[4, 1, 1, 1, 0]
"""


class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in reversed(range(n)):
            count = 0

            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1

            if stack:
                count += 1

            answer[i] = count
            stack.append(heights[i])

        return answer
