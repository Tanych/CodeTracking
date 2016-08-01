# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        stck=[root]
        min_depth=1<<31
        depth=1
        # bfs search
        while stck:
            tmp=[]
            for cur in stck:
                if not cur.right and not cur.left:
                    return depth
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
       
            depth+=1
            stck=tmp
            
        return min_depth
                
        