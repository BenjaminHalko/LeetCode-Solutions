#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0 or (x % 10 == 0 and x != 0)): return False
        x = str(x)
        return x == x[::-1]
        
# @lc code=end

