class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = set()
        result = []
        
        for i in range(len(s) - 9):
            if s[i:][:10] not in sequences: sequences.add(s[i:][:10])
            elif s[i:][:10] not in result: result.append(s[i:][:10]) 
                
        return result