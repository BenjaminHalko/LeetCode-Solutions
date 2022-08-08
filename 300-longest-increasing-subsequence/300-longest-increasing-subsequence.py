class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [nums[0]]
        for num in nums[1:]:
            if num > result[-1]: result.append(num)
            else: result[bisect_left(result, num)] = num
        return len(result)