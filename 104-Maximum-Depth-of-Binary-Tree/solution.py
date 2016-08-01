# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # dfs search
        if not root:
            return 0
        
        #return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    
        
        # the recursive method is very straightforward
        # in real or interview, need to implement using stack and some advanced traval tech
        # not level by level
        stck=[root]
        depth=0
        # bfs search
        while stck:
            tmp=[]
            depth+=1
            for cur in stck:
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            stck=tmp
        return depth
                