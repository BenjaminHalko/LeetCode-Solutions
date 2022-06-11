class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums)-x
        if(target == 0): return len(nums)
        elif(target < 0): return -1

        result = 0
        startPointer = 0
        currentSum = 0

        for endPointer,endNum in enumerate(nums):
            currentSum += endNum

            while startPointer < endPointer and currentSum > target:
                currentSum -= nums[startPointer]
                startPointer += 1
            
            if currentSum == target:
                if result == -1: result = endPointer-startPointer+1
                else: result = max(result,endPointer-startPointer+1)

        return -1 if result == 0 else len(nums) - result

        