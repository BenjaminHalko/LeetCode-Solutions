class Solution(object):
    def isValid(self, s):
        current = []
        openbrackets = "{[("
        closebrackets = "}])"

        for x in s:
            if x in openbrackets:
                current.append(openbrackets.index(x))
            elif len(current) == 0: return False
            elif closebrackets.index(x) != current.pop():
                return False
        
        return len(current) == 0
        