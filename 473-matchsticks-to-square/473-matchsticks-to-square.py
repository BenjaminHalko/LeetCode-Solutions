class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total < 4 or total % 4: return False
        edge = total // 4
        matchsticks.sort(reverse=True)
        @cache
        def findedges(l1, l2, l3, l4, i):
            return l1 == l2 == l3 == l4 == edge or (i <= len(matchsticks) - 1 and l1 <= edge and l2 <= edge and l3 <= edge and l4 <= edge and (findedges(l1 + matchsticks[i], l2, l3, l4, i + 1) or findedges(l1, l2 + matchsticks[i] , l3, l4, i + 1) or findedges(l1, l2, l3 + matchsticks[i], l4, i + 1) or findedges(l1, l2, l3, l4 + matchsticks[i] , i + 1)))
        
        return findedges(0, 0, 0, 0, 0)