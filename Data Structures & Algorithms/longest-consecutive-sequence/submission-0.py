class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        best = 0
        for num in nums:
            seen.add(num)
        for num in seen:
            cur = 0
            if num - 1 not in seen:
                while num in seen:
                    num += 1
                    cur += 1
                    best = max(best, cur)

        return best