# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def right(root):
            if (root.right): return right(root.right)
            return root
        
        while root:
            if root.left: right(root.left).right, root.right, root.left = root.right, root.left, None;
            root = root.right
                