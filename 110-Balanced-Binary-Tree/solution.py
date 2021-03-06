# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root):
        if not root:
            return 0
        left=self.helper(root.left)
        if left==-1:return -1
        right=self.helper(root.right)
        if right==-1: return -1
        # just the height diff
        if abs(left-right)>1: return -1
        # return the height
        return max(left,right)+1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.helper(root)!=-1
        
        