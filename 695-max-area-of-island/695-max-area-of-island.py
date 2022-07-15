class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0
        
        def recurse(i,j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + recurse(i+1,j) + recurse(i,j+1) + recurse(i-1,j) + recurse(i,j-1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]: result = max(result,recurse(i,j))
                    
        return result