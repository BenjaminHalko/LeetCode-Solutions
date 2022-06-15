class Solution:
    def intersect(self, main: List[int], sub: List[int]) -> List[int]:
        if len(sub) > len(main):
            main,sub = sub,main
            
        numbersFound = set()
        result = []
        
        for n in sub:
            if n not in numbersFound:
                numbersFound.add(n)
                result += [n]*min(main.count(n),sub.count(n))
                
        return result
            