class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        while i+1 < len(arr):
            num = max(range(i+1,len(arr)), key=arr.__getitem__)
            arr = arr[:i]+[arr[num]]*(num-i)+arr[num:]
            i = num
        
        arr[-1] = -1
        return arr