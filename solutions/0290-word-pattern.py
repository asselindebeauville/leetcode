"""290. Word Pattern

https://leetcode.com/problems/word-pattern/

>>> solution = Solution()
>>> solution.wordPattern("abba", "dog cat cat dog")
True
>>> solution.wordPattern("abba", "dog cat cat fish")
False
>>> solution.wordPattern("aaaa", "dog cat cat dog")
False
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if (
                char_to_word.get(char, word) != word
                or word_to_char.get(word, char) != char
            ):
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True
