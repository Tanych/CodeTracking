class Solution(object):
    def maxprofit_state(self,prices):
        state=[[-1<<31,0,-1<<31,0] for _ in xrange(2)]
        # using two mem to store the current state and next state
        # 0:buy  1: one buy and one sell 2:two buys and one sell 3: two buys and sells
        n=len(prices)
        cur,next=0,1
        for i in xrange(n):
            state[next][0]=max(state[cur][0],-prices[i])
            # 0 to 1, 1 to 2
            state[next][1]=max(state[cur][1],state[cur][0]+prices[i])
            state[next][2]=max(state[cur][2],state[cur][1]-prices[i])
            state[next][3]=max(state[cur][3],state[cur][2]+prices[i])
            cur,next=next,cur
        # at most transactions
        return max(state[cur][3],state[cur][1])
        
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        dynamic programming, assume the two transcation happens before i and after i,
        the maxprofit[i] is max(before[i]+after[i])
        """
        return self.maxprofit_state(prices)
        
        n=len(prices)
        if n<2:
            return 0
            
        preprofit=[0]*n
        postprofit=[0]*n
        maxprofit=0
        
        #get the maxprofit before i
        curmin=prices[0]
        for i in xrange(1,n):
            curmin=min(curmin,prices[i])
            preprofit[i]=max(preprofit[i-1],prices[i]-curmin)
        
        #get the array of sell post i
        curmax=prices[n-1]
        for i in xrange(n-2,-1,-1):
            curmax=max(curmax,prices[i])
            postprofit[i]=max(postprofit[i+1],curmax-prices[i])
        
        #get the maxprofit
        for i in xrange(n):
            maxprofit=max(maxprofit,preprofit[i]+postprofit[i])
        
        return maxprofit