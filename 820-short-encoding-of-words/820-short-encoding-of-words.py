class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words,key=len,reverse=True)
        
        result = 0
        foundWords = set()
        for word in words:
            if word in foundWords: continue
            result += len(word)+1
            for i in range(len(word)-1,-1,-1):
                foundWords.add(word[i:])
        return result