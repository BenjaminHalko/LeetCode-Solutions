class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for row in matrix: nums += row
        nums.sort()
        return nums[k-1]