#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        x = len(nums1)
        if x % 2: return nums1[x // 2]
        x //= 2
        return (nums1[x]+nums1[x-1]) * .5
# @lc code=end

