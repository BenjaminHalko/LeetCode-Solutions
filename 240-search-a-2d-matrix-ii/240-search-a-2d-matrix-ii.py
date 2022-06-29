class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix[::-1]:
            if row[0] > target: continue
            for n in row[::-1]:
                if n < target: continue
                if n == target: return True
        return False