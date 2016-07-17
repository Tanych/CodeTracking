class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            return self.myPow(1.0/x,-n)
        if n==0:
            return 1
        if n==1:
            return x
        if n==2:
            return x*x
        # odd
        if not n%2:
            return self.myPow(self.myPow(x,n/2),2)
        if n%2:
            return x*self.myPow(self.myPow(x,n/2),2)
            