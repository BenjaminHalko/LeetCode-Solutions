class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end, count = 0, 0
        
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[end][1]:
                count += 1
                if intervals[i][1] <= intervals[end][1]: end = i
            else: end = i
                
        return count