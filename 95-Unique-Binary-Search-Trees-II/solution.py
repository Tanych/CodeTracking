# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtrees(self,lst):
        if len(lst)==0:
            return [None]
        if len(lst)==1:
            return [TreeNode(lst[0])]
        
        res=[]
        for idx,value in enumerate(lst):
            # get the possible solution for left sub trees
            left_sub=self.subtrees(lst[:idx])
            # get all the solution for right
            right_sub=self.subtrees(lst[idx+1:])
            for left in left_sub:
                for right in right_sub:
                    root=TreeNode(value)
                    root.left=left
                    root.right=right
                    res.append(root)
        return res
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        # recusive
        return self.subtrees(range(1,n+1))
        