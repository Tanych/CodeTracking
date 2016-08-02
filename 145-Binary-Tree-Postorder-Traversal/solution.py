# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def reverse(self,from_node,to_node):
        if from_node==to_node:
            return
        a,b,c=from_node,from_node.right,None
        while True:
            c=b.right
            b.right=a
            a=b
            b=c
            if a==to_node:break
    
        
    def reverseadd(self,from_node,to_node,res):
        self.reverse(from_node,to_node)
        p=to_node
        
        while True:
            res.append(p.val)
            if p==from_node:
                break
            p=p.right
        # get back
        self.reverse(to_node,from_node)
        
    def postorderTraversal(self,root):
        dump=TreeNode(-1)
        dump.left=root
        cur,pre=dump,None
        res=[]
        while cur:
            if not cur.left:
                cur=cur.right
            else:
                pre=cur.left
                while pre.right and pre.right!=cur:
                    pre=pre.right
                if not pre.right:
                    pre.right=cur
                    cur=cur.left
                else:
                    self.reverseadd(cur.left,pre,res)
                    pre.right=None
                    cur=cur.right
        return res
                
        
    def postorderTraversal_on(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # using stack ways
        stck=[]
        # current node
        cur=root
        peak=last=None
        res=[]
        while cur or stck:
            if cur:
                stck.append(cur)
                cur=cur.left
            elif stck:
                # get the peak
                peak=stck[-1]
                # if has right branch, we need get right first
                # mark the peak and add the right subtree to stack
                # if subtree has all print out, add the peak val
                # last!=peak.right, aviod revisited
                if peak.right and last!=peak.right:
                    cur=peak.right
                # no right branch, directly add to res
                else:
                    res.append(peak.val)
                    last=peak
                    stck.pop()
        return res
                