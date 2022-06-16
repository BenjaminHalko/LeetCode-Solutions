class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        
        for num in range(2,rowIndex+2):
            row = [1]*num
            for i in range(1,num-1):
                row[i] = result[-1][i-1] + result[-1][i]
            result.append(row)
            
        return result[-1]