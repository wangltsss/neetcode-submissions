class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        cut = 0
        res = 0

        for idx, char in enumerate(s):
            if char in seen:
                cut = max(cut, seen[char] + 1)

            seen[char] = idx
            res = max(res, idx - cut + 1)

        return res
        