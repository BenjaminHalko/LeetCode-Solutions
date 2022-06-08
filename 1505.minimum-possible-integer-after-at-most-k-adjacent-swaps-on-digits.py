#
# @lc app=leetcode id=1505 lang=python3
#
# [1505] Minimum Possible Integer After at Most K Adjacent Swaps On Digits
#

# @lc code=start
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        numbers = {}
        numarray = [int(i) for i in num]
        for i,n in enumerate(num):
            n = int(n)
            if n in numbers: numbers[n].append(i)
            else: numbers[n] = [i]

        for i in range(10):
            if i in numbers: numbers[i].sort()
        
        for loop in range(k):
            breakout = False
            for i,n in enumerate(numarray):
                for numtoreplace in range(n):
                    if numtoreplace in numbers:
                        if numbers[numtoreplace][-1] > i:
                            numarray[i] = numtoreplace
                            numarray[numbers[numtoreplace][-1]] = n
                            numbers[]
                            breakout = True
                            break
                if breakout: break

        num = ""
        for i in numarray: num += str(i)
        return num
            
# @lc code=end

