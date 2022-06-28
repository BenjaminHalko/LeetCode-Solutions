class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        i,j,direction = 0,0,0
        
        for num in range(1,pow(n,2)+1):
            matrix[j][i] = num
            
            iNext, jNext = 0,0
            if direction % 2 == 1: jNext = 1 if direction == 1 else -1
            else: iNext = 1 if direction == 0 else -1
            
            if i+iNext < 0 or j+jNext < 0 or i+iNext >= n or j+jNext >= n or matrix[j+jNext][i+iNext] != 0:
                direction = (direction + 1) % 4
                if direction % 2 == 1: j += 1 if direction == 1 else -1
                else: i += 1 if direction == 0 else -1
            else: i,j = i+iNext,j+jNext
            
        return matrix