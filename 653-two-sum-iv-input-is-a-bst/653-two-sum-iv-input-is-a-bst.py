# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        nums = set()
        def find(root):
            if root == None: return False
            if k - root.val in nums: return True

            nums.add(root.val)
            return find(root.left) or find(root.right)
        
        return find(root)