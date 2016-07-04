# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTreeIndex(self,inorder,istart,iend,postorder,pstart,pend,indexDict):
        """
        check the last element in postorder, find the position in the inorder
        get the left part of the tree and the right part of the tree
        """
        if istart>iend or pstart>pend:
            return None
        root=TreeNode(postorder[pend])
        # root index
        rindex=indexDict.get(postorder[pend])
        # recursive get the left root and right root
        left=self.buildTreeIndex(inorder,istart,rindex-1,postorder,pstart,pstart+rindex-istart-1,indexDict)
        right=self.buildTreeIndex(inorder,rindex+1,iend,postorder,pstart+rindex-istart,pend-1,indexDict)
        # combine the root
        root.left=left
        root.right=right
        return root
        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        if len(inorder)!=len(postorder):
            return None
        # index map
        indexDict={}
        for i in xrange(len(inorder)):
            indexDict[inorder[i]]=i
        
        return self.buildTreeIndex(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,indexDict)
        