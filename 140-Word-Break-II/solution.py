class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res=[]
        self.dfs(s,wordDict,'',res)
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
        return dp[n]
        
    def dfs(self,s,wordDict,path,res):
        """
        string for one level 
        res to store the result
        """
        if self.dpcheckbk(s,wordDict):
            if len(s)==0:
                #get rid of the first' '
                res.append(path[1:])
            for i in xrange(1,len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:],wordDict,path+' '+s[:i],res)
                    
    
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
            
        
        
        