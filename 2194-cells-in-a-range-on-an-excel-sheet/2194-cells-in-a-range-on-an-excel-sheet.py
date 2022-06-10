class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(":")
        l1 = ord(s[0][0])
        l2 = ord(s[1][0])+1
        n1 = int(s[0][1])
        n2 = int(s[1][1])+1

        return [chr(l)+str(n) for l in range(l1,l2) for n in range(n1,n2)]