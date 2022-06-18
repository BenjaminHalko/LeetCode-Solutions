class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0: return 0
        
        result = min(brackets[0][0],income) * brackets[0][1] * 0.01
        if brackets[0][0] > income: return result
        for i, tax in enumerate(brackets[1:]):
            result += (min(tax[0],income) - brackets[i][0]) * tax[1] * 0.01
            if tax[0] > income: break
        
        return result