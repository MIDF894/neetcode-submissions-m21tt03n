class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def toList(stirng: str):
            result = []
            for i in stirng:
                result.append(i)
            return result
        return sorted(toList(s)) == sorted(toList(t))