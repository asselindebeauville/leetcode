"""205. Isomorphic Strings

https://leetcode.com/problems/isomorphic-strings/

>>> solution = Solution()
>>> solution.isIsomorphic("egg", "add")
True
>>> solution.isIsomorphic("foo", "bar")
False
>>> solution.isIsomorphic("paper", "title")
True
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for s_char, t_char in zip(s, t):
            if (
                s_to_t.get(s_char, t_char) != t_char
                or t_to_s.get(t_char, s_char) != s_char
            ):
                return False

            s_to_t[s_char] = t_char
            t_to_s[t_char] = s_char

        return True
