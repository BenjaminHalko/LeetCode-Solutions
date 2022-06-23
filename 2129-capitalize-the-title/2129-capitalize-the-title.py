class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = ""
        for word in title.lower().split():
            result += " " + (word[0].upper() + word[1:] if len(word) > 2 else word)
        return result[1:]