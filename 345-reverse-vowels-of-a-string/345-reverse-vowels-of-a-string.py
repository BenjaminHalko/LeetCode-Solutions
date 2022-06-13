class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [(i,n) for i,n in enumerate(s) if n in "aeiouAEIOU"]
        for i,num in enumerate(vowels):
            s = s[:vowels[len(vowels)-i-1][0]]+num[1]+s[vowels[len(vowels)-1-i][0]+1:]
        return s