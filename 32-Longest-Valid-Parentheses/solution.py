class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        definite: dp[i] means the longest valid parentthese in s[:i]
        initial: 0 
        """
        n=len(s)
        if n<2:
            return 0
        
        dp=[0 for _ in xrange(n)]
        maxlen=0
        for i in xrange(1,n):
            # first we need to find the ')' and the previous is not ')'
            # if start with '(' all post EX； (((( )
            # Another is star with ')' no '(' before EX: )))))((((
            if s[i]=='(' or (s[i-1]==')' and not dp[i-1]):
                continue
            else:
                # if s[i]==')' and previous is '('
                if s[i-1]=='(':
                    dp[i]+=2
                    # check whether i-2 before has valid
                    dp[i]+=dp[i-2] if i-2>=0 else 0
                    maxlen=max(maxlen,dp[i])
                    
                #
                #                   i-dp[i-1]-1       i-1 i
                #if previous is) ( )    (         ( ) ( ) )
                #                0 1    2
                #
                # check the value s[i-dp[i-1]-1] is '(', idx--2 in above example
                elif s[i-1]==')' and (i-dp[i-1]-1)>=0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=2+dp[i-1]
                    # plus the previous valid value, the value is idx 1 in above example
                    dp[i]+=dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0
                    maxlen=max(maxlen,dp[i])
                    
        return maxlen
        
        
        
        