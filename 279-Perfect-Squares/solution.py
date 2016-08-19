class Solution(object):
    def __init__(self):
        self._dp=[0]
    
    def dpsolution(self,n):
        if n<=0:
            return 0
        
        dp=[1<<31]*(n+1)
        dp[0]=0
        for k in xrange(1,n+1):
            #For each i, it must be the sum of some number (i - j*j) and 
            #a perfect square number (j*j)
            j=1
            while j*j<=k:
                dp[k]=min(dp[k],dp[k-j*j]+1)
                j+=1
        return dp[-1]
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        n=a+b*b
        dp[a+b*b]=min(dp[a]+1,dp[a+b*b])
        """
        return self.dpsolution(n)
        
        dp=self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
        
        """
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
        """