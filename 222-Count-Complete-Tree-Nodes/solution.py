# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        if not root.left and not root.right:
            return 1
        
        left=right=0
        if root.left:
            left=self.countNodes(root.left)
        if root.right:
            right=self.countNodes(root.right)
        
        return left+right+1
        