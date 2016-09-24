class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res=[]
        # 1.building divide dp 
        n=len(s)
        # dp[i] mean (i:n) can be divided
        dp=[False]*(n+1)
        dp[n]=True
        
        for j in xrange(n,0,-1):
            for i in xrange(j-1,-1,-1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i]=True

        def dfs(idx,path):
            """
            string for one level 
            res to store the result
            """
            if dp[idx]:
                if n==idx:
                    #get rid of the first' '
                    res.append(path[1:])
                    return
                for i in xrange(idx+1,n+1):
                    if s[idx:i] in wordDict and dp[i]:
                        dfs(i,path+' '+s[idx:i])
        dfs(0,'')
        return res
        
    def dpcheckbk(self,s,wordDict):
        n=len(s)
        dp=[False for i in xrange(n+1)]
        dp[0]=True
        
        for i in xrange(1,n+1):
            for k in xrange(0,i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i]=True
                    break
        return dp
        
    def dfs(self,s,idx,wordDict,path,res,dp):
        """
        string for one level 
        res to store the result
        """
        if dp[idx]:
            if len(s)==idx:
                #get rid of the first' '
                res.append(path[1:])
                return
            for i in xrange(idx+1,len(s)+1):
                if s[idx:i] in wordDict and dp[i]:
                    self.dfs(s,i,wordDict,path+' '+s[idx:i],res,dp)
                    
    
    def bkpos(self):
        """
        using bkpos[i] to store of the value for word[i:j] j in bkpos[i] is a 
        valid word in worddict.
        For example:
        bkpos[0]=[2,4,6] means s[0,2],s[0,4],s[0,6] are all valid words in dict
        """
        bkpos=[None]*n
        n=len(s)
        i=n-1
        while i>=0:
            if s[i:n] in wordDict:
                bkpos[i]=[n]
            else:
                bkpos[i]=[]
            #find all the possible value from i+1--n
            for j in xrange(i+1,n):
                #we need to make sure whether j has valid word,otherwise it won't work from j to n
                if  bkpos[j] and s[i:j] in wordDict:
                    bkpos[i].append(j)
            i-=1
            
        
        
        