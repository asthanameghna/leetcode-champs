class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, a in enumerate(nums):  
            needed = target - a 
            if needed in seen:
                return [seen[needed], i]
            else:
                seen[a] = i