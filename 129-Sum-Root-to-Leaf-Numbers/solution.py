# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,root,path,res):
        if not root.left and not root.right:
            res.append(path+str(root.val))
            return
        if root.left:
            self.dfs(root.left,path+str(root.val),res)
        if root.right:
            self.dfs(root.right,path+str(root.val),res)
            
    def sumNumbersRec(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        res=[]
        self.dfs(root,'',res)
        
        sum_res=0
        for i in xrange(len(res)):
            sum_res+=int(res[i])
        return sum_res
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        # using stack 
        if not root:
            return 0
            
        stck=[root]
        sum_res=0
        while stck:
            cur=stck.pop()
            if cur.left:
                cur.left.val=cur.val*10+cur.left.val
                stck.append(cur.left)
            if cur.right:
                cur.right.val=cur.val*10+cur.right.val
                stck.append(cur.right)
            # reach leaf
            if not cur.left and not cur.right:
                sum_res+=cur.val
                
        return sum_res
            
        