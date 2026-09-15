class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        left, best = 0, 0
        for char in s:
            if char not in cur:
                cur.add(char)
                best = max(best, len(cur))
            else:
                while s[left] != char:
                    cur.discard(s[left])
                    left += 1
                left += 1
        return best