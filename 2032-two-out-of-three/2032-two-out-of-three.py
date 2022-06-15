class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        foundNums = set()
        result = []
        
        for num in nums1+nums2+nums3:
            if num not in foundNums:
                foundNums.add(num)
                if (num in nums1) + (num in nums2) + (num in nums3) >= 2:
                    result.append(num)
                    
        return result