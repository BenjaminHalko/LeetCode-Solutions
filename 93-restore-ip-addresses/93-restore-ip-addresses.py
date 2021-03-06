class Solution(object):
    def restoreIpAddresses(self, s):
        result = []

        def findall(p,s,n):
            if(len(s) == 0): return

            if(n == 3):
                if len(s) <= 3 and int(s) <= 255 and (s[0] != "0" or s == "0"): result.append(p+s)
                return

            for i in range(1,min(4,len(s))):
                if int(s[:i]) <= 255 and (s[0] != "0" or s[:i] == "0"):
                    findall(p+s[:i]+".",s[i:],n+1)

        findall("",s,0)

        return result
        