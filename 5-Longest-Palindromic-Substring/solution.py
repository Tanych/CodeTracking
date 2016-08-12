class Solution(object):
    def preprocess(self,s):
        n=len(s)
        newstr='^'
        for ch in s:
            newstr+='#'+ch
        newstr+='#$'
        return newstr
    
    def manacher(self,s):
        newstr=self.preprocess(s)
        n=len(newstr)
        pnum=[0]*n
        center=right=0
        #get rid of ^,$
        for i in xrange(1,n-1):
            i_mirror=center-(i-center)
            
            pnum[i]=min(right-i,pnum[i_mirror]) if right>center else 0
            
            # expand palindrome centered at i
            while newstr[i+1+pnum[i]]==newstr[i-1-pnum[i]]:
                pnum[i]+=1
            # if palindrome centered at i expand past R, adjust the center to i
            if i+pnum[i]>right:
                center=i
                right=i+pnum[i]
                
        # find the max
        maxlen=centeridx=0
        for i in xrange(1,n-1):
            if pnum[i]>maxlen:
                maxlen=pnum[i]
                centeridx=i
                
        sidx=(centeridx-maxlen-1)/2
        return s[sidx:sidx+maxlen]
            
    def longestPalindromeDP(self,s):
        """
        define: dp[i][j] means whether subtring[i,j] is a palindrome
        initial: dp[i][i] is true, for the single char
                dp[i][i+1] is true if s[i]==s[i+1]
        dp[i][j]=dp[i+1][j-1] if s[i]==s[j]
        """
        n=len(s)
        maxstart,maxlen=0,1
        dp=[[False for _ in xrange(n)] for _ in xrange(n)]
        
        for i in xrange(n):
            dp[i][i]=True
        for i in xrange(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                maxstart=i
                maxlen=2
        
        for k in xrange(3,n+1):
            # keep the length of palindrom is k, so i stop at n-k+1
            for i in xrange(n-k+1):
                # for padlinrome length of k, j start at i+k-1
                j=i+k-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    maxstart=i
                    maxlen=k
        return s[maxstart:maxstart+maxlen]
            
                
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.manacher(s)
        #return self.longestPalindromeDP(s)
        
        if not s:
            return ""
        str_len=len(s)
        longest=s[0]
        for i in range(str_len-1):
            p1=self.expandfromcenter(s,i,i)
            if len(p1)>len(longest):
                longest=p1
                
            p2=self.expandfromcenter(s,i,i+1)
            if len(p2)>len(longest):
                longest=p2
                
        return longest
    
    def expandfromcenter(self,s,c1,c2):
        left=c1
        right=c2
        str_len=len(s)
        while left>=0 and right<=str_len-1 and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    

    
    
    