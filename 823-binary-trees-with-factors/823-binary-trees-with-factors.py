class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        nums = {i:1 for i in arr}
        for i,num1 in enumerate(arr[1:]):
            for num2 in arr[:i+1]:
                val = num1 // num2
                if val < 2 or math.sqrt(num1) > arr[i]: break
                if num1 % num2 == 0: nums[num1] += nums[num2] * nums.get(val, 0)
        return sum(nums.values()) % 1000000007
            