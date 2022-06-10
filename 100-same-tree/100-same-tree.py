# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.getdata(p,"") == self.getdata(q,"")

    def getdata(self, p: Optional[TreeNode], data):
        if p == None: return data + "null"
        data += str(p.val)
        data = self.getdata(p.left, data)
        data = self.getdata(p.right, data)
        return data
