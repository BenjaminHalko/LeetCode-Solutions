class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sLen = min(len(word1),len(word2))
        result = ""
        for i in range(sLen):
            result += word1[i] + word2[i]
            
        return result + word1[sLen:] + word2[sLen:]