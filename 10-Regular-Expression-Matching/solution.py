class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        # initial the value that a*b  value equal (disappear)b
        for j in range(1,len(p) + 1):
                if p[j-1] == '*':
                    # since * can make the preivous disappear
                    if j >= 2:
                        dp[0][j] = dp[0][j - 2]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # if preivous == or j-1 is . then match
                if p[j - 1] == '.'or s[i-1] == p[j-1]:   ## first case 
                    dp[i][j] = dp[i - 1][j - 1]
                # if preivous is *, check the previous 
                elif p[j - 1] == '*': 
                    # match 0 ele; match 1 ele
                    # match mutilple, for example 
                    # src:abcdeeee dst:abcde*
                    # check abceee match abcde* ==>check abcee match abcde* ==> and so on
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                    
        return dp[-1][-1]
        
            
        
            
            