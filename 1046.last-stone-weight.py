#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            val = stones.pop()-stones.pop()
            if len(stones) == 0: return val
            if val != 0:
                if stones[-1] <= val:
                    stones.append(val)
                    continue

                for i,n in enumerate(stones):
                    if(n >= val):
                        stones.insert(i, val)
                        break

        return stones[0] if len(stones) else 0

# @lc code=end
