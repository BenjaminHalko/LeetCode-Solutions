class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n == 1 or '0' not in bin(max(0,n-1))[2:]