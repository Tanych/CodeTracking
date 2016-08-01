# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymlevle(self,level):
        i,j=0,len(level)-1
        while i<=j:
            if not level[i] and level[j]:
                return False
            if level[i] and not level[j]:
                return False
                
            if not level[i] and not level[j]:
                i+=1
                j-=1
                continue
            
            if level[i].val!=level[j].val:
                return False
            i+=1
            j-=1
        return True
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        level=[root]
        
        while level:
            if not self.isSymlevle(level):
                return False
            tmp=[]
            for node in level:
                if node:
                    tmp.extend([node.left,node.right])
            level=tmp
            
        return True
                