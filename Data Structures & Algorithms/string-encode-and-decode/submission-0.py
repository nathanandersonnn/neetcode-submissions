class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}*{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("*", i)          # first * after i always ends the length
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length           # jump past the string, never scan it
        return res