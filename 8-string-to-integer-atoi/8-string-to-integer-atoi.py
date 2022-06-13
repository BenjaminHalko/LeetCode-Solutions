class Solution:
    def myAtoi(self, s: str) -> int:
        nums = ""
        for n in s.strip(' '):
            if n in "1234567890" or (n in "+-" and nums == ""):
                nums += n
            else: break
        return max(min(int(nums),pow(2,31)-1),-pow(2,31)) if nums != "+" and nums != "-" and nums != "" else 0