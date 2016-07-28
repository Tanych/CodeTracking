# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtrees(self,start,end,mapping):
        if end<start:
            return [None]
        if start==end:
            return [TreeNode(start)]
            
        if (start,end) in mapping:
            return mapping[(start,end)]
            
        res=[]
        for idx in range(start,end+1):
            # get the possible solution for left sub trees
            left_sub=self.subtrees(start,idx-1,mapping)
            # get all the solution for right
            right_sub=self.subtrees(idx+1,end,mapping)
            for left in left_sub:
                for right in right_sub:
                    root=TreeNode(idx)
                    root.left=left
                    root.right=right
                    res.append(root)
        mapping[(start,end)]=res
        return res
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        
        # recusive
        return self.subtrees(1,n,{})
        