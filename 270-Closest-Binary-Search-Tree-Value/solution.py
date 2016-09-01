# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff=1<<32
        res=None
        while root:
            if abs(root.val-target)<diff:
                diff=abs(root.val-target)
                res=root
            if root.val>target:
                root=root.left
            else:
                root=root.right
        return res.val if res else 0
