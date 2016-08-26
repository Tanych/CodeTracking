# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeCnt(object):
    def __init__(self,cnt,mn,mx):
        self.cnt=cnt
        self.mn=mn
        self.mx=mx
        
class Solution(object):
    def __init__(self):
        self.bstmax=1
        
    def isValidBST_333(self, root):
        # solution for #333
        if not root:
            return 0
        self.isvalid(root)
        return self.bstmax
    
    def isvalid(self,root):
        if not root:
            return TreeCnt(-1,-1,-1)
        if not root.left and not root.right:
            return TreeCnt(1,root.val,root.val)
        
        mid=root.val
        left=self.isvalid(root.left)
        right=self.isvalid(root.right)
        
        if left.cnt>0 and right.cnt>0 and left.mx<mid and right.mn>mid:
            self.bstmax=max(self.bstmax,left.cnt+right.cnt+1)
            return TreeCnt(left.cnt+right.cnt+1,left.mn,right.mx)
        # only with right subtree
        if left.cnt==-1 and right.cnt>0 and right.mn>mid:
            self.bstmax=max(self.bstmax,right.cnt+1)
            return TreeCnt(right.cnt+1,mid,right.mx)
        #only with left subtrees
        if right.cnt==-1 and left.cnt>0 and left.mx<mid:
            self.bstmax=max(self.bstmax,left.cnt+1)
            return TreeCnt(left.cnt+1,left.mn,mid)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stck=[]
        cur=root
        pre=-1<<32
        while cur or stck:
            if cur:
                stck.append(cur)
                cur=cur.left
            elif stck:
                if stck[-1].val>pre:
                    pre=stck[-1].val
                    cur=stck[-1].right
                    stck.pop()
                else:
                    return False
        return True
        