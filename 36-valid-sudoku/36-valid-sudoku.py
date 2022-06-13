class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        foundcol = []
        for i in range(9): foundcol.append(set())
        foundbox = []
        for i in range(9): foundbox.append(set())
        for row,boardrow in enumerate(board):
            found = set()
            for col,num in enumerate(boardrow):
                if num == ".": continue
                if num in found or num in foundcol[col] or num in foundbox[(row // 3) * 3+col // 3]: return False
                found.add(num)
                foundcol[col].add(num)
                foundbox[(row // 3) * 3+col // 3].add(num)
        print(foundcol)        
        return True