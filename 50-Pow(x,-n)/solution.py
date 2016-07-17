class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n<0:
            n=-n
            x=1.0/x
            
        tb=[0.0]*32
        tb[0]=x
        
        res=1
        for i in xrange(1,32):
            tb[i]=tb[i-1]*tb[i-1]
        
        for i in xrange(32):
            if n&(1<<i):
                res*=tb[i]
        return res