class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for _ in xrange(n+1)]
        
        dp[0]=dp[1]=1
        
        for i in xrange(2,n+1):
            for j in xrange(i):
                # the number of left * the number of right
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]
            