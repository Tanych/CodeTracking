class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n=len(s)
        dp=[False for i in xrange(n+1)]
        dp[0]=True
        
        for i in xrange(1,n+1):
            for k in xrange(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i]=True
                    break
        return dp[n]
        