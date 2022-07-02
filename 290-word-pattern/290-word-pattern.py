class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(s) != len(pattern): return False
        
        foundWords = {}
        foundLetters = set()
        
        for i,word in enumerate(s):
            if(word not in foundWords and pattern[i] not in foundLetters):
                foundWords[word] = pattern[i]
                foundLetters.add(pattern[i])
            elif((word in foundWords) != (pattern[i] in foundLetters)) or foundWords[word] != pattern[i]:
                return False
                
        return True