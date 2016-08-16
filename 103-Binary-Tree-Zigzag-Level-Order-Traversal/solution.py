# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        res=[]
        nlevel=0
        level=[root]
        # aleays check the last one
        while level:
            nlevel+=1
            tmp=[]
            vals=[]
            for node in level:
                vals.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if nlevel&1:
                res.append(vals)
            else:
                res.append(vals[::-1])
            level=tmp
        return res
        