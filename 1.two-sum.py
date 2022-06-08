#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums.pop(0)
            if target - num in nums:
                return [i,nums.index(target-num)+i+1]

            
        
# @lc code=end

