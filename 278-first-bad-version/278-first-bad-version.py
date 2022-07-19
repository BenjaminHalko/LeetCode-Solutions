# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s,e,m,result = 1,n,(1+n)//2,0
        while s <= e:
            if isBadVersion(m): e, result = m - 1, m
            else: s = m + 1
            m = (e+s)//2
        return result