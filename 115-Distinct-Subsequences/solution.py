class Solution(object):
     def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # To be clear, the question is to find the 
        # t string in s string which the position
        # shoule keep in original
        
        # It's a typical dp problem,the definition is as follows:
        # define: dp[i][j]: how many t[0,i] occurs in s[0,j]
        # initial: dp[0][j]=1 and dp[i][j]=0 since t(0,0)=""
        # it could 1 in every source string
        # gerneal: there are two situations:
        # 1. AE VS AECEE, if 'E' in AE comes from the last `E` in AECEEE
        # the problem transformed to how many A in AECE
        # dp[i][j]=dp[i-1]+dp[j-1]
        # 2. AE vs AECEE, if the E doesn't comes from the last 'E'
        # we need to find how many AE in AECE
        # dp[i][j]=dp[i][j-1]
        
        """
        O(mn)--O(mn)
        tlen=len(t)
        slen=len(s)
        dp=[[0 for _ in xrange(slen+1)] for _ in xrange(tlen+1)]
        dp[0][0]=1
        
        # initial the t 0 '' in s
        for i in xrange(tlen+1):
            for j in xrange(1,slen+1):
                if i==0: dp[i][j]=1
                else:
                    # i,j means the number of the string
                    # i-1 index means num i string
                    dp[i][j]=dp[i][j-1]+(dp[i-1][j-1] if t[i-1]==s[j-1] else 0)
                    
        return dp[tlen][slen]
        """
        
        # reduce the space to O(n)
        # since it only the previous result
        tlen=len(t)
        slen=len(s)
        dp=[0 for _ in xrange(tlen+1)]
        dp[0]=1
        for i in xrange(1,slen+1):
            pre=dp[0]
            for j in xrange(1,tlen+1):
                # record the value before change 
                # it means dp[i-1][j]
                tmp=dp[j]
                # update the dp[i][j]
                # pre corresponds to dp[i-1][j-1]
                dp[j]=tmp+(pre if t[j-1]==s[i-1] else 0)
                pre=tmp
                
        return dp[-1]
                