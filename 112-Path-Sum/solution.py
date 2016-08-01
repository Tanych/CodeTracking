# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
            
        stck=[root]
        sum_res=0
        while stck:
            cur=stck.pop()
            if cur.left:
                cur.left.val=cur.val+cur.left.val
                stck.append(cur.left)
            if cur.right:
                cur.right.val=cur.val+cur.right.val
                stck.append(cur.right)
            # get the leaf
            if not cur.right and not cur.left:
                if cur.val==sum:
                    return True
                    
        return False
            