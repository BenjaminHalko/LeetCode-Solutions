# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def recurse(root,level):
            if root == None: return
            
            if len(result) <= level: result.append([])
            result[level].append(root.val)
            
            recurse(root.left,level+1)
            recurse(root.right,level+1)
            
        recurse(root,0)
        
        return result