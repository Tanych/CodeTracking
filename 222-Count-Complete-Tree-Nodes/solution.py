# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lheight(self,root):
        depth=0
        while root:
            root=root.left
            depth+=1
        return depth
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        left=self.lheight(root.left)
        right=self.lheight(root.right)
        # since it's a complete tree, the short part could have
        # the 2 to short depth nodes
        if left>right:
            return self.countNodes(root.left)+(1<<right)
        else:
            return self.countNodes(root.right)+(1<<left)
            
        