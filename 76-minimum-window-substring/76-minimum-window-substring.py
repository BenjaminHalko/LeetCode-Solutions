class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = len(t)
        if len(s) < target: return ""
        if s == t: return t
        
        start = 0
        found = ""
        allfound = ""
        result = ""
        minFound = -1
        for end, letter in enumerate(s):
            if letter in t:
                found += letter
                if allfound.count(letter) < t.count(letter):
                    allfound += letter
                
            while start < end and (found.count(s[start]) > t.count(s[start]) or s[start] not in t):
                if found.count(letter) <= t.count(letter):
                    allfound.replace(s[start],"",1)
                found = found.replace(s[start],"",1)
                start += 1
            
            if len(allfound) == target and (end-start <= minFound or minFound == -1):
                minFound = end-start
                result = s[start:][:end-start+1]
        return result