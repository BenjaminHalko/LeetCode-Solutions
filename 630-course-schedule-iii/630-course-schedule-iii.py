class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses,key=lambda x: x[1])
        
        courseList = []
        currentTime = 0
        
        for duration,endTime in courses:
            heapq.heappush(courseList,-duration)
            currentTime += duration
            if currentTime > endTime: currentTime += heapq.heappop(courseList)
                
        return len(courseList)