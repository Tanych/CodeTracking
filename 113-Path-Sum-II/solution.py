# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root,path,res,sum_value):
        if not root.left and not root.right:
            path+=[root.val]
            if sum(path)==sum_value:
                res.append(path)
            return
        if root.left:
            self.helper(root.left,path+[root.val],res,sum_value)
        if root.right:
            self.helper(root.right,path+[root.val],res,sum_value)
            
    def pathSum(self, root, sum_num):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        res=[]
        self.helper(root,[],res,sum_num)
        return res
        