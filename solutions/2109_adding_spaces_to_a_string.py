class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        segments = []
        start = 0

        for end in spaces:
            segments.append(s[start:end])
            start = end
        segments.append(s[start:])

        return " ".join(segments)
