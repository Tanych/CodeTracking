class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        buy=sell=0
        res=0
        while buy<n and sell<n:
            # find the local small prices
            while buy+1<n and prices[buy+1]<prices[buy]:
                buy+=1
            sell=buy
            while sell+1<n and prices[sell+1]>prices[sell]:
                sell+=1
            res+=prices[sell]-prices[buy]
            buy=sell+1
        return res
            