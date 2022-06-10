#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        result = 1
        j = 0
        for i,n in enumerate(s):
            while n in s[j:][:i-j] and i-j != 0:
                j += 1
            result = max(result,i-j+1)
        return result
# @lc code=end
