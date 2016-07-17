class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
            
        res=x
        num=n if n>=0 else -n
        for i in xrange(num-1):
            res*=x
        if n<0:
            res=1.0/res 

        return res