class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        result = 0
        
        sums = [[0] * (n + 1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                sums[i + 1][j + 1] = matrix[i][j] + sums[i + 1][j] + sums[i][j + 1] - sums[i][j]
            
        for i in range(m):
            for j in range(i,m):
                subSums = defaultdict(int)
                subSums[0] = 1
                
                for k in range(n):
                    total = sums[j+1][k+1] - sums[i][k+1]
                    if total - target in subSums: result += subSums[total - target]
                    subSums[total] += 1
                    
        return result