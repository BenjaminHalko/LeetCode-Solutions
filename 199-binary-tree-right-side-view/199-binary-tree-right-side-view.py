# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def find(root,depth):
            if not root: return
            
            if len(result) == depth: result.append(root.val)
            
            find(root.right,depth+1)
            find(root.left,depth+1)
            
        find(root,0)
            
        return result