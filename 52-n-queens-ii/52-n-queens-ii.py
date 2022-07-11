class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(col,diag,anti_diag,row):
            if row == n: return 1
            count = 0
            for column in range(n):
                if not (col[column] or diag[row + column] or anti_diag[row - column + n - 1]):
                    col[column] = diag[row + column] = anti_diag[row - column + n - 1] = True;
                    count += solve(col, diag, anti_diag, row + 1); 
                    col[column] = diag[row + column] = anti_diag[row - column + n - 1] = False;  
            return count
        
        return solve([0]*n,[0]*(2*n-1),[0]*(2*n-1),0)