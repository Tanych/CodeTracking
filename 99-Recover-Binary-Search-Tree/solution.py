# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # EX: 5,2,3,4,1
        # the constant space solution only, morris can work
        cur,pre=root,None
        # record the first and second wrong value
        # from above example, first should be 5 and second should be 1
        first=second=None
        # record the predeccessor of current node
        prede=None
        while cur:
            # reach the leftmost
            if not cur.left:
                # found the targets
                if prede and cur.val<prede.val:
                    if not first:
                        first=prede
                    second=cur
                # move on predeceesor and current
                prede=cur
                cur=cur.right
            else:
                pre=cur.left
                while pre.right and pre.right!=cur:
                    pre=pre.right
                # connect the predeccesor node to current
                if not pre.right:
                    pre.right=cur
                    cur=cur.left
                else:
                    # found the targets
                    if prede and cur.val<prede.val:
                        if not first:
                            first=prede
                        second=cur
                    pre.right=None
                    prede=cur
                    cur=cur.right
        # swap
        first.val,second.val=second.val,first.val
        