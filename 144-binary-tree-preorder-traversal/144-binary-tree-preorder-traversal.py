# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root == None: return []
        result = str(root.val)+" "
        root.val = None
        
        while True:
            if root.left != None:
                result += str(root.left.val)+" "
                root.left.val = root
                root = root.left
                root.val.left = root.val.right
                root.val.right = None
            elif root.right != None:
                result += str(root.right.val)+" "
                root.right.val = root
                root = root.right
                root.val.right = None
            elif root.val != None:
                root = root.val
            else:
                break
            
        return [int(x) for x in result.split()]
        