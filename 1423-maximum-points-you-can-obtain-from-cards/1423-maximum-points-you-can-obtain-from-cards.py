class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        end = len(cardPoints) - k
        total = sum(cardPoints[end:])
        result = total

        for i in range(k):
            total += cardPoints[i] - cardPoints[end+i]
            result = max(result,total)
            
        return result