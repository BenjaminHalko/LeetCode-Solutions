class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        xlen = len(arr)
        if xlen < 2: return False
        decreasing = False
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]: return False
            if arr[i] > arr[i-1] and decreasing: return False
            if arr[i] < arr[i-1] and not decreasing:
                if i == 1: return False
                decreasing = True
                
        return decreasing