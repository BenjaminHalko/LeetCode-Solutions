class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if sLen < 2: return s
        
        result = s[0]
        maxTotal = 0
        
        for i,letter in enumerate(s):
            #aba
            j = 1
            while i-j >= 0 and i+j < sLen and s[i-j] == s[i+j]:
                if j*2+1 > maxTotal:
                    maxTotal = j*2+1
                    result = s[i-j:][:j*2+1]
                j += 1
            #bb
            j = 0
            while i-j-1 >= 0 and i+j < sLen and s[i-j-1] == s[i+j]:
                if (j+1)*2 > maxTotal:
                    maxTotal = (j+1)*2
                    result = s[i-j-1:][:(j+1)*2]
                j += 1
            
        return result