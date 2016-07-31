# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        ------recusive=----------
        if root:
            root.left=self.invertTree(root.right)
            root.right=self.invertTree(root.left)
        return root
        """
        return self.bfs(root)
        
    def bfs(self,root):
        level=[root] if root else []
        
        while level:
            tmp=[]
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                node.left,node.right=node.right,node.left
            # go to next level
            level=tmp
        
        return root
        