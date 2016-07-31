# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root):
        if not root:
            return (0,0)
        # get res from left
        left=self.helper(root.left)
        # get res from right
        right=self.helper(root.right)
        
        # two situation get the max
        # not rob root, we can do 
        max_norob=max(left[0],left[1])+max(right[0],right[1])
        # not rob left and right,rob root
        max_rob=root.val+left[0]+right[0]
        
        return (max_norob,max_rob)
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        1. root stolen
        2. root not stolen
        """
        res=self.helper(root)
        return max(res[0],res[1])
        