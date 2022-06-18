class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = defaultdict(int)
        for l in s:
            letters[l] += 1
        for i,l in enumerate(s):
            if letters[l] == 1:
                return i
        return -1