class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        kLen = len(str(k))
        
        def add10(index,num):
            while num[index] >= 10:
                num[index] -= 10
                if index == 0:
                    num.insert(0,1)
                    index += 1
                else:
                    num[index-1] += 1
                    add10(index-1,num)
        if kLen > len(num): num = [0]*(kLen-len(num)) + num
        for i,n in enumerate(str(k)):
            num[len(num)-kLen+i] += int(n)
            add10(len(num)-kLen+i,num)
            
        return num