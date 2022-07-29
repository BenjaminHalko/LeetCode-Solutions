class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def find(word):
            found = {}
            num = 0
            result = ""
            for i in word:
                if i in found: result += found[i]
                else:
                    found[i] = str(num)
                    result += str(num)
                    num += 1
            return result
        pattern = find(pattern)
        return [word for word in words if find(word) == pattern]