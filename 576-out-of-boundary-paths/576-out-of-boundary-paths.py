class Solution:
    @lru_cache(None)
    def findPaths(self, m: int, n: int, move: int, row: int, col: int) -> int:
        return 1 if row == m or row < 0 or col < 0 or col == n else 0 if move == 0 else (self.findPaths(m,n,move-1,row+1,col) + self.findPaths(m,n,move-1,row-1,col) + self.findPaths(m,n,move-1,row,col+1) + self.findPaths(m,n,move-1,row,col-1)) % (10**9+7)