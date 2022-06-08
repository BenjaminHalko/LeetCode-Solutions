#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        for word in s.split(): result += " "+word[::-1]
        return result[1:]
        
# @lc code=end

