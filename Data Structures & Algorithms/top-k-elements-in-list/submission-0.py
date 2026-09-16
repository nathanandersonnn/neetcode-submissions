class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        arr = []
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        for i in range(k):
            temp = max(seen, key=seen.get)
            arr.append(temp)
            del seen[temp]
        return arr