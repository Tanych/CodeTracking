class Solution(object):
    def helper(self,n):
        if n==1:
            return '1'
    
        pre=self.helper(n-1)
        n=len(pre)
        tmp=pre[0]
        num=1
        res=''
        for i in xrange(1,n):
           if pre[i]!=tmp:
               res+=str(num)+tmp
               tmp=pre[i]
               num=1
           else:
               num+=1
        # the one for only one letter
        res+=str(num)+tmp
        return res
          
        
        return res
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.helper(n)