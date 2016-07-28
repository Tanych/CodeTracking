# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def deepcopy(self,root,offset):
        if not root:
            return None
        newroot=TreeNode(root.val+offset)
        newroot.left=self.deepcopy(root.left,offset)
        newroot.right=self.deepcopy(root.right,offset)
        return newroot
            
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        
        dp=[[] for _ in xrange(n+1)]
        dp[0].append(None)
        
        for i in xrange(1,n+1):
            for j in xrange(i):
                for lnode in dp[j]:
                    for rnode in dp[i-j-1]:
                        newroot=TreeNode(j+1)
                        # the left sub stree can be directly add to the tree
                        # since the node is less the root node
                        # j=2 root.val=3 and dp[j]==[[1,null,2][2,1]] and the dp[j]
                        # can be directly add to the left subtree
                        newroot.left=lnode
                        """
                        for the right subtree, we need reconstruct the right part
                        ex j=0, root.val=1 dp[i-j-1]=dp[2]=[[1,null,2][2,1]]
                        if we directly add dp[2] it would has duplicate nodes, so
                        the start offset is the root.val, update the whole subtree
                        """
                        newroot.right=self.deepcopy(rnode,j+1)
                        dp[i].append(newroot)
        return dp[n]
        