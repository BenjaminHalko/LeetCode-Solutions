class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = [ord(x) for x in s]

        result = ""
        for i in range(len(shifts)-1,-1,-1):
            shifts[i-1] += shifts[i]
            result = chr((letters[i]+shifts[i] - 97) % 26 + 97) + result
            
        return result