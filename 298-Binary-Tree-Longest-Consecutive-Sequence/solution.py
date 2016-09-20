# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,target,root,curlen):
        if not root:
            return curlen
        # if not consectutive, reset
        if root.val!=target:
            curlen=0
            
        curlen+=1
        left=self.dfs(root.val+1,root.left,curlen)
        right=self.dfs(root.val+1,root.right,curlen)
        # get the max from the subtree
        return max(curlen,left,right)
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        return self.dfs(-1,root,0)
        