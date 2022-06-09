#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        gcd = lambda a,b : a if not b else gcd(b, a%b)
        deck.sort()
        x = deck.count(deck[0])
        i = x
        if x < 2: return False
        while i < len(deck):
            c = deck.count(deck[i])
            x = gcd(x,c)
            if x < 2: return False
            i += c
        return True

# @lc code=end