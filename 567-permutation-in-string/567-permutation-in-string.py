class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        numsOriginal = Counter(s1)
        nums = numsOriginal.copy()
        start = 0
        
        for i,letter in enumerate(s2):
            if letter not in nums:
                nums = numsOriginal.copy()
                start = i+1
            else:
                nums[letter] -= 1
                if nums[letter] == 0 and max(nums.values()) == 0: return True
                while nums[letter] < 0:
                    if s2[start] in nums: nums[s2[start]] = min(nums[s2[start]]+1,numsOriginal[s2[start]])
                    start += 1
        
        return False