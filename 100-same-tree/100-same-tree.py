# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        return self.getdata(p,"") == self.getdata(q,"")

    def getdata(self, p, data):
        if p == None: return data + "null"
        data += str(p.val)
        data = self.getdata(p.left, data)
        data = self.getdata(p.right, data)
        return data
