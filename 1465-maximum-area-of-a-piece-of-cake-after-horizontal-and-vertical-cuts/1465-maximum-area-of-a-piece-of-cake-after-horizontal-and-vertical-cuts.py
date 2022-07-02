class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        hDiff = 0
        wDiff = 0
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        for i in range(1,len(horizontalCuts)):
            hDiff = max(hDiff,horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1,len(verticalCuts)):
            wDiff = max(wDiff,verticalCuts[i]-verticalCuts[i-1])
            
        return (hDiff * wDiff) % (pow(10,9) + 7)