class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found = {}
        for i,num in enumerate(numbers):
            if num in found: return [found[num],i + 1]
            found[target - num] = i + 1