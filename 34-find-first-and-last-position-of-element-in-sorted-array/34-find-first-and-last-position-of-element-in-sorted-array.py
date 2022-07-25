class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1]*2
        start = nums.index(target)
        for i in range(start+1,len(nums)):
            if nums[i] != target: return [start,i-1]
        return [start,len(nums)-1]