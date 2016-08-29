# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lmapping={}
    
    def helper(self,root):
        if not root: return -1
        if not root.left and not root.right:
            self.lmapping[0]=self.lmapping.get(0,[])+[root.val]
            return 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        res=max(left,right)+1
        self.lmapping[res]=self.lmapping.get(res,[])+[root.val]
        return res
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        self.helper(root)
        return self.lmapping.values()
        