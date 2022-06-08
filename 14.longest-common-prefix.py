#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs,key=len)
        out = strs.pop(0)
        for word in strs:
            if word == out: continue
            for i in reversed(range(len(out)+1)):
                if(word[:i] == out[:i]):
                    out = out[:i]
                    break
            if(out == ""): return out
        return out

# @lc code=end

