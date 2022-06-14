class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if(mat == target): return True
        for rotation in range(3):
            for i,row in enumerate([row.copy() for row in mat][::-1]):
                for j,num in enumerate(row):
                    mat[j][i] = num
            if(mat == target): return True
        return False