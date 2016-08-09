class Solution(object):
    def __init__(self):
        self._dp=[0]
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        n=a+b*b
        dp[a+b*b]=min(dp[a]+1,dp[a+b*b])
        """
        dp=self._dp
        for i in xrange(n):
            dp+=[1<<31]
        
        i=0
        while i*i<=n:
            if i*i==n:
                return 1
            dp[i*i]=1
            i+=1
            
        for a in xrange(n+1):
            b=0
            while a+b*b<=n:
                dp[a+b*b]=min(dp[a]+1,dp[a+b*b])
                b+=1
                
        return dp[n]