class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 += nums2
        nums1.sort()
        x = len(nums1)
        if x % 2: return nums1[x // 2]
        x //= 2
        return (nums1[x]+nums1[x-1]) * .5
        