"""739. Daily Temperatures

https://leetcode.com/problems/daily-temperatures/

>>> solution = Solution()
>>> solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
[1, 1, 4, 2, 1, 1, 0, 0]
>>> solution.dailyTemperatures([30, 40, 50, 60])
[1, 1, 1, 0]
>>> solution.dailyTemperatures([30, 60, 90])
[1, 1, 0]
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return answer
