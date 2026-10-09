class Solution:
    def encode(self, strs: List[str]) -> str:
        b = ""
        for i in strs:
            if len(i) == 0:
                b +=  "." + "\n"
                continue
            b += i + "\n"

        return b.strip("\n")
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        reslst = []
        elems = s.split("\n")
        
        for i in elems:
            if i == ".":
                reslst.append("")
            else: 
                reslst.append(i)
        return reslst