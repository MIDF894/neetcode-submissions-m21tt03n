class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if len(s) != len(t):
            return False
        
        d = {}
        b = {}
        for i in range(len(s)):
            d[s[i]] = i
            b[t[i]] = i
        return d == b