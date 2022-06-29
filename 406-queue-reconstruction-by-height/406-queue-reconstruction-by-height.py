class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for x in sorted(people,key=lambda x: (-x[0],x[1])): result.insert(x[1],x)
        return result