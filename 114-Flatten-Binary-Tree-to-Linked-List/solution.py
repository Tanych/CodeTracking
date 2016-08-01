# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pnode=None
        
    def helper(self,root):
        # recorde the left and right of root
        # in order to do the recusive after the change node
        left=root.left
        right=root.right
        
        if not self.pnode:
            # just start, move pnode to root
            self.pnode=root
            # set root with single node
            self.pnode.left=self.pnode.right=None
        else:
            self.pnode.right=root
            # move to next right node
            self.pnode=self.pnode.right
            self.pnode.left=self.pnode.right=None
            
        if left:
            self.helper(left)
        if right:
            self.helper(right)
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.helper(root)
        