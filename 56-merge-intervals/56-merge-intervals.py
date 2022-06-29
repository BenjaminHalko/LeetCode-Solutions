class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        storedInterval = intervals[0]
        
        for i in intervals[1:]:
            if storedInterval[1] >= i[0]:
                storedInterval[1] = max(storedInterval[1],i[1])  
            else:
                result.append(storedInterval)
                storedInterval = i 
                
        return result + [storedInterval]