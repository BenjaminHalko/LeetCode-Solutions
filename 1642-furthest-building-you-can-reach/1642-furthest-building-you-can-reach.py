class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heightAmounts = []
        
        for b in range(1,len(heights)):
            height = heights[b] - heights[b-1]
            
            #Move to the next building if our height is <= to previous height
            if height <= 0:
                continue
            
            heapq.heappush(heightAmounts,height)
            
            #If we have no ladders, replace them with bricks
            if len(heightAmounts) > ladders:
                bricks -= heapq.heappop(heightAmounts)
            
            #If all checks fail, we have run out of bricks, return the building number
            if bricks < 0:
                return b - 1
            
        return len(heights) - 1