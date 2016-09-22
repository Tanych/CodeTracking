# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res=[]
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path=""
        if not root:
            return []
        return self.helper(root,path)

    def helper(self,root,path):
        path+=str(root.val)
        if not root.left and not root.right:
            self.res.append(path)
        path+="->"
        if root.left:
            self.helper(root.left,path)
        if root.right:
            self.helper(root.right,path)
        return  self.res
        