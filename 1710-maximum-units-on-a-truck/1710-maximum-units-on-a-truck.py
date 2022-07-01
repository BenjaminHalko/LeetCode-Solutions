class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        #Initialize result variable
        result = 0
        
        #Sort boxes by "box score"
        boxTypes.sort(key=lambda x: -x[1])
        
        #Loop over all box types
        for num, score in boxTypes:
            
            #Make sure num doesn't go over the truckSize left
            num = min(num,truckSize)
            
            #Add box score to result
            result += score * num
            
            #Subtrack boxes from truckSize
            truckSize -= num
            
            #Break out of loop if there is no more room on the truck
            if truckSize <= 0: break
                
        #Return the result
        return result