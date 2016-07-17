class Solution(object):
    def myPow(self, x, n):
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
        
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        sum=0
        for i in xrange(n):
            sum+=int((ord(s[i])-ord('A')+1)*self.myPow(26,n-i-1))
        
        return sum