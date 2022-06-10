class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == "": return 0
        result = 1
        j = 0
        for i,n in enumerate(s):
            while n in s[j:][:i-j] and i-j != 0:
                j += 1
            result = max(result,i-j+1)
        return result