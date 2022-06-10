class Solution(object):
    def longestCommonPrefix(self, strs):
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
        