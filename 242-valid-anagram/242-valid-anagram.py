class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        foundLetters = set()
        for letter in t:
            if letter not in foundLetters:
                foundLetters.add(letter)
                if s.count(letter) < t.count(letter):
                    return False
        return True