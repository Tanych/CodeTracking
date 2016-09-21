class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/19750/my-c-solution-o-n-time-o-1-space-8ms
        # two state record the situation for
        # 0-one buy, 1:one buy one sell 2:2 buy and 1 sell 3:2 buy and 2 sell
        state=[[-1<<31,0,-1<<31,0],[-1<<31,0,-1<<31,0]]
        cur,nxt=0,1
        for price in prices:
            state[nxt][0]=max(state[cur][0],-price)
            state[nxt][1]=max(state[cur][1],state[cur][0]+price)
            state[nxt][2]=max(state[cur][2],state[cur][1]-price)
            state[nxt][3]=max(state[cur][3],state[cur][2]+price)    
            cur,nxt=nxt,cur
        return max(state[cur][1],state[cur][3])