class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        def add10(index):
            while digits[index] >= 10:
                digits[index] -= 10
                if index == 0:
                    digits.insert(0,1)
                    index += 1
                else:
                    digits[index-1] += 1
                    add10(index-1)
                    
        digits[-1] += 1
        add10(len(digits)-1)
        
        return digits