class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 2:
                if min(nums[i:]) != 2:
                    while nums[i] == 2: nums.append(nums.pop(i))
            if nums[i] == 0: nums.insert(0,nums.pop(i))