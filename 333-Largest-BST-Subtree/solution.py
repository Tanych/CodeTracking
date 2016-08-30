# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxval=0
        
    def countbst(self,root,minval,maxval):
        if not root: return 0
        if root.val<minval or root.val>maxval: return -1
        left=self.countbst(root.left,minval,root.val)
        if left==-1:return -1
        right=self.countbst(root.right,root.val,maxval)
        if right==-1: return -1
        return left+right+1
    
    def dfs(self,root):
        cnt=self.countbst(root,-1<<31,(1<<31)-1)
        if cnt!=-1:
            self.maxval=max(self.maxval,cnt)
            return
        # otherwise try left
        self.dfs(root.left)
        # try right
        self.dfs(root.right)
        
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.maxval
        