#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    self.data = ""
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.getdata(p)
        self.data = ""
        self.getdata(q)
        data1 = self.data

    def getdata(self, p: Optional[TreeNode]):
        if(p == None)return data + "null"
        self.data += str(p.val)
        self.data = self.getdata(p.left)
        self.data = self.getdata(p.right)
        return data

# @lc code=end

