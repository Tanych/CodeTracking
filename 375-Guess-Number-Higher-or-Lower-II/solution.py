class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
        
        # using small range to get the larger range
        for low in xrange(n,0,-1):
            for hi in xrange(low+1,n+1):
                globalmin=1<<31
                for x in xrange(low,hi):
                    localmax=max(dp[low][x-1],dp[x+1][hi])+x
                    globalmin=min(globalmin,localmax)
                dp[low][hi]=globalmin
                
        return dp[1][n]