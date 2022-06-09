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
        x = len(s)
        for i in range(x):
            if x-i < result: break
            for j in range(i,x):
                result = max(result,j-i)
                if s[j] in s[i:][:j-i]: break
        return result
# @lc code=end

