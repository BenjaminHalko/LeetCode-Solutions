class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0: return 0
        
        result = min(brackets[0][0],income) * brackets[0][1] * 0.01
        
        for i, tax in enumerate(brackets[1:]):
            if brackets[i][0] > income: break
            result += (min(tax[0],income) - brackets[i][0]) * tax[1] * 0.01
            
        return result