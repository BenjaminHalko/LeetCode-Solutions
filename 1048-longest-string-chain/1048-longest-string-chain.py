class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        
        wordNum = {}
        for word in words:
            wordNum[word] = max(wordNum.get(word[:i]+word[i+1:],0) + 1 for i in range(len(word)))
            
        return max(wordNum.values())