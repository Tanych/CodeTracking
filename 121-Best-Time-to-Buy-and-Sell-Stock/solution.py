class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low=1<<31
        profit=0
        for p in prices:
            low=min(low,p)
            profit=max(profit,p-low)
        return profit