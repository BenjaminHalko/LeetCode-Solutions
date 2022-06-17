class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        i = 2
        while i * i <= n:
            if n % i: i += 1
            else: n //= i
        return n <= 3 or n == 5