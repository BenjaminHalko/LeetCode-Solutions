class Solution:
    def average(self, salary: List[int]) -> float:
        low, high, total = float('inf'),-float('inf'),0
        for num in salary:
            low = min(low,num)
            high = max(high,num)
            total += num
        return (total - low - high) / (len(salary) - 2)