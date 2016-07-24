class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[[0 for  _ in xrange(n+1)] for _ in xrange(n+1)]

        for lo in xrange(n,0,-1):
            for hi in xrange(lo+1,n+1):
                global_min =1<<31
                for x in xrange(lo,hi):
                    local_max=x+max(dp[lo][x-1],dp[x+1][hi])
                    global_min=min(global_min,local_max)
                    
                dp[lo][hi]=global_min
                
        return dp[1][n]