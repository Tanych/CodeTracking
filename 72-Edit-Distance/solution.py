class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        Finally, it's always the dynamic programming
        there are three possible operation invovled
        Definiton: dp[i][j] means how many mini steps to convert word1[0:i-1] to word2[0:j-1]
        
        Result: dp[n][m], n is the length of word1,m is length of word2
        
        Corner case: one of the word1 and word2 is empty, dp[i][0] and dp[0][j]
                    dp[i][0]=i means delete i steps, dp[0][j]=j means insert j steps
                    
        General: dp[i][j]:
            A. word1[i-1]==word2[j-1], dp[i][j]=dp[i-1][j-1] don't do anything just pass
            B. word[i-1]!=word2[j-1]
               a) Replace, replace word[i-1] with word2[j-1], dp[i][j]=dp[i-1][j-1]+1
                  1 step for replacement
               b) Insert, insert word2[j-1] into word1[:i-1], 
                  it made word1[:i-1]+word2[j-1]==word2[:j-1], in other words,
                  we need convert word[:i-1] to word2[:j-2]
                  dp[i][j]=dp[i][j-1]+1 (1 step for insert)
               c) Deletion: delete word1[i-1] made word1[:i-2]==word2[:j-1]
                  dp[i][j]=dp[i-1][j]+1
              finally, we need get the min of the three
        """
        # initial
        n=len(word1)
        m=len(word2)
        dp=[[0 for _ in xrange(m+1)] for _ in xrange(n+1)]
        
        # corner case
        for i in xrange(1,n+1):
            dp[i][0]=i
        for j in xrange(1,m+1):
            dp[0][j]=j
        
        # gernal case
        for i in xrange(1,n+1):
            for j in xrange(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[n][m]
        
        