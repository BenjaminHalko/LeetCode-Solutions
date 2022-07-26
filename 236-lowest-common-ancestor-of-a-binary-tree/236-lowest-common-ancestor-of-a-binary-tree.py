# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(n):
            if n in (None, p, q): return n
            l, r = search(n.left), search(n.right)
            if l and r: return n
            else: return l or r
        return search(root)