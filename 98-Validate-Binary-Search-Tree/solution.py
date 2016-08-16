# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
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
        