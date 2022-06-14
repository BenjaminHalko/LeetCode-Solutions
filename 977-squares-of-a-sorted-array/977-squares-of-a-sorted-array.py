class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        val = [x*x for x in nums]
        val.sort()
        return val