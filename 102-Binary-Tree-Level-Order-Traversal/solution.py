# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrdervectical(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level=[(root,0)]
        res={}
        mincol,maxcol=1<<31,-1<<31
        while level:
            for node,col in level:
                mincol=min(mincol,col)
                maxcol=max(maxcol,col)
                res[col]=res.get(col,[])+[node.val]
            tmp=[]
            for node,col in level:
                if node.left:
                    tmp.append((node.left,col-1))
                if node.right:
                    tmp.append((node.right,col+1))
            level=tmp
        reslist=[]
        for i in xrange(mincol,maxcol+1):
            reslist.append(res[i])
        return reslist
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level=[root]
        res=[]
        while level:
            res.append([node.val for node in level])
            tmp=[]
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            level=tmp
            
        return res
            