# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        level=[(root.left, root.right)]
        
        while level:
            n1,n2=level.pop()
            if n1 and n2 and n1.val != n2.val:
                return False
            elif n1 and n2:
                # get the mirror ndoe
                level.extend([(n1.left, n2.right), (n1.right, n2.left)])
            elif n1 or n2:
                return False
        return True
                