class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        cut = 0
        res = 1

        if len(s) == 0:
            return 0

        for idx, char in enumerate(s):
            if seen.get(char) is not None:
                cut = max(seen[char] + 1, cut)

            seen[char] = idx
            res = max(idx - cut + 1, res)

        return res
        