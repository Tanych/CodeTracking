class Solution(object):
    def verifypostorder(self,postorder):
        # left-right-root
        stck=[]
        maxnum=1<<31
        for i in xrange(len(postorder)-1,-1,-1):
            if postorder[i]>maxnum:return False
            while stck and postorder[i]<stck[-1]:
                maxnum=stck.pop()
            stck.append(maxnum)
        return True
        
        #---O(1)
        
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        #return self.verifypostorder(preorder)
        """
        stck=[]
        minnum=-1<<31
        for num in preorder:
            if num<minnum:return False
            while stck and num>stck[-1]:
                minnum=stck.pop()
            stck.append(num)
        return True
        """
        #---O(1)
        i,minnum=-1,-1<<31
        for num in preorder:
            if num<minnum:return False
            while i>=0 and num>preorder[i]:
                minnum=preorder[i]
                i-=1
            i+=1
            preorder[i]=num
        return True