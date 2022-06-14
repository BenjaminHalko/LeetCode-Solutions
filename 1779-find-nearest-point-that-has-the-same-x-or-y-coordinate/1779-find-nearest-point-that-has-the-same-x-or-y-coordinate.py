class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        smallestDistance = -1
        for i, point in enumerate(points):
            if x != point[0] and y != point[1]: continue
            dist = abs(x-point[0])+abs(y-point[1])
            if dist < smallestDistance or smallestDistance == -1:
                smallestDistance = dist
                index = i
        return index