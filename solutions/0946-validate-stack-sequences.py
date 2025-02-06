"""946. Validate Stack Sequences

https://leetcode.com/problems/validate-stack-sequences/

>>> solution = Solution()
>>> solution.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
True
>>> solution.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
False
"""


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        pop_index = 0
        stack = []

        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

        return pop_index == len(popped)
