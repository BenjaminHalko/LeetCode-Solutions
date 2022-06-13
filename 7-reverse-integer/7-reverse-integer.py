class Solution:
    def reverse(self, x: int) -> int:
        return (lambda y: y*(1-(x < 0)*2) if y < pow(2,31)-1 else 0)(int(str(x).replace("-","")[::-1]))