# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recurse(root):
            return 0 if root == None else max(recurse(root.left),recurse(root.right))+1
        
        return recurse(root)