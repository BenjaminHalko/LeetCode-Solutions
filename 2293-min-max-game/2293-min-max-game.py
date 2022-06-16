class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        lam = lambda i: max(nums[i*2],nums[i*2+1]) if i % 2 else min(nums[i*2],nums[i*2+1])
        while len(nums) > 1:
            nums = [lam(i) for i in range(len(nums)//2)]
        return nums[0]
                