class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1] + [0] * (len(ratings) - 1)
        
        for i in range(1,len(ratings)):
            ans[i] = ans[i-1] + 1 if ratings[i] > ratings[i-1] else 1
            
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]: ans[i] = max(ans[i], ans[i+1] + 1)
                
        return sum(ans)