class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        numEnd = len(nums)-1
        
        i = 0
        while i < numEnd:
            start = i+1
            end = numEnd
            
            while start != end:
                total = nums[i]+nums[start]+nums[end]
                if total < 0: start += 1
                else:
                    if total == 0: result.append([nums[i],nums[start],nums[end]])
                    end -= 1
                    while start != end and nums[end] == nums[end+1]: end -= 1
            
            i += 1
            while i < numEnd and nums[i] == nums[i-1]: i += 1
                    
        return result