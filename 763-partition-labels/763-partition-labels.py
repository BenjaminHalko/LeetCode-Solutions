class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sLen, i, result = len(s), 0, []
        last = {s[i]: i for i in range(sLen)}
        while i < sLen:
            nextLast, j = last[s[i]], i + 1
            while j < nextLast:
                nextLast = max(nextLast, last[s[j]])
                j += 1
            result.append(nextLast - i + 1)
            i = nextLast + 1
        return result