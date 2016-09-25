# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level=[root]
        res=0
        while level:
            tmp=[]
            for node in level:
                if node.left:
                    if not node.left.left and not node.left.right:
                        res+=node.left.val
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            level=tmp
        return res