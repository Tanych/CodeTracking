class Solution(object):
    def dfshelper(self,res,dp,path,pos,strs):
        # if reach the end of one path
        n=len(strs)
        if pos==n:
            res.append(path-1)
            return
        
        for i in xrange(pos,n):
            # if currecnt pos is pandirome
            if dp[pos][i]:
                # add to path check the rest
                self.dfshelper(res,dp,path+1,i+1,strs)
       
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[False for _ in xrange(n)] for _ in xrange(n)]
        res=[]
        
        # check whether the partion is palindrome
        for cur in xrange(n):
            for pre in xrange(cur+1):
                if s[cur]==s[pre] and (cur-pre<=2 or dp[pre+1][cur-1]):
                    dp[pre][cur]=True
        self.dfshelper(res,dp,0,0,s)
        return min(res)
        