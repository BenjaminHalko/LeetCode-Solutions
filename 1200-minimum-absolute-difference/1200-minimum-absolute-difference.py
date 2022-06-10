class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr) == 0: return []
        arr.sort()
        smallest = abs(arr[0]-arr[1])
        result = [[arr[0],arr[1]]]
        j = arr[1]

        for i in arr[2:]:
            x = abs(i-j)
            if x < smallest:
                smallest = x
                result = [[j,i]]
            elif x == smallest: result.append([j,i])
            j = i

        return result
        