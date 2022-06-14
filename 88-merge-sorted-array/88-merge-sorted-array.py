class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i,num in enumerate(nums2[:n]):
            nums1[i+m] = num
        nums1.sort()
        