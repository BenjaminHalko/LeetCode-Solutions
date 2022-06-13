class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxtotal = 0
        found = False
        for n in nums:
            total += n
            
            if total > maxtotal or not found:
                maxtotal = total
                result = nums
                found = True
            
            if total < 0:
                total = 0
        
        return maxtotal
    