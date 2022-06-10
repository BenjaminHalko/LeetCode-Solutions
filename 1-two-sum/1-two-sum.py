class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums.pop(0)
            if target - num in nums:
                return [i,nums.index(target-num)+i+1]
                
        