class Solution(object):
    """
    def __init__(self):
        self._dp=[0]
    """
    dp=[0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(len(self.dp), n+1):
            result = sys.maxsize
            k = int(math.sqrt(i))
            if k * k == i:
                self.dp.append(1)
                continue
            for j in range(1, int(math.sqrt(i)) + 1):
                result = min(result, self.dp[i - j * j] + 1)
                if result is 2:
                    break
            self.dp.append(result)
        return self.dp[n]
        
    def numSquares1(self,n):
        # DP TLE....
        if n<=0:
            return 0
        
        for i in xrange(1,n+1):
            self.dp+=[1<<31]
            
        self.dp[0]=0
        for k in xrange(1,n+1):
            #For each i, it must be the sum of some number (i - j*j) and 
            #a perfect square number (j*j)
            j=1
            while j*j<=k:
                self.dp[k]=min(self.dp[k],self.dp[k-j*j]+1)
                j+=1
        return self.dp[-1]
        
    def numSquares2(self, n):
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