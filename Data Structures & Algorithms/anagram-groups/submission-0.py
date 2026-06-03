class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        copystrs = []

        for i in strs:
            copystrs.append("".join(sorted(i)))
        copystrs = set(copystrs)

        for n in copystrs:
            vremenilst = []
            for o in strs:
                if n == "".join(sorted(o)):
                    vremenilst.append(o)
            result.append(vremenilst)
        return result