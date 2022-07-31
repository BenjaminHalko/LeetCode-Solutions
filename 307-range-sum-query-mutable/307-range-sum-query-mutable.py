class NumArray:
    def __init__(self, nums: List[int]):
        self.nums, self.l, self.s = nums, len(nums), sum(nums)
    def update(self, index: int, val: int) -> None:
        self.nums[index], self.s = val, self.s + val - self.nums[index]
    def sumRange(self, left: int, right: int) -> int:
        return self.s - sum(self.nums[:left]) - sum(self.nums[right+1:])