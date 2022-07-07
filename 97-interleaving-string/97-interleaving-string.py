class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)
        if s1Len + s2Len != len(s3): return False
        @cache
        def find(i1,i2):
            return (i1 == s1Len and i2 == s2Len) or (i1 < s1Len and s1[i1] == s3[i1+i2] and find(i1+1,i2)) or (i2 < s2Len and s2[i2] == s3[i1+i2] and find(i1,i2+1))
        return find(0,0)