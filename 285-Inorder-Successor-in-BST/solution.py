# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursive(self,root,p):
        if not root:
            return None
        if p.val<root.val:
            left=self.recursive(root.left,p)
            return root if not left else left
        else:
            return self.recursive(root.right,p)
            
    def inorderpreoder(self,root,p):
        pre=None
        while root:
            if p.val>root.val:
                pre=root
                root=root.right
            else:
                root=root.left
        return pre
        
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        return self.recursive(root,p)
        suc=None
        while root:
            if p.val<root.val:
                suc=root
                root=root.left
            else:
                root=root.right
        return suc