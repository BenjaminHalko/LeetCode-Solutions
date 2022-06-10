class Solution(object):
    def removeDuplicates(self, nums):
        lastnum = ""
        x = 0
        for num in nums:
            if lastnum == "" or lastnum != num:
                lastnum = num
                nums[x] = num
                x += 1
            elif lastnum > num: break
        return x
        