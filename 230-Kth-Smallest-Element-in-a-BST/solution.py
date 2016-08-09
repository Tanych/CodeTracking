# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        cur=root
        stck=[]
        while stck or cur:
            if cur:
                stck.append(cur)
                cur=cur.left
            elif stck:
                k-=1
                if k==0:
                    return stck[-1].val
                cur=stck[-1].right
                stck.pop()
                