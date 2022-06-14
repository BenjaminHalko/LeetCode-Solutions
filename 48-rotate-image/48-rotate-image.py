class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i,row in enumerate([row.copy() for row in matrix][::-1]):
            for j,num in enumerate(row):
                matrix[j][i] = num
        