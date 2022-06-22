class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = ""
        for n in b: num += str(n)
        return pow(a,int(num),1337)