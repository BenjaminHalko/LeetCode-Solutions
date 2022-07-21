class OrderedCounter(Counter,OrderedDict): pass
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sCount, tCount = OrderedCounter(s), OrderedCounter(t)
        if tuple(sCount.values()) != tuple(tCount.values()): return False
        
        # Backup Plan
        key = {i: j for i, j in zip(sCount.keys(), tCount.keys())}
        
        for i,letter in enumerate(s):
            if key[letter] != t[i]: return False
        
        return True