# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #morris traversal, using prev record the predecessor
        cur,prev=root,None
        res=[]
        while cur:
            # if reach the leftmost
            if not cur.left:
                res.append(cur.val)
                # to the right
                cur=cur.right
            else:
                prev=cur.left
                # fint the predecessor of the cur
                while prev.right and prev.right!=cur:
                    prev=prev.right
                # if pre.right has no node,first time get the rightmost
                if not prev.right:
                    prev.right=cur
                    cur=cur.left
                else:
                    prev.right=None
                    res.append(cur.val)
                    cur=cur.right
        return res
        
    def inorderTraversal_on(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stck,res=[],[]
        cur=root
        while cur or stck:
            if cur:
                stck.append(cur)
                cur=cur.left
            # after all the left node haved added
            elif stck:
                # get the leftmost value
                res.append(stck[-1].val)
                # go to right
                cur=stck[-1].right
                stck.pop()
                
        return res
                