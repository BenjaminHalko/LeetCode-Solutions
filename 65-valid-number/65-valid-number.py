class Solution:
    def isNumber(self, s: str) -> bool:
        for i,n in enumerate(s.lower().split("e")):
            if n == '' or i > 1: return False
            if n[0] == '+' or n[0] == '-':
                n = n[1:]

            if i == 0: n = n.replace('.','',1)
            if not n.isnumeric(): return False
        return True

        