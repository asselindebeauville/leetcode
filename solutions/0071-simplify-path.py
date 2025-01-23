"""71. Simplify Path

https://leetcode.com/problems/simplify-path/

>>> solution = Solution()
>>> solution.simplifyPath("/home/")
'/home'
>>> solution.simplifyPath("/home//foo/")
'/home/foo'
>>> solution.simplifyPath("/home/user/Documents/../Pictures")
'/home/user/Pictures'
>>> solution.simplifyPath("/../")
'/'
>>> solution.simplifyPath("/.../a/../b/c/../d/./")
'/.../b/d'
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for component in path.split("/"):
            if component == ".":
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            elif component:
                stack.append(component)

        return "/" + "/".join(stack)
