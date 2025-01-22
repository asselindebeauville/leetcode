"""844. Backspace String Compare

https://leetcode.com/problems/backspace-string-compare/

>>> solution = Solution()
>>> solution.backspaceCompare("ab#c", "ad#c")
True
>>> solution.backspaceCompare("ab##", "c#d#")
True
>>> solution.backspaceCompare("a#c", "b")
False
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        return process(s) == process(t)
