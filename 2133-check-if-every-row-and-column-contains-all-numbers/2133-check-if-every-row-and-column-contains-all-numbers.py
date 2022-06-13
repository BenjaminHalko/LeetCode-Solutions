class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        x = len(matrix)
        total = []
        for i in range(x): total.append([])
        for row in matrix:
            thisrow = row.copy()
            thisrow.sort()
            if thisrow != list(range(1,x+1)): return False
            for i,n in enumerate(row):
                total[i].append(n)
        
        for i in total:
            i.sort()
            if i != list(range(1,x+1)): return False
        return True
        