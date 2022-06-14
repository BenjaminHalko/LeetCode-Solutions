class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s.lower() if ch.isalnum())
        print(s)
        return s == s[::-1]