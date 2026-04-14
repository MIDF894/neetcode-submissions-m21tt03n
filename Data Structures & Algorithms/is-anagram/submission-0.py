class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def toArr(stirng: str):
            result = []
            for i in stirng:
                result.append(i)
            return result
        return sorted(toArr(s)) == sorted(toArr(t))