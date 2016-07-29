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
            
        stck=[[root]]
        level=0
        # aleays check the last one
        while len(stck[-1])!=0:
            level+=1
            tmp=[]
            # if the even level
            if not level&1:
                for i in xrange(len(stck[-1])-1,-1,-1):
                    if stck[-1][i].left:
                        tmp.append(stck[-1][i].left)
                    if stck[-1][i].right:
                        tmp.append(stck[-1][i].right)
            # reverse
            else:
                for i in xrange(len(stck[-1])-1,-1,-1):
                    if stck[-1][i].right:
                        tmp.append(stck[-1][i].right)
                    if stck[-1][i].left:
                        tmp.append(stck[-1][i].left)
            stck.append(tmp)
            
        res=[]
        # deal with the stack res
        for i in xrange(len(stck)):
            tmp=[]
            for j in xrange(len(stck[i])):
                tmp.append(stck[i][j].val)
            if tmp:
                res.append(tmp)
        return res
        