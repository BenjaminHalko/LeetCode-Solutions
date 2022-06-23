class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word[0].lower() + word[1:] == word.lower()