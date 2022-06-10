class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for l in ransomNote:
            if l not in magazine: return False
            x = magazine.index(l)
            magazine = magazine[:x]+magazine[x+1:]
        return True
        