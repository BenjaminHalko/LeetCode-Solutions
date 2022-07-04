class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        vals = defaultdict(int)
        total = result = 0
        
        for num in nums:
            total += num
            result += (total == k) + vals[total - k]
            vals[total] += 1
            
        return result