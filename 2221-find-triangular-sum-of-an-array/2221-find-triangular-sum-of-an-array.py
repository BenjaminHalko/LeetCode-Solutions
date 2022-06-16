class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            nums = [nums[x]+nums[x+1] % 10 for x in range(i)]
        return nums[0] % 10