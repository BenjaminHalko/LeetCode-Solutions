class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        nums.sort()
        for i,n in enumerate(nums):
            if i+1 < len(nums) and nums[i+1] == n: return True
        return False