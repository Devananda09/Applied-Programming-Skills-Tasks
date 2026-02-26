# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        
        while True:
            # go to leftmost node
            while root:
                stack.append(root)
                root = root.left
            
            # visit node
            root = stack.pop()
            k -= 1
            
            if k == 0:
                return root.val
            
            # go to right subtree
            root = root.right
        