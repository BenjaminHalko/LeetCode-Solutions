class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if sorted(nums,reverse=True) == nums: return -1
        
        value = -1
        lowest = float('inf')
        
        for num in nums:
            if num < lowest:
                lowest = num
                continue
                
            value = max(value,num-lowest)
            
        return value