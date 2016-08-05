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
        return self.isValidSerialization_stck(preorder)
        
        n=len(preorder)
        
        # the nodes lists
        nodes=preorder.split(',')
        return self.helper(nodes,0)==len(nodes)-1
    
    def isValidSerialization_stck(self,preorder):
        n=len(preorder)
        
        # the nodes lists
        nodes=preorder.split(',')
        stck=[]
        for i in xrange(len(nodes)):
            cur=nodes[i]
            while cur=='#' and stck and stck[-1]=='#':
                # pop the '#'
                stck.pop()
                if not stck:
                    return False
                # pop the number
                stck.pop()
            # add the '#' after pop in order to do next
            # or add number
            stck.append(cur)
            
        return len(stck)==1 and stck[0]=='#'
            
                