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
        #self.helper(root)
        
        # let's do it in non-recursive
        if not root.left and not root.right:
            return
        
        while root:
            # start from the first left, skip the only right node
            if not root.left:
                root=root.right
                continue
            left=root.left
            # get the rightmost in the left subtree
            while left.right:
                left=left.right
            # change the pointer
            # insert the rightmost node 
            # 1.pointer to the root.right
            left.right=root.right
            # 2.make the leftsubstree in right way to the tree
            root.right=root.left
            root.left=None
            root=root.right
            
        