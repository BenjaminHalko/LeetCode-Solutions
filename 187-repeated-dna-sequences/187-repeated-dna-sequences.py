class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = set()
        result = set()
        
        for i in range(len(s) - 9):
            if s[i:i+10] not in sequences: sequences.add(s[i:i+10])
            elif s[i:i+10] not in result: result.add(s[i:i+10]) 
                
        return result