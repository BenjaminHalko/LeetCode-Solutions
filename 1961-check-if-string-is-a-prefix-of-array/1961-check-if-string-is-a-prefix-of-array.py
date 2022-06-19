class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        total = ""
        for word in words:
            total += word
            if total == s: return True 
        return False