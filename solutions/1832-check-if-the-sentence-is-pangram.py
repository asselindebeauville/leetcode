"""1832. Check if the Sentence Is Pangram

https://leetcode.com/problems/check-if-the-sentence-is-pangram/

>>> solution = Solution()
>>> solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
True
>>> solution.checkIfPangram("leetcode")
False
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
