class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        
        for freq in sorted(collections.Counter(s).values(), reverse=True):
            if freq % 2 and result % 2: result -= 1
            result += freq
            
        return result