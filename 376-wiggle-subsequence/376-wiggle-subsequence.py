class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        top = bottom = 1
        
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]: top = bottom + 1
            elif nums[i-1] < nums[i]: bottom = top + 1
                
        return max(top,bottom)
            