# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTreeIndex(self,preorder,pstart,pend,inorder,istart,iend,indexDict):
        if pstart>pend or istart>iend:
            return None
        root=TreeNode(preorder[pstart])
        rindex=indexDict.get(preorder[pstart])
        # prestart+len of left part
        left=self.buildTreeIndex(preorder,pstart+1,pstart+rindex-istart,inorder,istart,rindex-1,indexDict)
        right=self.buildTreeIndex(preorder,pstart+rindex-istart+1,pend,inorder,rindex+1,iend,indexDict)
        root.left=left
        root.right=right
        return root
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder:
            return None
        if len(inorder)!=len(preorder):
            return None
        # index map
        indexDict={}
        for i in xrange(len(inorder)):
            indexDict[inorder[i]]=i
        
        return self.buildTreeIndex(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,indexDict)
        