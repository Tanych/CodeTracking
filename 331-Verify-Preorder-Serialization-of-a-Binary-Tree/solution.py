class Solution(object):
    def helper(self,nodes,cur):
        if cur>=len(nodes):
            return -1
        if nodes[cur]=='#':
            return cur
        
        left=self.helper(nodes,cur+1)
        if left==-1:
            return -1
        # the right node is the last leaf node +1
        right=self.helper(nodes,left+1)
        return -1 if right==-1 else right
        
        
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        n=len(preorder)
        
        # the nodes lists
        nodes=preorder.split(',')
        return self.helper(nodes,0)==len(nodes)-1
            
                