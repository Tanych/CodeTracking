class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        """
        definition: dp[i] means min coins to achieve total i
        result: return dp[amount]
        assume the initial would be inf 
        """
        
        dp=[1<<31 for _ in xrange(amount+1)]
        
        dp[0]=0
        n=len(coins)
        for i in xrange(n):
            for j in xrange(coins[i],amount+1):
                # get the min value using coins i
                # suppose coins[i]==5 , we need check
                # the min to get to 5, to check the min in dp[0]+1(5 coins)
                # if we check 6 ,we need know the min num to reach dp[1]+1(5 coins)
                dp[j]=min(dp[j-coins[i]]+1,dp[j])
                
        return -1 if dp[amount]==1<<31 else dp[amount]
        