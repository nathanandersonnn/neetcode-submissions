class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            needs = target - num
            if needs in seen:
                return [seen[needs], i]
            seen[num] = i