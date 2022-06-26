class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numOfNums = defaultdict(int)
        
        for num in nums: numOfNums[num] += 1
            
        return sorted(numOfNums.items(),key=lambda i: i[1],reverse=True)[0][0]