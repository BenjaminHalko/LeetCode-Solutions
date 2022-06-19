class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        wordLen = len(searchWord)
        for i in range(1,wordLen+1):
            result.append([])
            for product in products:
                if len(product) >= i and product[:i] == searchWord[:i]:
                    result[-1].append(product)
                    if len(result[-1]) >= 3: break
                        
        return result