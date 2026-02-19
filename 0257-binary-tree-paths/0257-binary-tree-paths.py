# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # add current node to path
            path.append(str(node.val))
            
            # if leaf → save path
            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            
            # backtrack
            path.pop()
        
        dfs(root, [])
        return res
        