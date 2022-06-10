# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        
        def travel(root,i,j):
            if j not in d:
                d[j] = {}

            if i not in d[j]:
                d[j][i] = []
            
            d[j][i].append(root.val)
            if root.left != None: travel(root.left,i+1,j-1)
            if root.right != None: travel(root.right,i+1,j+1)

        travel(root, 0, 0)

        result = []
        for x,i in sorted(d.items()):
            temp = []
            for y,j in sorted(i.items()):
                j.sort()
                temp += j
            result.append(temp)

        return result
        