class Solution(object):
 
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[False for _ in xrange(n)] for _ in xrange(n)]
        cutidx=[0 for _ in xrange(n)]
        
        # check whether the partion is palindrome
        for cur in xrange(n):
            # in the cur iteration, the max is cut into all single char
            # so its max its the number of gaps
            mincut=cur
            for pre in xrange(cur+1):
                if s[cur]==s[pre] and (cur-pre<=2 or dp[pre+1][cur-1]):
                    dp[pre][cur]=True
                    # if the s[pre;cur] is palindrome no need to cut
                    # else we need to calcute the previous index
                    """
                    a   c   a   |   a  b a
                                    j    i
                           j-1  |  [j, i] is palindrome
                       cutidx(j-1) +  1
                    """
                    mincut=0 if pre==0 else min(mincut,cutidx[pre-1]+1)
            cutidx[cur]=mincut
            
        return cutidx[n-1]
        