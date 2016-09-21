class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find the lowest price to buy
        # and find the relative high price to sell
        n=len(prices)
        buy=sell=0
        res=0
        while buy<n and sell<n:
            while buy+1<n and prices[buy+1]<prices[buy]:
                buy+=1
            # get the lowest buy,find the highest forward
            sell=buy
            while sell+1<n and prices[sell+1]>prices[sell]:
                sell+=1
            res+=prices[sell]-prices[buy]
            buy=sell+1
        return res
            