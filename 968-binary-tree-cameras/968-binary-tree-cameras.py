# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None: return 1
        
        def camera(root):
            if root == None: return 0
            result = camera(root.left) + camera(root.right)
            current = min(root.left.val if root.left != None else float("inf"), root.right.val if root.right != None else float("inf"))
            
            if current == 0:
                root.val = 1
                return result + 1
            
            if current == 1:
                root.val = 2
                
            return result
        
        return camera(root) + (root.val == 0)