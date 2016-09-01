# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        # target predecessor
        self.predecessor=[]
        # target successor
        self.successor=[]
    
    def inorder(self,root,target,reverse):
        if not root: return
        self.inorder(root.right if reverse else root.left,target,reverse)
        
        if reverse:
            if root.val<=target:
                return
            self.successor.append(root.val)
        else:
            if root.val>target:
                return
            self.predecessor.append(root.val)
            
        self.inorder(root.left if reverse else root.right,target,reverse)
        
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res=[]
        self.inorder(root,target,False)
        self.inorder(root,target,True)
        for i in xrange(k):
            if not self.predecessor:
                res.append(self.successor.pop())
            elif not self.successor:
                res.append(self.predecessor.pop())
            elif abs(self.predecessor[-1]-target)<abs(self.successor[-1]-target):
                res.append(self.predecessor.pop())
            else:
                res.append(self.successor.pop())
                
        return res