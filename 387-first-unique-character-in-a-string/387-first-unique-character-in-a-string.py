class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,l in enumerate(s):
            if s.count(l) == 1:
                return i
        return -1