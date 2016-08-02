# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur,prev=root,None
        res=[]
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                
                # reach the right most
                if not prev.right:
                    res.append(cur.val)
                    prev.right=cur
                    cur=cur.left
                else:
                    prev.right=None
                    cur=cur.right
        return res
                
                
        
    def preorderTraversal_on(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # using stack
        cur,stck=root,[]
        res=[]
        while cur or stck:
            if cur:
                # this is the only diffrent from inorder
                res.append(cur.val)
                stck.append(cur)
                cur=cur.left
            elif stck: 
                cur=stck[-1].right
                stck.pop()
                
        return res
        