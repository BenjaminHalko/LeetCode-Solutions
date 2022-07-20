class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        if not words or not s: return 0
        
        buckets = defaultdict(lambda: deque([]))
        for word in words:
            buckets[word[0]].append(word)
        
        result = 0
        for letter in s:
            for _ in range(len(buckets[letter])):
                word = buckets[letter].popleft()
                if len(word) == 1: result += 1
                else: buckets[word[1]].append(word[1:])
                
        return result