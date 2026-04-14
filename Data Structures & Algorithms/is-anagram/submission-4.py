class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def toList(string: str):
            result = []
            for i in string:
                result.append(i)
            return result
        return sorted(toList(s)) == sorted(toList(t))