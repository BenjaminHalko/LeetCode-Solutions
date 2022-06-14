class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = len(t)
        if len(s) < target: return ""
        if s == t: return t
        
        sub = defaultdict(int)
        for i in t: sub[i] += 1
        
        start = 0
        found = defaultdict(int)
        foundnum = 0
        
        result = ""
        minFound = -1
        
        for end, letter in enumerate(s):
            if letter in sub:
                found[letter] += 1
                if found[letter] <= sub[letter]:
                    foundnum += 1
                
            while start < end and (s[start] not in t or found[s[start]] > sub[s[start]]):
                if s[start] in sub:
                    if found[letter] < sub[letter]:
                        foundnum -= 1
                    found[s[start]] -= 1
                start += 1

            if foundnum >= target and (end-start <= minFound or minFound == -1):
                minFound = end-start
                result = s[start:][:end-start+1]
        return result