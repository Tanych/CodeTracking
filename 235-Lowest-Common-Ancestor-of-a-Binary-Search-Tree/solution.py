# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not q or not p:
            return None
        
        if p.val>q.val:
            return self.lowestCommonAncestor(root,q,p)
            
        while True:
            if p.val>root.val and q.val>root.val:
                root=root.right
            elif p.val<root.val and q.val<root.val:
                root=root.left
            else:
                return root
        