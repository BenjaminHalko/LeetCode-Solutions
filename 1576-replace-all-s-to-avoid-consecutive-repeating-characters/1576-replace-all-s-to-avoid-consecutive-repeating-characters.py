class Solution:
    def modifyString(self, s: str) -> str:
        while "?" in s:
            x = s.index("?")
            i = 97
            while (x != 0 and s[x-1] == chr(i)) or (x != len(s)-1 and s[x+1] == chr(i)):
                i += 1
            s = s.replace("?",chr(i),1)
        return s
        