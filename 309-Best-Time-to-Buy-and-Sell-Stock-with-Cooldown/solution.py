class Solution(object):
    def maxProfit(self, prices):
        """
        DP solution:
        sate:
        buy[i]: means before day i what is the maxProfit for any sequence end with buy
        sell[i], rest[i] has the smilar meanings
        
        buy[i]  = max(rest[i-1]-price, buy[i-1]) 
        sell[i] = max(buy[i-1]+price, sell[i-1])
        rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        
        but rest[i]=sell[i-1] since buy before cool and sell after cool
        SO:
        buy[i] = max(sell[i-2]-price, buy[i-1])
        sell[i] = max(buy[i-1]+price, sell[i-1])
        
        """
        if not prices and len(prices)<=1:
            return 0
        pre_sell=pre_buy=sell=0
        buy=-1<<31
        for price in prices:
            pre_buy=buy
            # pre_sell save the status of sell[i-2]
            buy=max(pre_sell-price,pre_buy)
            # record the sell[i-1] but in next level it would be sell[i-2]
            pre_sell=sell
            # the sell in () in previous is sell[i-1] and sell has update so it's sell[i]
            sell=max(pre_buy+price,sell)
            
        return sell
            