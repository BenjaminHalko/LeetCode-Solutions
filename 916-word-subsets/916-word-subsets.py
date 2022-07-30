class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result, temp = [], Counter()
        for w in words2: temp |= Counter(w)
        return [w for w in words1 if not temp - Counter(w)]