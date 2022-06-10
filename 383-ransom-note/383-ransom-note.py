class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for l in ransomNote:
            if l not in magazine: return False
            x = magazine.index(l)
            magazine = magazine[:x]+magazine[x+1:]
        return True