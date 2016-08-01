# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self,root,res):
        if not root:
            return res.append('#')
            
        res.append(str(root.val))
        self.tree2str(root.left,res)
        self.tree2str(root.right,res)  
        
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        resp=[]
        resq=[]
        self.tree2str(p,resp)
        self.tree2str(q,resq)
        #print resp,resq
        return ''.join(resp)==''.join(resq)
        
        