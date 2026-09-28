class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        best, left = 0, 0
        for char in s:
            if char not in cur:
                cur.add(char)
                best = max(best, len(cur))
                continue
            while s[left] != char:
                cur.remove(s[left])
                left += 1
            left += 1
        return best