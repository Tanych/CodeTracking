# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root,mapping):
        if not root:
            return 0
        if root in mapping:
            return mapping[root]
        
        max_sum=0
        if root.left:
            max_sum+=self.helper(root.left.left,mapping)+self.helper(root.left.right,mapping)
        if root.right:
            max_sum+=self.helper(root.right.left,mapping)+self.helper(root.right.right,mapping)
        
        # two situation get the max
        max_sum=max(max_sum+root.val,self.helper(root.left,mapping)+self.helper(root.right,mapping))
        mapping[root]=max_sum
        return max_sum
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        1. root stolen
        2. root not stolen
        """
        mapping={}
        return self.helper(root,mapping)
        