class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0: return 1
        result = [1] + [0 for x in range(k)]
        for j in range(1, n):
            tempResult = [1] + [0 for x in range(k)]
            temp = 1
            for i in range(1, k+1):
                temp += result[i]
                if i >= j+1: temp -= result[i-j-1]
                tempResult[i] = temp
            result = tempResult
        return result[-1] % (10**9+7)