class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        nums.sort()
        streak = 0
        result = 1
        for i,n in enumerate(nums):
            if n == nums[i-1]+1:
                streak += 1
                if streak > result:
                    result = streak
            elif n != nums[i-1]:
                streak = 1
        return result