class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        if n == 1 and target > 1: return -1

        dp = [[[float('inf')] * (n + 1) for _ in range(target + 1)] for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][0][i] = 0
        
        for i in range(1, m + 1):
            for k in range(1, n + 1):
                if houses[i - 1] and houses[i - 1] != k: continue
                for j in range(1, target + 1):
                    dp[i][j][k] = min(dp[i - 1][j - 1][:k] + dp[i - 1][j - 1][k + 1:] + [dp[i - 1][j][k]]) + cost[i - 1][k - 1] * (houses[i - 1] == 0)
                
        
        return (lambda x: -1 if x == float('inf') else x)(min(dp[m][target][1:]))