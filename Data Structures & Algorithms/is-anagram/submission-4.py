class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = set(s)
        set_t = set(t)
        alphabet_s = {}
        alphabet_t = {}
        if set_s != set_t:
            return False
        for i in set_s:
            alphabet_s[i] = 0
        for i in set_t:
            alphabet_t[i] = 0
        for i in range(len(s)):
            alphabet_s[s[i]] += 1
            alphabet_t[t[i]] += 1
        return alphabet_s == alphabet_t
            