class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[y[x] for y in matrix] for x in range(len(matrix[0]))]