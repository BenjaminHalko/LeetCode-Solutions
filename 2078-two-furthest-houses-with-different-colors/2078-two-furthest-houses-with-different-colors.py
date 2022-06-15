class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist = len(colors)
        
        for index, color in enumerate(colors):
            if color != colors[-1]:
                dist = len(colors) - index
                break
                
        for index, color in enumerate(colors[::-1]):
            if color != colors[0]:
                dist = max(dist,len(colors) - index)
                break
            
        return dist - 1