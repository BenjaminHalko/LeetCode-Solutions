class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        allowDecrease = True
        
        for i in range(1,len(nums)):
            if nums[i] >= nums[i-1]: continue
            
            if allowDecrease:
                allowDecrease = False
                if i != 1 and nums[i-2] > nums[i]: nums[i] = nums[i-1]
                continue
                
            return False
        
        return True