class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        median = nums[len(nums)//2]
        for num in nums: result += abs(num-median)
        return result