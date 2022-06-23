# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror(root1,root2):
            if root1 == None and root2 == None: return True
            if not (root1 != None and root2 != None): return False
            return root1.val == root2.val and mirror(root1.left,root2.right) and mirror(root1.right,root2.left)
        
        return True if root == None else mirror(root.left,root.right)