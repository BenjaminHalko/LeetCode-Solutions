class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        counter = defaultdict(int)
        result = 0
        startPointer = 0
        total = 0

        for endPointer,num in enumerate(nums):
            total += num
            counter[num] += 1
            while startPointer < endPointer and counter[num] > 1:
                total -= nums[startPointer]
                counter[nums[startPointer]] -= 1
                startPointer += 1
            
            result = max(result,total)

        return result
        