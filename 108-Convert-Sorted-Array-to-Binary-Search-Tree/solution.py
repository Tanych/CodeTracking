# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # BST need height blanced the root should be the meadian
        n=len(nums)
        if n==0:
            return None
        if n==1:
            return TreeNode(nums[0])
        mid=(n-1)/2
        root=TreeNode(nums[mid])
        left=self.sortedArrayToBST(nums[:mid])
        right=self.sortedArrayToBST(nums[mid+1:])
        
        root.left=left
        root.right=right
        return root
        
        