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
        """
        resp=[]
        resq=[]
        self.tree2str(p,resp)
        self.tree2str(q,resq)
        return ''.join(resp)==''.join(resq)
        """
        # another naive way
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p==q
        """
        # using stack
        if not p and not q:
            return True
        
        stk=[(p,q)]
        while stk:
            n1,n2=stk.pop()
            if n1 and n2 and n1.val!=n2.val:
                return False
            elif n1 and n2:
                stk.extend([(n1.right,n2.right),(n1.left,n2.left)])
            elif n1 or n2:
                return False
                
        return True
        