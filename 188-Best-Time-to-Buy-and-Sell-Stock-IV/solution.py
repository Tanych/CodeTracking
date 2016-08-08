class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        """
        dp[i][j] means the max profit can achieve at days j with at most j transcations
                 |1.T[i][j-1] do nothing at jth day
        dp[i][j]=|best you can get by completing transaction at jth day
                 |2.(prices[j]-prices[m])+T[i-1][m] for m in [0:j-1] ( buy at mth day and sell at jth day)
        """ 
        
        days=len(prices)
        if days<2:
            return 0
            
        if k>=days:
            return self.maxprofit2(prices)
        dp=[[0 for _ in xrange(days)] for _ in xrange(k+1) ]
        
        for i in xrange(1,k+1):
            maxdiff=dp[i-1][0]-prices[0]
            for j in xrange(1,days):
                dp[i][j]=max(dp[i][j-1],prices[j]+maxdiff)
                maxdiff=max(maxdiff,dp[i-1][j]-prices[j])
        
        return dp[k][days-1]
        
        
    def maxprofit2(self,prices):
        days=len(prices)
        maxprofit=0
        for i in xrange(1,days):
            diff=prices[i]-prices[i-1]
            if diff>0:
                maxprofit+=diff
        return maxprofit
        