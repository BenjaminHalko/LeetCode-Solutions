class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = len(t)
        if len(s) < target: return ""
        if s == t: return t
        
        sub = defaultdict(int)
        for i in t:
            sub[i] += 1
        
        start = 0
        found = defaultdict(int)
        allfound = ""
        result = ""
        minFound = -1
        for end, letter in enumerate(s):
            if letter in sub:
                found[letter] += 1
                if allfound.count(letter) < sub[letter]:
                    allfound += letter
                
            while start < end and (s[start] not in t or found[s[start]] > sub[s[start]]):
                if found[letter] >= sub[letter]:
                    allfound.replace(s[start],"",1)
                if s[start] in sub: found[s[start]] -= 1
                start += 1
            
            if len(allfound) == target and (end-start <= minFound or minFound == -1):
                minFound = end-start
                result = s[start:][:end-start+1]
        return result