class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        total = 0
        result = 0
        for end, num in enumerate(nums):
            total += num
            while start < end and total-nums[start] >= target:
                total -= nums[start]
                start += 1
                
            if total >= target and (result == 0 or end - start + 1 < result):
                result = end - start + 1
                
        return result