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
            
        res=1
        while n>0:
            if n&1:
                res*=x
            x*=x
            n/=2
        return res
            