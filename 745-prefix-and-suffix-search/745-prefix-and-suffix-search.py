class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.indexes = defaultdict(int)
        
        for index, word in enumerate(words):
            self.indexes[word] = index
            
            for i in range(len(word)):
                self.prefixes[word[:i+1]].add(word)
                self.suffixes[word[i:]].add(word)
        
    def f(self, prefix: str, suffix: str) -> int:
        result = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            result = max(result,self.indexes[word])
        return result


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)