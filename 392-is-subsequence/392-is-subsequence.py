class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        try:
            i = 0
            for letter in s:
                i += t[i:].index(letter) + 1
                print(i)
            return True
        except ValueError: return False