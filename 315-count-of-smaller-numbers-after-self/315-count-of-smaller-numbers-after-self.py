class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedNums, result = sorted(nums), []
        for num in nums:
            i = bisect_left(sortedNums,num)
            result.append(i)
            del sortedNums[i]
        return result