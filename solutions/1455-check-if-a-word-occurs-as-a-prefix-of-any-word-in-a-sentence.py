"""1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

>>> solution = Solution()
>>> solution.isPrefixOfWord("i love eating burger", "burg")
4
>>> solution.isPrefixOfWord("this problem is an easy problem", "pro")
2
>>> solution.isPrefixOfWord("i am tired", "you")
-1
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(), start=1):
            if word.startswith(searchWord):
                return i

        return -1
