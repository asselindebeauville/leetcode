"""2000. Reverse Prefix of Word

https://leetcode.com/problems/reverse-prefix-of-word/

>>> solution = Solution()
>>> solution.reversePrefix("abcdefd", "d")
'dcbaefd'
>>> solution.reversePrefix("xyxzxe", "z")
'zxyxxe'
>>> solution.reversePrefix("abcd", "z")
'abcd'
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        char_index = word.find(ch)

        if char_index == -1:
            return word

        return word[: char_index + 1][::-1] + word[char_index + 1 :]
