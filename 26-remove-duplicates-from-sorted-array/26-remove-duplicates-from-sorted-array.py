class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastnum = ""
        x = 0
        for num in nums:
            if lastnum == "" or lastnum != num:
                lastnum = num
                nums[x] = num
                x += 1
            elif lastnum > num: break
        return x
    