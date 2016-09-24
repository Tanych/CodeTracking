class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        """
        the python way is not gernal,
        like do it like java and c++
        using dp and backtracking
        """
        
        # the dp is record substring[i,j] is a palindrome
        n=len(s)
        dp=[[False for _ in xrange(n)] for _ in xrange(n)]
        res=[]
        
        # check whether the partion is palindrome
        for cur in xrange(n):
            for pre in xrange(cur+1):
                if s[cur]==s[pre] and (cur-pre<=2 or dp[pre+1][cur-1]):
                    dp[pre][cur]=True
        # dfs search
        def dfs(res,path,pos):
            if pos==n:
                res.append(path)
                return
            for i in xrange(pos,n):
                # if currecnt pos is pandirome
                if dp[pos][i]:
                    # add to path check the rest
                    dfs(res,path+[s[pos:i+1]],i+1)
        
        dfs(res,[],0)
        return res
        