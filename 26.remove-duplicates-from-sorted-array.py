#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastnum = ""
        x = 0
        for num in nums:
            if lastnum == "" or lastnum != num:
                lastnum = num
                nums[x] = num
                x += 1
            elif lastnum > num: break
        return x
    
# @lc code=end

