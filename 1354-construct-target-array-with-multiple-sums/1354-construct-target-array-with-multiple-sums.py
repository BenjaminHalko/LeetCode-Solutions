class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        targetOnes = [1]*len(target)
        while max(target) != 1:
            
            #Get Maximum
            maxIndex = max(range(len(target)), key=target.__getitem__)
            
            #Get total
            total = sum(target) - target[maxIndex]
            
            if(total >= target[maxIndex] or total == 0 or (target[maxIndex] % total == 0  and total != 1)):
                return False
            
            target[maxIndex] = target[maxIndex] % total
            
        return True