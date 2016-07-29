class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        n=len(preorder)
        
        # the nodes lists
        nodes=preorder.split(',')
        # using indgree and outdgree
        # the finall total should be 0
        # the root has no ingree 
        degree=-1
        for node in nodes:
            degree+=1
            # if degree is total larger, directly return
            if degree>0:
                return False
            # for none leaf node outdgree is 2
            if node!='#':
                degree-=2
        
        return degree==0
            
                