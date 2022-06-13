class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache
        def gettotal(pos,i):
            if i+1 < len(triangle):
                return triangle[i][pos] + min(gettotal(pos, i+1),gettotal(pos+1, i+1))
            return triangle[i][pos]
        return gettotal(0, 0)
