class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = [(-nums[0],0)]
        
        for i in range(1,n):
            while h[0][1] < i - k: heappop(h)
            if i == n - 1: return - h[0][0] + nums[i]
            heappush(h,(h[0][0] - nums[i], i))
            
        return nums[0]