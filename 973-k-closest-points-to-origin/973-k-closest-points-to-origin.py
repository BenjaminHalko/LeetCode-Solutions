class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x: x[0]*x[0]+x[1]*x[1]
        points = sorted(points,key=dist)
        return points[:k]
        