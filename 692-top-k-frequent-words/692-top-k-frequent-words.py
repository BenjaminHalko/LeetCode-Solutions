class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = defaultdict(int)
        words.sort()
        for word in words: frequency[word] += 1
        return [x[0] for x in sorted(frequency.items(), key=lambda item: item[1],reverse=True)[:k]]