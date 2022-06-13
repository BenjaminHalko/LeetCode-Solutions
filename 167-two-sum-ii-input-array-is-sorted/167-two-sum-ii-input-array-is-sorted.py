class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            num = numbers.pop(0)
            if target - num in numbers:
                return [i+1,numbers.index(target-num)+i+2]