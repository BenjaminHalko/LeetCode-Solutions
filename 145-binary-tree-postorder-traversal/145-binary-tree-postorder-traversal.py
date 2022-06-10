# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []

        def order(root):
            if root == None: return
            order(root.left)
            order(root.right)
            result.append(root.val)
        
        order(root)

        return result
        