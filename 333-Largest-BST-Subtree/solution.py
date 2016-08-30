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
    
    def bottomup(self,root,parent):
        # return (size,minval,maxval)
        if not root: return (0,parent.val,parent.val)
        left=self.bottomup(root.left,root)
        right=self.bottomup(root.right,root)
        if root.val<left[2] or root.val>right[1] or left[0]==-1 or right[0]==-1:
            return (-1,0,0)
        newsize=left[0]+right[0]+1
        self.maxval=max(self.maxval,newsize)
        return (newsize,left[1],right[2])
        
        
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # up-bottom
        # self.dfs(root)
        # bottom-up
        # O(n) solution
        if not root: return 0
        self.bottomup(root,None)
        return self.maxval
        