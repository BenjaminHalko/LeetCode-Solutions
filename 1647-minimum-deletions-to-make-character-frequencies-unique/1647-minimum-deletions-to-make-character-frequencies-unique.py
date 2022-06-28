class Solution:
    def minDeletions(self, s: str) -> int:
        freq = defaultdict(int)
        for i in s: freq[i] += 1
        result,foundFreqs = 0,set()
        for x in freq.values():
            while x in foundFreqs:
                x -= 1
                result += 1
            if x > 0: foundFreqs.add(x)
                
        return result