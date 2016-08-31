class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n ==0 or k == 0:
            return 0
        if n == 1:
            return k
        
        # the first two are same
        same = k
        # the fist two are diffirent 
        diff = k*(k-1)
        # check the previous two is same or diff
        for i in range(3,n+1):
            same,diff=diff,(k-1)*(same+diff)
        return same+diff