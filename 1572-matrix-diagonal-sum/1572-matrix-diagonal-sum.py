class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        x = len(mat)
        for i in range(x):
            total += mat[i][i]
            if x-1-i != i: total += mat[x-1-i][i]
        return total