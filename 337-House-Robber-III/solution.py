# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root,stolen):
        if not root:
            return 0
        if stolen:
            return self.helper(root.left,False)+self.helper(root.right,False)
        else:
           return max(root.val+self.helper(root.left,True)+self.helper(root.right,True),self.helper(root.left,False)+self.helper(root.right,False))
            
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        1. root stolen
        2. root not stolen
        """
        return max(self.helper(root,False),self.helper(root,True))
        
        