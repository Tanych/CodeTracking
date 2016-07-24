class Solution(object):
        
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
        do it as a dp
        define: dp[i] means the ith number if 1count
        dp[0]=0
        """
        dp=[0 for _ in xrange(num+1)]
        for i in xrange(1,num+1):
            # if i is odd, the could the half+1
            # if i is even it equal the half
            # we can image than <<1 is double 
            # if the last digit is 0 we doulbe nothing
            # if the last digit is 1 we lose 1
            dp[i]=dp[i>>1]+1 if i&1 else dp[i>>1]
            
        return dp