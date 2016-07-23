class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if n==2: return 2
        a=1
        b=2
        for i in xrange(n-2):
            a,b=b,a+b
        return b