class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        xlen = len(shifts)
        letters = [ord(x) for x in s][::-1]
        moves = [0]*xlen
        
        result = ""
        for i,num in enumerate(shifts[::-1]):
            if i+1 < xlen: moves[i+1] = moves[i] + num
            result = chr((letters[i]+moves[i] + num - 97) % 26 + 97)+result
            
        return result