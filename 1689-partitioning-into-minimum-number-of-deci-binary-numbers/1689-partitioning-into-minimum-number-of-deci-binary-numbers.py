class Solution:
    def minPartitions(self, num: str) -> int:
        result = 0
        for n in num:
            result = max(result,int(n))
            if result == 9: break
        return result